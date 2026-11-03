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

check_inventory(current_page_number=107, book=4)

fr_text = """
Le bandit à cheval vous poursuit, sa lance se rapprochant de
votre dos à une allure inquiétante. Vous courez à toutes jambes
en direction d'un soldat du Sommerlund qui se trouve juste sur
votre chemin, son arc tendu, prêt à tirer. « Plongez ! » vous crie
l'archer. Instinctivement, vous obéissez à son ordre. Presque en
même temps, il lâche la corde de son arc. Le bandit à cheval n'est
plus qu'à quelques mètres de vous, lorsque la pointe d'acier de la
flèche s'enfonce dans sa visière et ressort à l'arrière de son
heaume comme une broche transperçant une pomme. Son cheval
trébuche et tombe à terre, projetant le cadavre du cavalier à vos
côtés. Vous vous apprêtez à remercier le soldat qui vient de vous
sauver, mais celui-ci court déjà vers la barricade.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez le suivre, rendez-vous au :'))
    st.page_link("tomes/tome4/page_59.py", label="59", icon="📄")

    st.write_stream(stream_text('Si vous préférez continuer en direction de la tour de guet, rendez-vous au :'))
    st.page_link("tomes/tome4/page_310.py", label="310", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
