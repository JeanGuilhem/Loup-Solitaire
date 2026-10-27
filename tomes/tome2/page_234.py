import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies, ls_death

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=234, book=2)

fr_text = """
Avant que vous ayez pu esquisser un geste pour vous défendre, le
Monstre d'Enfer s'est jeté sur vous et vous tombez tous deux sur la
chaussée en contrebas. Vous éprouverez peut-être quelque consolation
en apprenant que votre mort a été soudaine et indolore. Vous vous êtes
rompu le cou dans votre chute et vous n'aurez donc pas le désagrément
de sentir les doigts décharnés du Monstre d'Enfer s'enfoncer dans votre
gorge en vous déchirant la peau de leurs griffes pointues. Le Sceau
d'Hammardal retournera désormais à Holmgard et la ville tombera aux
mains des Maîtres des Ténèbres. Votre mission s'achève donc ici en
même temps que votre vie.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    show_illustrations()
    ls_death()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
