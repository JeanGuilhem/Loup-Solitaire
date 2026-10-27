import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies, ls_death

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=126, book=2)

fr_text = """
L'homme tire sur la corde d'une clochette dissimulée aux regards et,
soudain, quatre gardes armés font irruption dans la pièce. « Ces
documents sont des faux. Vous êtes sans aucun doute un espion, peut-
être même pire. Quoi qu'il en soit, vous n'allez pas tarder à apprendre
ce que nous faisons des criminels dans votre genre, à Port Bax.
Emmenez-le ! » Avant que vous n'ayez pu fournir la moindre
explication, les gardes vous saisissent et vous emmènent à la prison de
la ville. Tout votre équipement est confisqué, y compris les Objets
Spéciaux et les armes, et on vous jette dans une cellule remplie de
canailles à l'aspect patibulaire. Vous remarquez aussitôt que plusieurs
de ces fripons portent au poignet gauche un tatouage qui représente un
serpent : c'est le signe de Vonatar le Traître. Et lorsque, enfin, les
gardes découvrent votre véritable identité en examinant votre
équipement, il est trop tard : les séides du sorcier vous ont déjà
étranglé. Votre mission s'achève donc tragiquement en même temps
que votre vie dans un cul-de-basse-fosse de Port Bax.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    show_illustrations()
    ls_death()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
