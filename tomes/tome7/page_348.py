import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=348, book=7)

fr_text = """
Vous arrivez rapidement à un autre escalier, mais celui-ci est
intact et monte vers l'entrée de ce qui semble être une grotte
située au creux de l'abrupte paroi rocheuse. Vous ne pouvez pas
longer la plage plus avant car une saillie du rempart de la
forteresse bloque le chemin. De plus, le temps se gâte, et vous
devez chercher un abri avant que la tempête n'éclate. Vous
grimpez donc les marches vers la grotte et, lorsque vous arrivez
devant l'entrée, la tempête commence déjà à faire rage : le sol
tremble à chaque coup de tonnerre et un vent puissant souffle
sur la plage. Une pluie violente se met à tomber, et vous entrez
prudemment dans la grotte qui n'est éclairée que par la faible
lumière du bouclier de protection. Mais vous êtes bientôt
environné par les ténèbres, et votre progression devient
terriblement lente.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    light = has_item("GRAINE DE FEU") or has_item("LANTERNE") or has_item("BRIQUET À AMADOU")
    st.write_stream(stream_text("Si vous avez une Graine de Feu de Kalte, une Lanterne ou un Briquet d'Amadou, rendez-vous au :"))
    st.page_link("tomes/tome7/page_49.py", label="49", icon="📄", disabled=not light)
    st.write_stream(stream_text("Si vous ne possédez aucun de ces objets, rendez-vous au :"))
    st.page_link("tomes/tome7/page_277.py", label="277", icon="📄", disabled=light)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
