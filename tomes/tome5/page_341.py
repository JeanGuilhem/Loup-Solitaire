import streamlit as st
from inventory import (
    add_to_inventory,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=341, book=5)

fr_text = """
Tandis que vous enjambez les corps inanimés, vous remarquez
qu'un des Gardes possède une Clé de Cuivre accrochée autour du
cou par une chaîne. Vous prenez cette Clé, que vous glissez dans
votre poche (n'oubliez pas d'inscrire cette nouvelle acquisition
dans la case des Objets Spéciaux de votre Feuille d'Aventure).
Vous dévalez ensuite l'escalier, mais une fois arrivé au pied de la
tour, vous apercevez une armée de Drakkars et de Gardes du
Palais en train de se précipiter sur le pont ; une mort certaine
vous y attend si vous vous y engagez à votre tour. Vous décidez
donc de continuer à descendre les marches vers le sous-sol. Là,
une faible lueur éclaire une salle de Garde. Au dossier d'une
chaise en fer forgé sont accrochées une épée et une gourde d'eau.
Vous pouvez prendre un de ces objets, ou même les deux, si vous
le désirez. Dans ce cas, notez-les sur votre Feuille d'Aventure
dans la case Sac à Dos). Soudain, vous entendez vos adversaires
se ruer dans l'escalier ; dans une minute, ils vous auront rejoint !
Toutefois, une lourde porte en bois encastrée dans le mur nord
vous offre encore une chance de vous échapper.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        add_to_inventory("CLÉ DE CUIVRE")
    st.success("La Clé de Cuivre a été ajoutée à vos Objets Spéciaux.")

    pickup_button("ÉPÉE", key="epee", label="Prendre l'Épée")
    pickup_button("GOURDE", key="gourde", label="Prendre la Gourde")

    st.write_stream(stream_text('Si vous souhaitez fuir par cette porte, rendez-vous au :'))
    st.page_link("tomes/tome5/page_246.py", label="246", icon="📄")

    st.write_stream(stream_text('Si vous préférez vous préparer à combattre vos poursuivants, rendez-vous au :'))
    st.page_link("tomes/tome5/page_231.py", label="231", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
