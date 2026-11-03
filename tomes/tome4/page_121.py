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

check_inventory(current_page_number=121, book=4)

fr_text = """
A peine votre adversaire s'est-il effondré à vos pieds qu'une autre
vague d'attaquants se rue en avant. Vos hommes sont courageux
et inflexibles, mais l'ennemi les surpasse en nombre et vous ne
pourrez pas le contenir indéfiniment. « Dans la mine ! » hurlez-vous
alors, tandis que les agresseurs se préparent à lancer une
nouvelle charge. Mais quatre de vos hommes seulement
parviennent jusqu'à la mine. Les autres ont été tués et leurs corps
restent étendus sur le champ de bataille, sous leurs boucliers.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_248.py", label="248", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
