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

check_inventory(current_page_number=272, book=6)

fr_text = """
Dehors, le soleil commence à poindre par-dessus les arbres, et une
agréable odeur d'herbe mouillée embaume l'air du petit matin. Vous
sellez votre cheval et continuez votre voyage. La route passe
entre deux rangées de collines noyées dans le brouillard. Vers
midi, vous atteignez un petit village. Ses cottages richement
décorés sont regroupés autour d'une place pavée. Au centre se
dresse une espèce de serre coiffée d'un dôme immense, en forme de
bulbe. A l'ombre du dôme poussent des rangées d'arbustes aux
fruits orange surveillées par un groupe de vieilles femmes assises
sur des bancs.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez vous arrêter pour examiner cette étrange serre, rendez-vous au :"))
    st.page_link("tomes/tome6/page_342.py", label="342", icon="📄")

    st.write_stream(stream_text("Si vous préférez continuer directement votre chemin vers Varetta, rendez-vous au :"))
    st.page_link("tomes/tome6/page_100.py", label="100", icon="📄")

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de la Science Médicale, rendez-vous au :"))
    if has_magnakai("Science Médicale"):
        st.page_link("tomes/tome6/page_250.py", label="250", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome6/page_250.py", label="250", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
