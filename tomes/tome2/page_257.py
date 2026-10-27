import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=257, book=2)

fr_text = """
Cette rue aux pavés jonchés d'ordures est bordée de taudis, de masures
aux façades moisies et de boutiques délabrées. Les quelques passants
que vous croisez ont la mine sombre, les traits tirés et les yeux hagards.
Ils avancent dans le noir en traînant les pieds, le dos voûté sous la pluie
qui tombe à verse et le regard fixé sur le pavé. Vous arrivez bientôt à
un croisement ; là, la rue de la Hache s'oriente vers le nord et une autre
rue part vers l'est.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez aller vers le nord et prendre la rue du Chevalier Noir, rendez-vous au :'))
    st.page_link("tomes/tome2/page_335.py", label="335", icon="📄")

    st.write_stream(stream_text("Si vous préférez prendre la direction de l'est en empruntant la rue du Sage, rendez-vous au :"))
    st.page_link("tomes/tome2/page_181.py", label="181", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
