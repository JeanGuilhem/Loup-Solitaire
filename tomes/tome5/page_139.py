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

check_inventory(current_page_number=139, book=5)

fr_text = """
Gêné par la véritable couverture d'insectes qui grouillent sur
votre peau, vous ne voyez même pas le poteau en fer rouillé qui
sort de l'eau. Mais lorsque vous perdez brusquement pied, vous
essayez instinctivement de vous y agripper. Hélas ! Comme tout
ce qui se trouve dans ces égouts, il est recouvert d'une vase
visqueuse aussi glissante que la glace de Kalte elle-même.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_94.py", label="94", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
