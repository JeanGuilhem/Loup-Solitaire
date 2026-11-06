import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    remove_from_inventory,
    set_flag,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=212, book=6)

fr_text = """
Vous procédez à l'échange. (N'oubliez pas d'apporter les
modifications nécessaires sur votre Feuille d'Aventure.) L'homme
vous tend les rênes de son cheval. « Bonne chance, habitant du
Nord, dit-il, tandis que vous grimpez en selle. J'espère que
vous retrouverez rapidement votre compagnon, il peut être fier
d'avoir un ami tel que vous ! » Vous lui dites adieu puis vous
éperonnez vigoureusement votre cheval.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # Fait posé : « cheval ». Venu du 45, vous donnez l'Arc en Chêne ; venu du 132 ou du 148, vous avez
    # déjà payé l'échange (20 Pièces d'Or ou 2 Objets Spéciaux) sur ces pages.
    if is_new_page():
        if st.session_state.last_page_number == 45:
            remove_from_inventory("ARC EN CHÊNE")
        set_flag("cheval")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_39.py", label="39", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
