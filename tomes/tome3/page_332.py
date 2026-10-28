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

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=332, book=3)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Au sommet de l'escalier, vous découvrez un vaste palier que
traverse un couloir orienté nord-sud.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez vous diriger vers le nord, rendez-vous au :"))
    st.page_link("tomes/tome3/page_104.py", label="104", icon="📄")
    st.write_stream(stream_text("Si vous préférez aller au sud, rendez-vous au :"))
    st.page_link("tomes/tome3/page_69.py", label="69", icon="📄")
    st.write_stream(stream_text("Enfin, si vous maîtrisez la Discipline Kaï du Sixième Sens ou celle de la Chasse, rendez-vous au :"))
    if has_kai("Le Sixième Sens") or has_kai("La Chasse"):
        st.page_link("tomes/tome3/page_249.py", label="249", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome3/page_249.py", label="249", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
