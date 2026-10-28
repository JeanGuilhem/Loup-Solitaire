import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=74, book=3)

fr_text = """
Les murs de pierre du couloir sont couverts d'étranges sculptures
qui projettent de grandes ombres. Vous vous servez de ces
ombres pour vous y dissimuler avec l'agilité qui vous est
coutumière. Le Barbare des Glaces avance lentement dans votre
direction, les muscles tendus, la démarche hésitante. Vous avez
alors la chair de poule en remarquant pour la première fois que
ses yeux blancs sont dépourvus de pupilles. Retenant votre
souffle, vous faites des prières pour qu'il ne vous ait pas vu.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    roll = hazard_roll()
    if roll is not None and roll <= 4:
        st.write_stream(stream_text("Vous avez tiré un chiffre entre 0 et 4, rendez-vous au :"))
        st.page_link("tomes/tome3/page_48.py", label="48", icon="📄")
    elif roll is not None:
        st.write_stream(stream_text("Vous avez tiré un chiffre entre 5 et 9, rendez-vous au :"))
        st.page_link("tomes/tome3/page_287.py", label="287", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
