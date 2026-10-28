import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=119, book=3)

fr_text = """
De gros morceaux de glace se détachent du pont et une large
fissure apparaît. Vous parvenez malgré tout à maintenir le
traîneau sur sa trajectoire et vous atteignez le bord opposé de la
gorge. Malheureusement, vous avez tôt fait de constater que l'un
des patins est cassé et irréparable. Vous êtes donc contraint
d'abandonner le traîneau et de continuer à pied. Il contient
toujours, cependant, du matériel fort utile. Vous pouvez
emporter une partie de ce matériel en le rangeant dans votre Sac
à Dos (mais souvenez-vous que vous n'avez pas le droit de
transporter plus de 8 objets).
"""

fr_text_suite = """
Fenor, Irian et Dyce se hâtent de vous rejoindre, mais lorsqu'ils
sont parvenus au milieu du pont, une catastrophe se produit.
Dyce, en effet, se prend le pied dans une fissure et tombe.
Horrifié, vous le voyez glisser dans le vide ; au dernier moment,
cependant, il parvient à s'accrocher au bord du pont et reste ainsi
suspendu, les doigts crispés sur la glace. « Au secours ! Aidez-moi ! »
hurle-t-il, tandis que ses mains glissent peu à peu.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Voici le choix qui vous est offert :"))
    st.write("**Des vivres équivalents à 5 Repas** (chaque Repas compte pour un objet) :")
    cols = st.columns(5)
    for i, col in enumerate(cols, start=1):
        with col:
            pickup_button("REPAS", key=f"repas_{i}", label="Prendre 1 Repas")
    pickup_button("COUVERTURE DE FOURRURE", key="couverture", label="Prendre les Couvertures de Fourrure (2 objets)")
    pickup_button("TENTE", key="tente", label="Prendre la Tente (3 objets)")
    pickup_button("CORDE", key="corde", label="Prendre la Corde (2 objets)")
    st.write(fr_text_suite)
    st.write_stream(stream_text("Si vous souhaitez venir en aide à Dyce, rendez-vous au :"))
    st.page_link("tomes/tome3/page_19.py", label="19", icon="📄")
    st.write_stream(stream_text("Si vous estimez qu'il est trop dangereux de lui porter secours, rendez-vous au :"))
    st.page_link("tomes/tome3/page_257.py", label="257", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
