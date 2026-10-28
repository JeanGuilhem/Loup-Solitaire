import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=184, book=3)

fr_text = """
Ce tunnel n'est pas très long et vous arrivez bientôt dans une
petite caverne. Deux cadavres humains sont étendus sur le sol et,
en dépit de la température glaciale qui règne en ces lieux, leur
état de décomposition est déjà bien avancé. De toute évidence, il
y a très longtemps que ces hommes sont morts. Tous deux sont
vêtus de fourrure et l'un d'eux tient encore à la main un poignard
en silex. A en juger par la position des corps, il semblerait que ces
deux hommes se soient entre-tués au cours d'un combat
particulièrement acharné.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez fouiller ces cadavres, rendez-vous au :'))
    st.page_link("tomes/tome3/page_298.py", label="298", icon="📄")
    st.write_stream(stream_text("Si vous préférez poursuivre votre chemin, vous pouvez quitter cette caverne en empruntant un tunnel qui s'ouvre dans le mur du fond. Rendez-vous pour cela au :"))
    st.page_link("tomes/tome3/page_315.py", label="315", icon="📄")
    st.write_stream(stream_text("Enfin, s'il vous semble plus judicieux de revenir sur vos pas et d'emprunter l'autre tunnel, rendez-vous au :"))
    st.page_link("tomes/tome3/page_125.py", label="125", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
