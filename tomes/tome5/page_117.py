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

check_inventory(current_page_number=117, book=5)

fr_text = """
L'allée tortueuse aboutit dans un petit jardin, bordé sur trois
côtés par des maisons aux toits en forme de coupole. Toutes ces
demeures possèdent des portes et des fenêtres ornées de grilles
en fer forgé ainsi que de grands balcons au premier étage. Vous
grimpez à un solide treillis en bois qui monte jusqu'à un de ces
balcons mais, au moment où vous allez enjamber la balustrade,
les hommes de Maouk font irruption sur la place. De nombreux
soldats sont armés de lourdes arbalètes en bronze. « Rendez-vous,
Loup Solitaire, crie Maouk, ou mes hommes vont vous
clouer au mur ! » La situation est désespérée car, à cette
distance, les Sharnazims ne peuvent pas vous manquer.
Maudissant votre infortune, vous vous laissez tomber par terre,
aux pieds de Maouk. « Vous êtes courageux, Seigneur Kaï, dit-il
férocement, mais votre bravoure ne saurait vous sauver
maintenant ! »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_176.py", label="176", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
