import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    show_illustrations,
    show_map,
)
from text import fr_unknown_magnakai
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=248, book=6)

fr_text = """
Les gardes cessent aussitôt l'inspection des chariots, et vous vous
retrouvez encerclé au milieu d'une forêt de lances. Le sergent
s'avance vers vous et hurle : « Jette tes armes, étranger, ou je te
laisse en pâture aux corbeaux ! » Puis, pour bien montrer qu'il ne
plaisante pas, il vous entaille la cuisse de la pointe de sa lance.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez riposter en attaquant le sergent, rendez-vous au :"))
    st.page_link("tomes/tome6/page_201.py", label="201", icon="📄")

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de l'Invisibilité, rendez-vous au :"))
    if has_magnakai("Invisibilité"):
        st.page_link("tomes/tome6/page_322.py", label="322", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome6/page_322.py", label="322", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
