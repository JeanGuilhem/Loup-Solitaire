import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=100, book=5)

fr_text = """
La porte de marbre s'ouvre sur une pièce sombre où flotte une
odeur de parchemin moisi. Sur des étagères en pierre sont
soigneusement rangés de grands livres reliés en cuir et portant
au dos de délicates arabesques peintes à l'or fin. D'après les dates
et les inscriptions que vous pouvez lire, cette collection de livres
constitue l'inventaire de tous les trésors du Grand Palais, dont
certains remontent à plusieurs siècles. Chaque étagère de la
bibliothèque est surchargée de livres, excepté une, où une petite
Clé de Cuivre et un Prisme sont disposés sur un napperon de soie
pourpre.
"""

fr_text_2 = """
Mis à part la porte de marbre par
laquelle vous êtes entré, il n'y a pas d'autre porte donnant accès à
la bibliothèque. Après vous être assuré qu'il n'y a plus rien
d'intéressant dans cette pièce, vous refermez la porte et vous
reprenez votre chemin le long du couloir. Mais, alors que vous
arrivez à un croisement, vous voyez une patrouille de Gardes
commencer à monter l'escalier. Sans hésiter, vous vous élancez
vers la porte qui donne à l'est pour éviter d'être repéré.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez prendre l'un ou l'autre de ces objets, ou même les deux, n'oubliez pas de les inscrire sur votre Feuille d'Aventure dans la case des Objets Spéciaux et mettez-les par conséquent dans votre poche."))
    pickup_button("CLÉ DE CUIVRE", key="cle_cuivre", label="Prendre la Clé de Cuivre")
    pickup_button("PRISME", key="prisme", label="Prendre le Prisme")
    st.write(fr_text_2)
    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_57.py", label="57", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
