import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    pickup_gold,
    show_illustrations,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=302, book=2)

fr_text = """
Vous enjambez le corps puis vous montez l'escalier pour fouiller la
tour. Au cours d'une perquisition en règle, vous trouvez les objets
suivants : Masse d'Armes, Glaive, Bâton, Potion de Guérison (une dose
qui vous redonne 3 points d'ENDURANCE si vous la buvez après un
combat), une quantité de nourriture équivalant à 3 Repas, un Sac à Dos,
12 Pièces d'Or. Prenez ce dont vous avez besoin, modifiez en
conséquence votre Feuille d'Aventure et hâtez-vous de quitter la tour de
peur que quelqu'un ne découvre votre présence. La forêt qu'il vous faut
traverser est très dense et vous allez devoir abandonner votre cheval
pour continuer votre chemin à pied.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write("Prenez ce dont vous avez besoin :")
    pickup_button("MASSE D'ARMES", key="masse", label="Prendre la Masse d'Armes")
    pickup_button("GLAIVE", key="glaive", label="Prendre le Glaive")
    pickup_button("BÂTON", key="baton", label="Prendre le Bâton")
    pickup_button("PETITE POTION DE GUÉRISON", key="potion", label="Prendre la Potion de Guérison (3 points)")
    pickup_button("REPAS", key="repas_1", label="Prendre un Repas")
    pickup_button("REPAS", key="repas_2", label="Prendre un deuxième Repas")
    pickup_button("REPAS", key="repas_3", label="Prendre un troisième Repas")
    pickup_button("SAC À DOS", key="sac", label="Prendre le Sac à Dos")
    pickup_gold(12, key="gold")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_244.py", label="244", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
