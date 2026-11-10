import streamlit as st
from combat import combat
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=219, book=7)

fr_text = """
Vous attaquez le monstre et vous lui faites une profonde blessure
à la paupière. Mais avant que vous ne puissiez lui assener un
autre coup, une flamme rouge jaillit en sifflant de la grille et vous
atteint à l'épaule. Vous trébuchez en arrière, le bras paralysé par
une douleur atroce, et vos doigts devenus insensibles laissent
échapper votre arme qui tombe au sol avec un bruit métallique
(vous perdez 6 points d'ENDURANCE). Le serpent se tord et se
contorsionne dans tous les sens, et ses mâchoires grandes
ouvertes cherchent à vous mordre dans une rage aveugle. Il
trouve rapidement votre trace et s'apprête à se venger en lançant
une attaque fulgurante.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-6)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-6)

    st.write_stream(stream_text("Votre arme gît à vos pieds : vous combattez à mains nues (-4 HABILETÉ) pendant les 2 premiers Assauts. A moins que vous ne maîtrisiez la Science Médicale, les points d'ENDURANCE perdus au cours du combat sont multipliés par deux (venin)."))
    outcome = combat([("HACTARATON GÉANT", 20, 45)], key="hactaraton", unarmed_rounds=2,
                     ls_loss_multiplier=1 if has_magnakai("Science Médicale") else 2)
    if outcome == "win":
        st.write_stream(stream_text("Si vous remportez le combat, rendez-vous au :"))
        st.page_link("tomes/tome7/page_21.py", label="21", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
