import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    has_magnakai,
    show_illustrations,
    show_map,
)
from text import fr_unknown_magnakai
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=24, book=6)

fr_text = """
Il y a bien longtemps que la chapelle a été abandonnée et livrée
aux intempéries du rude climat de la région. Le peu qu'il en reste
est à moitié en ruine, et vous découvrez dans un coin un trou
béant s'ouvrant sur une salle souterraine. Vous distinguez au fond
de grandes flaques d'eau noires et luisantes, et la puanteur
exécrable qui s'en dégage monte jusqu'à vous par vagues, portée
par des courants d'air mugissants. Un gros rat, tapi sur les
restes d'un cadavre en décomposition, vous regarde fixement, la
clarté glauque de l'endroit se réfléchissant dans les deux petites
billes noires de ses yeux. Au fur et à mesure que vous vous
habituez à la pénombre, vous réalisez que cette cave est en fait
remplie de dépouilles : les infortunées victimes du Yamsark !
Soudain, votre attention est attirée par un marteau de guerre en
bronze rutilant, posé sur la poitrine d'un défunt. Dans cette
macabre fosse, l'humus et les moisissures ont tout recouvert,
excepté cette arme qui brille comme si elle était flambant neuve.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez une Corde, vous pouvez essayer de soulever le marteau de guerre grâce à elle ; rendez-vous pour cela au :"))
    st.page_link("tomes/tome6/page_101.py", label="101", icon="📄", disabled=not has_item("CORDE"))

    st.write_stream(stream_text("Si cette arme n'offre aucun intérêt pour vous, sortez de ce funeste endroit pour aller rejoindre Cyrilus ; rendez-vous dans ce cas au :"))
    st.page_link("tomes/tome6/page_338.py", label="338", icon="📄")

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de Nexus, rendez-vous au :"))
    if has_magnakai("Nexus"):
        st.page_link("tomes/tome6/page_276.py", label="276", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome6/page_276.py", label="276", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
