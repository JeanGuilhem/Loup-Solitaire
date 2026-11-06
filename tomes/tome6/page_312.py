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

check_inventory(current_page_number=312, book=6)

fr_text = """
Le tavernier est en train de séparer deux soldats soûls qui se
battent. Il a trouvé un moyen efficace pour les mettre d'accord : il
prend les deux hommes par le cou et cogne leurs têtes l'une
contre l'autre, avec une force telle que vous pouvez entendre le
bruit qu'elles font en se heurtant malgré le vacarme qui règne
dans la taverne. Vous vous approchez du tavernier et lui
demandez où se trouve la rue des Chaudronniers. « La rue des
Chaudronniers ? répète-t-il en se grattant la tête. Oui, je la
connais bien. Venez, je vais vous la montrer. » Il vous entraîne à
l'écart puis sort un bout de papier froissé de sa poche sur lequel il
griffonne un plan. La rue se trouve à l'autre bout de la ville, près
du mur d'enceinte ouest. Vous mettez le papier dans votre poche
et remerciez le tavernier qui retourne au milieu de la foule des
consommateurs pour régler un autre différend de sa manière
inimitable.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome6/page_17.py", label="17", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
