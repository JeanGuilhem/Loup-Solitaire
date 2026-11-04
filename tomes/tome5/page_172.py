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

check_inventory(current_page_number=172, book=5)

fr_text = """
« Entrez, étranger. Bienvenue dans mon humble taverne, dit
d'une voix accueillante la propriétaire rondelette de l'auberge.
Nous avons du vin et de la nourriture à volonté, et des chambres
à louer. » Elle a à peine terminé sa phrase que vous entendez les
hommes de Maouk faire irruption sur la Place. Ils jettent des
regards inquisiteurs vers la porte qui est restée ouverte. La
tenancière se rend compte de votre nervosité et vous montre du
doigt l'escalier de la cave. « Ne vous inquiétez pas, chuchote-t-
elle, nous partageons votre crainte du nouveau Zakhan, il n'y a
pas une seconde à perdre, descendez vous cacher ! » Vous n'avez
pas le choix, car les hommes de Maouk s'approchent déjà de la
taverne.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome5/page_16.py", label="16", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
