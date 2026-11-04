import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=316, book=5)

fr_text = """
Après vous être péniblement remis debout, vous constatez que la
Nef du ciel est assaillie par les Drakkars. Ceux-ci ont en effet
sauté à bas de leurs Kraans hurlants et s'abattent maintenant sur
la passerelle et le pont, leurs noires épées déjà tirées de leur
fourreau et prêtes à frapper. Les Nains sont momentanément
pris de court, car toutes leurs armes ont été emmagasinées dans
la soute, mais ils ne tardent pas à se reprendre et à combattre de
toute leur énergie et de toute leur habileté. Une voix s'élève au-
dessus du vacarme et vous entendez Nolrim lancer son fameux
cri de guerre : « Œil pour œil, dent pour dent ! » Mais un coup
inattendu vous atteint dans le dos et vous fait tomber de la plate-
forme sur le pont en contrebas. Vous commencez à vous
redresser péniblement quand votre agresseur passe de nouveau à
l'attaque. Vous ne pouvez pas lui échapper :
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Étant donné la rapidité de l'attaque, réduisez votre total d'HABILETÉ de 2 points durant les 3 premiers Assauts."))
    outcome = combat([("DRAKKAR", 18, 26)], first_round_modifier=-2, first_rounds=3)
    if outcome == "win":
        st.write_stream(stream_text('Si vous sortez vainqueur du combat, rendez-vous au :'))
        st.page_link("tomes/tome5/page_333.py", label="333", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
