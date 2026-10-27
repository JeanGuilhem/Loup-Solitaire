import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=50, book=2)

fr_text = """
Le moine se penche soudain en avant et dépose une autre Couronne
d'Or sur l'assiette ; la diligence est alors autorisée à poursuivre sa route.
« Peut-être pourrez-vous rendre la pareille un jour, mon fils », dit le
moine en reprenant place sur la banquette avant que vous ayez pu dire
un mot. Vous remarquez alors que le capuchon de sa robe de bure
maintient constamment son visage dans l'ombre : voilà qui est étrange...
Bientôt, la diligence traverse la rivière en crue et le voyage se poursuit.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_249.py", label="249", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
