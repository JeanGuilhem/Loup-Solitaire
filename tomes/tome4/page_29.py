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

check_inventory(current_page_number=29, book=4)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
La Torche projette une lueur ardente qui, quelques secondes plus
tard, vacille et s'éteint. Vous essayez de la rallumer, mais vos
efforts restent vains. Si vous avez d'autres Torches dans votre Sac
à Dos, vous vous apercevrez que, pour quelque mystérieuse
raison, il vous sera également impossible de les allumer.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous disposez d'une Sphère de Feu, rendez-vous au :"))
    if has_item("SPHÈRE DE FEU"):
        st.page_link("tomes/tome4/page_168.py", label="168", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome4/page_168.py", label="168", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous souhaitez poursuivre votre chemin dans l'obscurité, rendez-vous au :"))
    st.page_link("tomes/tome4/page_246.py", label="246", icon="📄")

    st.write_stream(stream_text("Si vous préférez quitter l'endroit et essayer d'entrer par la porte de la crypte que surveillent les Gardes, rendez-vous au :"))
    st.page_link("tomes/tome4/page_183.py", label="183", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
