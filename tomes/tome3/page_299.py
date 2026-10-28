import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=299, book=3)

fr_text = """
Si vous ne possédez pas la Discipline Kaï de la Maîtrise
Psychique de la Matière, des éclairs bleus jaillissent des piliers
noirs et vous atteignent en pleine poitrine. Vous êtes projeté en
arrière sous la force du choc et vous tombez de tout votre long
sur le sol glacé du temple. Vous perdez alors 2 points
d'ENDURANCE. S'il vous est possible, en revanche, de recourir à
la Discipline Kaï de la Maîtrise Psychique de la Matière, les
éclairs se révèlent inoffensifs pour vous et vous êtes indemne.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if has_kai("Maîtrise Psychique de la Matière"):
        st.success("*Grâce à la Maîtrise Psychique de la Matière, les éclairs se révèlent inoffensifs : vous êtes indemne.*")
    else:
        if is_new_page():
            change_endurance(-2)
        st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)

    st.write_stream(stream_text("Si vous voulez essayer à nouveau d'appuyer sur les boutons, rendez-vous au :"))
    st.page_link("tomes/tome3/page_65.py", label="65", icon="📄")

    st.write_stream(stream_text('Si vous préférez quitter le temple, rendez-vous au :'))
    st.page_link("tomes/tome3/page_306.py", label="306", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
