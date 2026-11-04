import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=333, book=5)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
Vous apercevez Nolrim en train de se frayer un chemin parmi
une foule de Drakkars tout habillés de rouge ; par trois fois il
abat sa hache et fait mouche à chaque coup. Arrivé près de vous,
il désigne de son arme sanguinolente une créature planant au-
dessus de la Nef du ciel. Il s'agit d'un Zlan, un oiseau apparenté
aux Kraans, mais de bien plus large envergure. Il sert de monture
à un Vordak vêtu de rouge qui tient un long tube de fer noir dans
sa main osseuse. Soudain, un éclair jaillit au bout de cette arme
étrange, suivi d'une vive langue de feu bleuâtre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous possédez le Glaive de Sommer, rendez-vous au :'))
    if has_item("GLAIVE DE SOMMER"):
        st.page_link("tomes/tome5/page_258.py", label="258", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome5/page_258.py", label="258", icon="📄", disabled=True)

    st.write_stream(stream_text('Si vous ne possédez pas cet Objet Spécial, rendez-vous au :'))
    if has_item("GLAIVE DE SOMMER"):
        st.page_link("tomes/tome5/page_348.py", label="348", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome5/page_348.py", label="348", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
