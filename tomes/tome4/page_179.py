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

check_inventory(current_page_number=179, book=4)

fr_text = """
Le pilier de bois ploie peu à peu sous vos coups puis se casse
soudain. Un tremblement secoue alors le tunnel ; vous trébuchez
et vous tombez à terre. Vous vous relevez aussitôt et, tandis que
vous courez vous mettre à l'abri, un déluge de terre et de pierres
se déverse dans le souterrain. Une onde de choc vous frappe de
plein fouet dans le dos et vous projette sur le sol ; un nuage de
poussière se répand dans l'air. Vous vous relevez tant bien que
mal et vous poursuivez votre chemin d'un pas chancelant, mais il
vous faut marcher une demi-heure avant d'arriver à un endroit
du tunnel où l'air redevient respirable et où les Torches fixées
aux parois continuent de brûler.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_335.py", label="335", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
