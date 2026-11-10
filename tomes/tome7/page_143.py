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

check_inventory(current_page_number=143, book=7)

fr_text = """
La vrille s'enroule rapidement autour de vous et vous enserre
solidement le cou. Puis, d'une brusque secousse, elle vous
arrache de la fissure et vous porte lentement vers la monstrueuse
gueule. Le désespoir le plus total s'empare de vous, surmontant
la peur et la douleur, lorsque vous sentez souffler sur votre visage
une haleine tiède et fétide.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez des Graines de Feu, rendez-vous au :"))
    st.page_link("tomes/tome7/page_10.py", label="10", icon="📄", disabled=not (has_item("GRAINE DE FEU")))

    st.write_stream(stream_text("Si vous possédez le Glaive de Sommer, rendez-vous au :"))
    st.page_link("tomes/tome7/page_317.py", label="317", icon="📄", disabled=not (has_item("GLAIVE DE SOMMER")))

    st.write_stream(stream_text("Si vous n'avez ni l'un ni l'autre de ces Objets Spéciaux, rendez-vous au :"))
    st.page_link("tomes/tome7/page_331.py", label="331", icon="📄", disabled=has_item("GRAINE DE FEU") or has_item("GLAIVE DE SOMMER"))

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
