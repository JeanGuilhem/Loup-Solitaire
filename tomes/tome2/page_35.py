import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=35, book=2)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Vous enjambez le soldat évanoui et vous vous hâtez de fuir la tour en
direction de la forêt car si d'autres gardes apparaissent, il y a tout à
parier qu'ils vous attaqueront avant de vous poser des questions. Vous
avez marché pendant plus de deux heures lorsque vous parvenez à une
bifurcation, à proximité d'un chêne rabougri.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous décidez d'aller à gauche, rendez-vous au :"))
    st.page_link("tomes/tome2/page_155.py", label="155", icon="📄")
    st.write_stream(stream_text("Si vous préférez aller à droite, rendez-vous au :"))
    st.page_link("tomes/tome2/page_293.py", label="293", icon="📄")
    st.write_stream(stream_text("Enfin, si vous maîtrisez la Discipline Kaï de l'Orientation, rendez-vous au :"))
    if has_kai("L'Orientation"):
        st.page_link("tomes/tome2/page_13.py", label="13", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome2/page_13.py", label="13", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
