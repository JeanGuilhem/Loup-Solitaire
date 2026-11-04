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

check_inventory(current_page_number=83, book=5)

fr_text = """
Il s'agit du registre de l'Armurerie, où sont minutieusement
consignés tous les mouvements d'armes : le nombre de lances et
d'épées destinées à la garnison de Kara-Kala, les cargaisons de
minerai en provenance des Monts de Vakar, les armes devant
être réparées, etc. Vous vous apprêtez à vous débarrasser du
registre lorsque vous remarquez qu'un bout de parchemin plié en
quatre est glissé au dos de la reliure. C'est une liste de dates et de
nombres qui porte comme en-tête : « La Porte de Bronze ». Vous
parcourez la liste jusqu'à ce que vous trouviez la date du jour. Le
nombre inscrit en regard est 67. Notez ce chiffre dans la marge
de votre Feuille d'Aventure, car il pourra vous être utile
ultérieurement. Après avoir reposé le livre sur l'établi, vous vous
mettez à chercher votre équipement.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_181.py", label="181", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
