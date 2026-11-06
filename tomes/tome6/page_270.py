import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=270, book=6)

fr_text = """
Un tourbillon de ténèbres commence à se former au-dessus de
l'église, plongeant tout ce qui se trouve en dessous dans un froid
glacial et sépulcral. Une couche de givre recouvre les pelouses et
les fleurs, et, soudain, un terrible craquement déchire le silence
et la terre se met à trembler. Des fissures apparaissent dans le
sol sous vos pieds, et de nombreuses mains décharnées surgissent
du sol pour happer votre cheval. Terrifié, ce dernier se met à
hennir bruyamment, puis il fait une ruade désespérée qui vous
jette dans les bras tendus des Morts Vivants. L'effet de surprise
de cette attaque vous fait perdre 2 points d'HABILETÉ pour les 2
premiers Assauts du combat, à moins que vous ne possédiez la
Discipline Magnakaï de l'Art de la Chasse. Les Morts Vivants sont
insensibles au Foudroiement Psychique et à la Puissance Psychique.
Par ailleurs, si vous ne maîtrisez pas la Discipline Magnakaï de
Nexus, vous devez diminuer votre total d'ENDURANCE de 2 points à
chaque Assaut du combat, en raison du froid intense.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat(
        [("ASSEMBLÉE DES MORTS VIVANTS", 18, 35)],
        first_round_modifier=0 if has_magnakai("Art de la Chasse") else -2,
        first_rounds=2,
        psychic_immune=True,
        undead=True,
        # froid intense : -2 ENDURANCE à chaque assaut sans Nexus
        extra_loss=0 if has_magnakai("Nexus") else 2,
    )
    if outcome == "win":
        st.write_stream(stream_text("Si vous l'emportez, rendez-vous au :"))
        st.page_link("tomes/tome6/page_326.py", label="326", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
