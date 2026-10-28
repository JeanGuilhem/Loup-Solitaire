import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_flag,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=70, book=3)

fr_text = """
« Vite ! il faut remballer nos affaires et partir immédiatement !
s'écrie Fenor, tandis que le mugissement du vent emporte ses
paroles dans la nuit noire. Les Languabarbs ne chassent jamais
seuls ; il y en a sûrement d'autres à proximité et ils sentent
l'odeur du sang à des kilomètres à la ronde. » Vous démontez la
tente et vous vous hâtez de partir, Dyce ouvrant la marche, vous-
même surveillant les arrières. Mais à peine avez-vous parcouru
une cinquantaine de mètres qu'une catastrophe survient. Aveuglé
à la fois par le vent et l'obscurité, Dyce ne remarque pas que le
chemin s'arrête brusquement, tout au bord d'un précipice. Votre
sang se glace d'horreur lorsque vous entendez les cris de vos
deux guides retentir dans les ténèbres, puis décroître tout au
long de leur chute. La mort vous menace de tous côtés et vous
vous cramponnez désespérément à la paroi glacée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous vous êtes enduit le corps d'huile de Bakanal, rendez-vous au :"))
    st.page_link("tomes/tome3/page_209.py", label="209", icon="📄", disabled=not has_flag("huile de Bakanal"))

    st.write_stream(stream_text("Dans le cas contraire, rendez-vous au :"))
    st.page_link("tomes/tome3/page_339.py", label="339", icon="📄", disabled=has_flag("huile de Bakanal"))

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
