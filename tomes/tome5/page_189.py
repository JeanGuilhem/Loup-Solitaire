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

check_inventory(current_page_number=189, book=5)

fr_text = """
Le Messager tombe en criant, mais il est déjà mort lorsqu'il
heurte les pavés. Vous tirez rapidement son cadavre dans
l'ombre, puis vous revêtez son ample habit et vous rabattez le
capuchon pour cacher votre visage.
Dans la poche de l'habit, vous trouvez un parchemin : le sauf-
conduit indispensable pour pénétrer dans le Grand Palais. Le
cheval du messager, effarouché, s'est enfui, mais le fait que vous
arriviez à pied à la porte du Palais ne semble cependant pas
éveiller de soupçon. Les Gardes examinent le laissez-passer avec
indifférence puis vous autorisent à entrer dans les jardins du
Palais.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome5/page_137.py", label="137", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
