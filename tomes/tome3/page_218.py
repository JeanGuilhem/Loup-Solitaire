import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=218, book=3)

fr_text = """
La boîte en os contient un magnifique Diamant. Même dans la
pénombre des lieux, ses multiples facettes étincellent. Dans le
royaume du Sommerlund, une pierre de cette taille et de cette
qualité vaudrait des milliers de Couronnes d'Or.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Si vous souhaitez conserver ce Diamant, glissez-le dans votre poche et inscrivez-le dans vos "
            "Objets Spéciaux."
        )
    )
    if not has_item("DIAMANT"):
        pickup_button("DIAMANT", key="diamant", label="Prendre le Diamant")
    st.write_stream(stream_text("Vous pouvez à présent examiner la porte de la forteresse en vous rendant au :"))
    st.page_link("tomes/tome3/page_52.py", label="52", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
