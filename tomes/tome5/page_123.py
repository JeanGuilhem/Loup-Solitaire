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

check_inventory(current_page_number=123, book=5)

fr_text = """
Le bruit s'amplifie. Soudain, le loquet de la porte grince et une
voix bourrue s'élève au-dessus du vacarme : « Enfoncez la porte ! »
Une hache à double tranchant transperce les planches, des
morceaux de bois et des barres de fer tordues sont violemment
projetés dans la cave. Finalement, la porte sort de ses gonds et
vos poursuivants font irruption dans la pièce en se bousculant,
gênés par l'enchevêtrement des planches brisées qui jonchent le
sol. Aussitôt, vous vous jetez en avant dans la mêlée en donnant
des coups à gauche et à droite. Vous étendez à terre deux
hommes avant même qu'ils ne vous aient aperçu. L'Officier, un
grand guerrier au cou de taureau et au nez écrasé, se fraie un
chemin à coups de coude parmi les hommes, puis il passe à
l'attaque. Vous frappez le premier et, d'un coup bien placé à son
poignet, vous le dépossédez de son cimeterre. Mais il passe de
nouveau à l'attaque. Il tient maintenant dans sa main valide un
grand poignard et il se jette sur vous en soufflant comme un
bœuf.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("OFFICIER SHARNAZIM", 18, 28)], flee_after=0)
    if outcome == "fled":
        st.write_stream(stream_text("Vous pouvez prendre la fuite à tout moment en vous échappant par la trappe. Dans ce cas, rendez-vous au :"))
        st.page_link("tomes/tome5/page_51.py", label="51", icon="📄")
    elif outcome == "win":
        st.write_stream(stream_text("Si vous remportez le combat, rendez-vous au :"))
        st.page_link("tomes/tome5/page_198.py", label="198", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
