import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=240, book=6)

fr_text = """
Vous avancez vers sa table mais, tout à coup, trois gardes aux
corps musclés surgissent devant vous et vous bloquent le
passage. Le marchand, coiffé d'un chapeau en velours au large
rebord, lève lentement la tête puis vous dit d'une voix frêle mais
sèche : « Qu'est-ce que vous me voulez, étranger ?»
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez lui demander le chemin de la rue des Chaudronniers, rendez-vous au :"))
    st.page_link("tomes/tome6/page_47.py", label="47", icon="📄")

    st.write_stream(stream_text("Si vous voulez lui dire que vous désirez faire quelques affaires avec lui, rendez-vous au :"))
    st.page_link("tomes/tome6/page_189.py", label="189", icon="📄")

    st.write_stream(stream_text("Enfin, si vous préférez vous excuser du dérangement que vous lui avez causé avant de vous diriger vers le comptoir, rendez-vous au :"))
    st.page_link("tomes/tome6/page_312.py", label="312", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
