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

check_inventory(current_page_number=135, book=4)

fr_text = """
Les étendues plates et désolées du Pays Sauvage n'offrent aucun
abri pour vous dissimuler aux yeux des hordes de brigands. Ces
derniers sont quatre fois plus nombreux que vous et la vie ou la
mort de toute votre troupe dépend à présent de la décision que
vous prendrez.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez partir à l'attaque des brigands dans l'espoir qu'une action audacieuse saura les effrayer, rendez-vous au :"))
    st.page_link("tomes/tome4/page_284.py", label="284", icon="📄")

    st.write_stream(stream_text("Si vous préférez séparer vos hommes en deux groupes, vous partirez d'un côté avec dix patrouilleurs, tandis que les autres prendront la direction de l'ouest pour essayer d'attirer les bandits vers les monts Durncrag. Rendez-vous pour cela au :"))
    st.page_link("tomes/tome4/page_211.py", label="211", icon="📄")

    st.write_stream(stream_text("Enfin, si vous estimez plus judicieux de galoper vers le sud pour essayer d'atteindre la forêt de Ruanon avant que les bandits n'aient pu vous rattraper, rendez-vous au :"))
    st.page_link("tomes/tome4/page_30.py", label="30", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
