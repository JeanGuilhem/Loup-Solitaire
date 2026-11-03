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
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=327, book=4)

fr_text = """
Vous tirez l'épée de votre ceinture et vous l'offrez au capitaine.
Une expression de surprise et de contentement apparaît sur son
visage tandis qu'il examine la lame. « Je n'espérais plus jamais
revoir ma fidèle épée, dit-il. C'est un bon présage pour la bataille
qui nous attend. » Après vous avoir remercié, le capitaine remet
son épée dans son fourreau qui, jusqu'alors, pendait vide à son
côté.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        remove_from_inventory("ÉPÉE DE GAYAL")
    st.write("*Vous avez rendu l'Épée au capitaine Gayal.*")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_289.py", label="289", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
