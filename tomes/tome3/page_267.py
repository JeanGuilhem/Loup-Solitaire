import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
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

check_inventory(current_page_number=267, book=3)

fr_text = """
Loi-Kymar montre soudain la poche dans laquelle vous avez
rangé la Pierre Rayonnante. « Pourquoi donc conservez-vous une
pierre maudite, Seigneur Kaï ? Ignorez-vous les dangers qu'elle
présente ?» Vous retirez aussitôt la Pierre de votre poche et vous
la montrez au magicien. « Argh ! s'écrie-t-il comme si le simple
fait de la regarder lui causait une intense douleur. Jetez-la au
plus vite, avant que nous ne succombions au terrible mal. C'est
une pierre maudite des Anciens, elle ne peut apporter que
maladie et mort à quiconque d'entre les mortels convoite sa
beauté. » A contrecœur, vous obéissez à Loi-Kymar et vous vous
débarrassez de la Pierre. Rayez-la de votre Feuille d'Aventure.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page() and has_item("PIERRE RAYONNANTE"):
        remove_from_inventory("PIERRE RAYONNANTE")
    st.caption("La Pierre Rayonnante a été rayée de votre Feuille d'Aventure.")

    st.write_stream(stream_text('Rendez-vous ensuite au :'))
    st.page_link("tomes/tome3/page_44.py", label="44", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
