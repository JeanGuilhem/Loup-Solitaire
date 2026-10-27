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

check_inventory(current_page_number=70, book=2)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
Vous haletez de douleur lorsque le serpent plonge ses crochets dans
votre bras. Vous saisissez le reptile juste derrière sa tête repoussante,
vous l'arrachez à votre bras et vous le jetez dans l'herbe. Mais le serpent
a eu le temps de vous infliger une profonde morsure et son venin
commence à faire de l'effet.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez le Pendentif à l'Étoile de Cristal, rendez-vous au :"))
    if has_item("PENDENTIF À L'ÉTOILE DE CRISTAL"):
        st.page_link("tomes/tome2/page_219.py", label="219", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome2/page_219.py", label="219", icon="📄", disabled=True)

    st.write_stream(stream_text("Dans le cas contraire, rendez-vous au :"))
    st.page_link("tomes/tome2/page_44.py", label="44", icon="📄", disabled=has_item("PENDENTIF À L'ÉTOILE DE CRISTAL"))

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
