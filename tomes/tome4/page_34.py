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

check_inventory(current_page_number=34, book=4)

fr_text = """
La créature est éblouie par la clarté d'or du Glaive de Sommer.
Une expression de terreur apparaît sur son visage de vampire et
elle s'élance dans les airs pour éviter votre coup. Vous vous
préparez à frapper à nouveau, mais en vain : votre adversaire
silencieux vient de s'enfuir par une fente du plafond. Vous
remettez votre Glaive au fourreau et vous poursuivez votre
chemin. Vous remarquez alors une ouverture dans le mur, au-delà de laquelle s'étend un couloir long et étroit.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez emprunter ce couloir, rendez-vous au :"))
    st.page_link("tomes/tome4/page_235.py", label="235", icon="📄")

    st.write_stream(stream_text("Si vous préférez quitter les lieux et essayer d'entrer dans le temple par la porte de la crypte que surveillent les gardes, rendez-vous au :"))
    st.page_link("tomes/tome4/page_183.py", label="183", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
