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

check_inventory(current_page_number=71, book=4)

fr_text = """
Tandis que le Guerrier tombe mort à vos pieds, vous vous
retournez vers vos hommes. Vous constatez alors avec horreur
que trois d'entre eux sont étendus sur les marches, tués par des
carreaux d'arbalète. Le quatrième est blessé et cerné par
l'ennemi. D'autres Gardes arrivent à ce moment. « Fuyez,
Seigneur Kaï, fuyez pendant qu'il en est encore temps ! » vous
crie le patrouilleur. A peine l'écho de ces paroles a-t-il retenti
qu'une épée lui transperce le cœur. Vous vous précipitez aussitôt
en direction d'un tunnel orienté au nord. Une porte est ouverte à
l'entrée de ce tunnel ; vous la claquez derrière vous dès que vous
l'avez franchie et vous tirez le verrou. Vous courez ensuite le long
du souterrain au sol couvert de poussière en priant le ciel que la
porte tienne et garde vos poursuivants à distance.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_348.py", label="348", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
