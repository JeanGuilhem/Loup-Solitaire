import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=125, book=2)

fr_text = """
Vous vous précipitez par la porte latérale de la taverne et vous courez
tout au long d'une ruelle qui aboutit à la place principale. Vous
apercevez, au-delà de la foule qui se presse en tous sens, de nombreux
bateaux amarrés aux quais. Les brigands vous suivent de près et il vous
faut agir vite, sinon ils vous tueront comme ils ont sans doute tué
Ronan. Vous défaites alors l'amarre d'un canot puis vous sautez du quai
et vous atterrissez lourdement dans l'embarcation, en fracassant dans
votre chute le petit siège de bois aménagé au milieu. Vous trouvez une
rame au fond du canot et vous pagayez ferme pour rejoindre le Sceptre
Vert qui mouille à 300 mètres de là.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_300.py", label="300", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
