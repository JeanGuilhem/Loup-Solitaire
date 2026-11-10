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

check_inventory(current_page_number=149, book=7)

fr_text = """
Le Seigneur Zahda pousse un hurlement inhumain quand votre
lame lui transperce le cœur. Il tend une main implorante vers le
ciel avant de s'écrouler à genoux, et la malédiction qu'il
s'apprêtait à lancer se noie dans le flot de sang qui jaillit de sa
bouche. Son œil gauche s'allume d'un vif éclat pendant une
fraction de seconde, telle la flamme d'une bougie vacillant dans
la tempête avant de s'éteindre sous la pluie. Puis il bascule en
avant et tombe de l'estrade dans le puits, où il est
immédiatement dévoré par les flammes rugissantes. Vous vous
précipitez vers le trône, dégainez à nouveau votre arme et
assenez un formidable coup au cristal noir. Celui-ci s'ouvre en
deux, laissant échapper son pouvoir maléfique en une myriade
d'étincelles sombres. Les fragments de la Pierre du Mal tombent
à leur tour dans le brasier, et le feu s'apaise brusquement. Des
profondeurs du puits s'élève alors un terrible grondement.
L'estrade se met à trembler et une colonne de feu illumine la
salle du trône, tandis qu'un flot de lave en fusion jaillit dans les airs.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez vous emparer de la Pierre de la Sagesse et prendre la fuite par le tube d'acier, rendez-vous au :"))
    st.page_link("tomes/tome7/page_250.py", label="250", icon="📄")

    st.write_stream(stream_text("Si vous préférez prendre la Pierre de la Sagesse et chercher un autre moyen de vous évader de ce lieu infernal, rendez-vous au :"))
    st.page_link("tomes/tome7/page_267.py", label="267", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
