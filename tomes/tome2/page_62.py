import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=62, book=2)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
Vous entrez dans une vaste pièce remplie de classeurs et de livres de
comptes. Face à vous, un homme revêtu d'un uniforme d'officier des
forces navales de Durenor est assis à un grand bureau. Il tient devant lui
un énorme livre posé debout sur le bureau. A votre entrée, l'homme
lève les yeux de son livre et vous jette un regard inquisiteur. « Vous
devez avoir des affaires bien urgentes à mener pour solliciter un
laissez-passer rouge à une heure aussi tardive. Je voudrais voir votre
permis d'entrée et l'autorisation de votre officier commandant. »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous avez réuni ces documents au cours de votre quête, rendez-vous au :"))
    if has_item("DOCUMENTS"):
        st.page_link("tomes/tome2/page_126.py", label="126", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome2/page_126.py", label="126", icon="📄", disabled=True)

    st.write_stream(
        stream_text(
            "Si vous n'avez pas les documents demandés, ou si vous ne souhaitez pas les présenter à cet"
            " homme, vous devrez prendre le risque de lui montrer le Sceau d'Hammardal et vous rendre "
            "dans ce cas au :"
        )
    )
    if has_item("SCEAU D'HAMMARDAL"):
        st.page_link("tomes/tome2/page_263.py", label="263", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome2/page_263.py", label="263", icon="📄", disabled=True)

    st.write_stream(
        stream_text(
            "Si vous n'avez ni le Sceau ni les documents, quittez la pièce et retournez dans le hall en"
            " vous rendant au :"
        )
    )
    st.page_link("tomes/tome2/page_318.py", label="318", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
