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

check_inventory(current_page_number=16, book=4)

fr_text = """
Vous atteignez la porte que vous vous hâtez de franchir. A
l'extérieur de la taverne, le terrain est escarpé et couvert d'une
forêt dense. Deux de vos hommes vous suivent, mais ils sont tous
deux grièvement blessés et ne parviennent pas à courir aussi vite
que vous. Vous vous retournez pour les encourager de la voix,
mais ils sont alors brutalement frappés dans le dos et
s'effondrent morts sur le sol. Les brigands qui les ont tués
essuient leurs armes et se lancent à votre poursuite.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez vous enfuir tout droit dans la forêt, rendez-vous au :"))
    st.page_link("tomes/tome4/page_123.py", label="123", icon="📄")

    st.write_stream(stream_text("Si vous préférez changer de direction dès que les arbres vous cacheront aux yeux de vos poursuivants, rendez-vous au :"))
    st.page_link("tomes/tome4/page_169.py", label="169", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
