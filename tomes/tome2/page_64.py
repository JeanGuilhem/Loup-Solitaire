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

check_inventory(current_page_number=64, book=2)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Un peu plus loin, vous apercevrez une diligence semblable à celles qui
transportent les voyageurs le long des côtes menant à Ragadorn. Les
chevaux ont été dételés et le véhicule semble abandonné. Vous
remarquez alors les corps de trois soldats étendus entre les roues. Leurs
uniformes sont tachés de sang.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Si vous souhaitez fouiller la diligence en espérant y trouver de la nourriture ou quelque "
            "objet utile, rendez-vous au :"
        )
    )
    st.page_link("tomes/tome2/page_134.py", label="134", icon="📄")

    st.write_stream(
        stream_text(
            "Si vous préférez poursuivre votre chemin sans vous attarder, rendez-vous au :"
        )
    )
    st.page_link("tomes/tome2/page_208.py", label="208", icon="📄")

    st.write_stream(
        stream_text(
            "Si enfin vous maîtrisez la Discipline Kaï du Sixième Sens, rendez-vous au :"
        )
    )
    if has_kai("Le Sixième Sens"):
        st.page_link("tomes/tome2/page_229.py", label="229", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome2/page_229.py", label="229", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
