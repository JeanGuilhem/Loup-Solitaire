import streamlit as st
from combat import combat
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

check_inventory(current_page_number=47, book=6)

fr_text = """
« Comment osez-vous me faire perdre mon temps avec de telles
sottises ! s'écrie le négociant avec une grimace de mépris.
Débarrassez-moi de cet importun ! » Aussitôt, ses gardes du corps
accourent, le poing levé, prêts à passer à l'attaque. Vous
remarquez que l'un d'eux porte une épaisse lanière hérissée de
pointes d'acier et, à en juger par son expression, il est
impatient de s'en servir. En raison de la rapidité de l'attaque de
vos adversaires, vous ne pouvez pas utiliser votre arc.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # l'Arc ne compte jamais comme arme de corps à corps : combat() en tient compte
    outcome = combat([("GARDES DU CORPS", 18, 34)])
    if outcome == "win":
        st.write_stream(stream_text("Si vous sortez vainqueur de l'affrontement, rendez-vous au :"))
        st.page_link("tomes/tome6/page_263.py", label="263", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
