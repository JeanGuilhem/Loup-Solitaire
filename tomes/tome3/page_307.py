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

check_inventory(current_page_number=307, book=3)

fr_text = """
Vous vous préparez à combattre et vous faites signe aux autres de
passer à l'attaque. Les Barbares des Glaces ont tôt fait de
mesurer le danger qui les menace et ils s'enfuient vers l'ouest.
Vous avez alors la mauvaise surprise de constater qu'ils sont
équipés de skis et peuvent ainsi s'échapper très vite. Chacun de
ces Barbares vêtus de fourrure porte attaché dans le dos une tige
au bout de laquelle flotte un étrange drapeau bleu. « Ce sont les
éclaireurs d'un convoi de traîneaux, dit Irian, la main en visière
pour se protéger de l'éclat de la neige, leurs " Banachs bleus "
(c'est ainsi que l'on appelle leurs drapeaux) indiquent qu'ils
escortent une expédition de marchands. Ils reviennent
probablement du comptoir de Liouk. Leur convoi ne doit pas être
à plus de quelques kilomètres, 7 ou 8 tout au plus. »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez poursuivre votre chemin en direction d'Ikaya en essayant de prendre les Barbares de vitesse avant qu'ils ne puissent revenir avec des renforts, rendez-vous au :"))
    st.page_link("tomes/tome3/page_327.py", label="327", icon="📄")
    st.write_stream(stream_text("Si vous préférez suivre ces éclaireurs vers l'ouest pour essayer d'en savoir plus au sujet de leur convoi, rendez-vous au :"))
    st.page_link("tomes/tome3/page_178.py", label="178", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
