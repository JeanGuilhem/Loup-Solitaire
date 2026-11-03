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

check_inventory(current_page_number=5, book=4)

fr_text = """
Vous le projetez à terre et, à l'aide de votre cape de Seigneur Kaï,
vous étouffez le feu qui le dévore. Les flammes s'éteignent
bientôt et vous vous hâtez d'enlever votre cape pour voir si le
capitaine est blessé. La promptitude de vos réflexes lui a sauvé la
vie : il est indemne ; en effet, seul son uniforme est brûlé et
déchiré. « C'est à mon tour de vous remercier, Loup Solitaire,
cette fois c'est vous qui m'avez sauvé d'une mort certaine. » Vous
aidez le capitaine à se relever et vous vous précipitez vers la
barricade. L'ennemi a maintenant atteint le périmètre en ruines
de Ruanon et s'avance peu à peu à l'abri des murs encore debout.
Vous montez sur un chariot retourné et vous ordonnez aux
soldats du Sommerlund de revenir sur les barricades. Mais est-il
encore temps de repousser l'attaque ?
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_186.py", label="186", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
