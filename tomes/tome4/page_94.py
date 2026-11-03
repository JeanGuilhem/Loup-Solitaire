import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    lose_backpack,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=94, book=4)

fr_text = """
Soudain, le bateau bascule en avant et vous êtes projeté en l'air.
Vous tombez pendant ce qui vous semble être une éternité, avant
de heurter la surface de l'eau avec une telle violence que vous
plongez à plus de 6 mètres de profondeur. L'eau glacée vous
assomme à moitié et brise vos forces. Vous cherchez
désespérément à respirer un peu d'air en vous débattant pour
tenter de remonter à la surface. Votre Sac à Dos, cependant, vous
entraîne au fond et vous devez vous en débarrasser pour ne pas
vous noyer. Lorsqu'enfin vous parvenez à l'air libre, le courant
vous entraîne en vous éloignant de la chute d'eau. Vous vous
échouez bientôt sur une rive de graviers au fond d'un ravin
escarpé. Vous avez perdu votre Sac à Dos avec tout ce qu'il
contenait ainsi que votre bateau et vos hommes mais, en dépit du
désastre, vous êtes toujours vivant et à peu près indemne.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        lose_backpack()
    st.warning("*Vous avez perdu votre Sac à Dos et tout son contenu.*")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_219.py", label="219", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
