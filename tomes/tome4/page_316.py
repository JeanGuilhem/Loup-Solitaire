import streamlit as st
from combat import combat
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

check_inventory(current_page_number=316, book=4)

fr_text = """
Vous êtes arrivé à mi-chemin, lorsqu'un de vos hommes glisse
soudain et se trouve emporté par le courant torrentiel de la
rivière. Ses cris désespérés alertent les brigands et, tout à coup,
un Guerrier Pillard surgit au sommet du gros rocher derrière
lequel vous vous cachiez. Il pousse un hurlement et vous porte un
coup de lance. Pendant toute la durée de ce combat, vous devrez
réduire de 2 points votre total d'HABILETÉ en raison de votre
position désavantagée. Le brigand se trouve en effet au-dessus de
vous, et vous vous tenez sur un sol humide et glissant.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("GUERRIER PILLARD", 16, 26)], hability_modifier=-2, flee_after=0)
    if outcome == "win":
        st.write_stream(stream_text("Si vous remportez la victoire, rendez-vous au :"))
        st.page_link("tomes/tome4/page_146.py", label="146", icon="📄")
    elif outcome == "fled":
        st.write_stream(stream_text("Vous vous enfuyez en plongeant dans l'eau de la rivière Xane. Rendez-vous au :"))
        st.page_link("tomes/tome4/page_31.py", label="31", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
