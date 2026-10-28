import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

fr_unknown_item = "Vous ne possédez pas cet objet."

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=97, book=3)

fr_text = """
Tout au long de ce couloir se dressent des pilastres de pierre
disposés à intervalles réguliers. Ils ont plusieurs dizaines de
centimètres d'épaisseur et vous permettent donc de vous cacher
en cas de besoin. A une vingtaine de mètres devant vous, vous
apercevez un Barbare des Glaces qui monte la garde au pied d'un
large escalier de pierre. Vous vous dissimulez aussitôt derrière
un des piliers, réfléchissant à un moyen de vous débarrasser de
ce gêneur. Il n'en existe que deux : distraire son attention, ou le
faire taire à tout jamais.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous possédez un Diamant, rendez-vous au :'))
    if has_item("DIAMANT"):
        st.page_link("tomes/tome3/page_24.py", label="24", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome3/page_24.py", label="24", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous souhaitez distraire l'attention du garde à l'aide de quelques Pièces d'Or, rendez-vous au :"))
    st.page_link("tomes/tome3/page_152.py", label="152", icon="📄")

    st.write_stream(stream_text("Enfin, si vous jugez préférable de l'attaquer, rendez-vous au :"))
    st.page_link("tomes/tome3/page_208.py", label="208", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
