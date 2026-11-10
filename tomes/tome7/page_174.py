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

check_inventory(current_page_number=174, book=7)

fr_text = """
Des flammes bleues jaillissent de la baguette de Zahda, mais
vous parvenez à les intercepter et à les dévier grâce à la lame du
Glaive de Sommer. L'éclair meurtrier se dirige maintenant en
sifflant vers la salle obscure et détruit un rang entier de gradins
dans une terrible secousse. « Vous allez mourir... mourir...
MOURIR ! » hurle Zahda comme un possédé. Il fait tourner sa
baguette deux fois au-dessus de sa tête avant de se précipiter sur
vous, ses mains griffues tendues en avant. Le Seigneur Zahda est
immunisé contre la Puissance Psychique et le Foudroiement
Psychique.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("ZAHDA (armé de sa baguette magique)", 33, 45)], psychic_immune=True)
    if outcome == "win":
        st.write_stream(stream_text("Si vous remportez le combat, rendez-vous au :"))
        st.page_link("tomes/tome7/page_149.py", label="149", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
