import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=315, book=4)

fr_text = """
A la lueur vacillante de votre Torche, vous remarquez que le
tunnel est étayé par des piliers et des poutres. Les murs suintent
d'humidité, et une étroite rigole d'eau teintée par le minerai
coule sur le sol. Vous parvenez bientôt à une bifurcation.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez aller à gauche, rendez-vous au :"))
    st.page_link("tomes/tome4/page_269.py", label="269", icon="📄")

    st.write_stream(stream_text("Si vous préférez aller à droite, rendez-vous au :"))
    st.page_link("tomes/tome4/page_145.py", label="145", icon="📄")

    if has_kai("L'Orientation"):
        st.write_stream(stream_text("Enfin, si vous maîtrisez la Discipline Kaï de l'Orientation, rendez-vous au :"))
        st.page_link("tomes/tome4/page_48.py", label="48", icon="📄")
    else:
        st.write_stream(stream_text("Enfin, si vous maîtrisez la Discipline Kaï de l'Orientation, rendez-vous au :"))
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome4/page_48.py", label="48", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
