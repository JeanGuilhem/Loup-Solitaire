import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=55, book=7)

fr_text = """
Au bas de l'escalier s'étend un vestibule désert qui mène à une
imposante porte en bronze à deux battants. De somptueuses
tapisseries et des statuettes en or s'alignent de chaque côté, et
l'eau d'une fontaine en marbre incrusté d'argent emplit le
vestibule de son ruissellement mélodieux. Mais à peine avez-vous
 fait quelques mètres qu'un garde en armure surgit de
derrière la fontaine. Il est armé d'une arbalète et s'empresse de
vous prendre pour cible.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard. Si vous possédez la Discipline Magnakaï de l'Art de la Chasse ou de l'Intuition, ajoutez 3 au chiffre que vous avez tiré."))
    roll = hazard_roll(key="arbalete")
    if roll is not None:
        total = roll + (3 if has_magnakai("Art de la Chasse") or has_magnakai("Intuition") else 0)
        st.write(f"*Résultat : {total}.*")
        st.write_stream(stream_text("Si le résultat obtenu est compris entre 0 et 2, rendez-vous au :"))
        st.page_link("tomes/tome7/page_189.py", label="189", icon="📄", disabled=total > 2)
        st.write_stream(stream_text("Si ce résultat est supérieur ou égal à 3, rendez-vous au :"))
        st.page_link("tomes/tome7/page_62.py", label="62", icon="📄", disabled=total < 3)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
