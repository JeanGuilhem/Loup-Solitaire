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

check_inventory(current_page_number=81, book=5)

fr_text = """
Vous reconnaissez avec horreur les symptômes de la Paralysie
des Membres ! Votre blessure est déjà infectée par des myriades
de microbes qui comptent parmi les plus mortels de toutes les
espèces de bactéries du Baga-darooz. Aucune de vos Disciplines
Kaï ne pourra vous empêcher de perdre l'usage de votre bras d'ici
quelque temps. Le seul et unique remède serait d'appliquer sur
votre plaie de l'herbe d'Oede avant 24 heures. Si vous ne
parvenez pas à vous procurer cette herbe avant demain après-midi,
la gangrène apparaîtra et vous devrez choisir entre perdre
votre bras... ou votre vie. Cette effrayante perspective renforce
votre résolution de vous évader de cet horrible endroit. Car une
chose est certaine : ce n'est pas dans le Baga-darooz que vous
trouverez l'herbe d'Oede !
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous maintenant au :"))
    st.page_link("tomes/tome5/page_166.py", label="166", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
