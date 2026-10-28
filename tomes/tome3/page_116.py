import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    remove_from_inventory,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=116, book=3)

fr_text = """
Vous versez la potion sur votre peau irritée et meurtrie, et vous
ressentez immédiatement les effets bienfaisants du liquide. La
douleur disparaît peu à peu et l'enflure se résorbe. La Pierre
Rayonnante est une roche maudite qui émet une énergie mortelle
à laquelle tous les êtres vivants sont sensibles. Si vous n'aviez pas
eu la Potion de Laumspur en votre possession, la pierre
maléfique vous aurait certainement tué. Vous jetez la Pierre
Rayonnante ainsi que la fiole à présent vide, puis vous mettez
votre Feuille d'Aventure à jour.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        remove_from_inventory("PIERRE RAYONNANTE")
        remove_from_inventory("POTION ROUGE DE LAUMSPUR")
    st.info("La Pierre Rayonnante et la Potion rouge de Laumspur ont été retirées de vos Objets Spéciaux.")
    st.write_stream(stream_text("Vous poursuivrez ensuite votre chemin le long du couloir en vous rendant au :"))
    st.page_link("tomes/tome3/page_97.py", label="97", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
