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

check_inventory(current_page_number=262, book=7)

fr_text = """
La porte est verrouillée, mais le mécanisme est si rouillé qu'il
cède à la première pression. Vous pénétrez dans une pièce où
s'entassent pêle-mêle des barriques, des caisses poussiéreuses et
des bouteilles de vin éventé. Sur un banc en bois humide, vous
trouvez un sabre et un bouclier rond. (Si vous souhaitez prendre
un de ces objets, n'oubliez pas de le noter sur votre Feuille
d'Aventure ; le bouclier est un Objet Spécial qui ajoute 2 points à
votre total d'HABILETÉ au cours d'un combat.)
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("SABRE", key="banc", label="Prendre le Sabre")
    pickup_button("BOUCLIER", key="banc", label="Prendre le Bouclier (Objet Spécial, +2 HABILETÉ)")

    st.write_stream(stream_text("Si vous voulez fouiller la pièce plus attentivement, rendez-vous au :"))
    st.page_link("tomes/tome7/page_73.py", label="73", icon="📄")

    st.write_stream(stream_text("Si vous préférez quitter la pièce et explorer l'escalier, rendez-vous au :"))
    st.page_link("tomes/tome7/page_11.py", label="11", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
