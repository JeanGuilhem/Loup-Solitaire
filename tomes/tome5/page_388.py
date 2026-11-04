import streamlit as st
from inventory import (
    buy_button,
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

check_inventory(current_page_number=388, book=5)

fr_text = """
Vous suivez l'avenue qui s'enfonce en serpentant dans le quartier
des armuriers d'Ikaresh. Un camelot vend tout un assortiment
d'épées et de poignards qui attirent votre attention : ils sont bien
ouvragés, d'un équilibre parfait et très aiguisés. Une petite
pancarte en bois annonce les prix :
"""

fr_text_2 = """
Ensuite, vous continuez à remonter l'avenue et vous
arrivez au marché des viandes. Des carcasses de bœufs sont
pendues à des crochets, en plein air, et vous n'êtes pas surpris
que les Ikareshis se promènent dans les rues avec des morceaux
de coton dans les narines car l'odeur que dégage la viande est
vraiment insupportable ! Finalement, vous arrivez à un
croisement, mais il n'y a aucun panneau pour indiquer où
mènent ces nouvelles rues.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.markdown(
        "| Arme | Prix |\n|---|---|\n"
        "| Épée | 5 Pièces d'Or |\n| Poignard | 5 Pièces d'Or |\n| Grande Épée | 9 Pièces d'Or |"
    )
    st.write_stream(stream_text("Vous pouvez acheter les armes que vous voulez si vous en avez les moyens."))
    buy_button("ÉPÉE", 5, key="epee")
    buy_button("POIGNARD", 5, key="poignard")
    buy_button("GRANDE ÉPÉE", 9, key="grande_epee")

    st.write(fr_text_2)

    st.write_stream(stream_text("Si vous souhaitez prendre la rue de gauche, rendez-vous au :"))
    st.page_link("tomes/tome5/page_216.py", label="216", icon="📄")
    st.write_stream(stream_text("Si vous préférez prendre la rue de droite, rendez-vous au :"))
    st.page_link("tomes/tome5/page_367.py", label="367", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
