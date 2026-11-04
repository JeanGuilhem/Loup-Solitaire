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

check_inventory(current_page_number=310, book=5)

fr_text = """
Tandis que vous enjambez les cadavres, vous remarquez une Clé
de Cuivre accrochée au cou d'un homme par une fine chaîne.
Vous prenez cette Clé, que vous glissez dans votre poche, puis
vous descendez rapidement l'escalier au bas duquel brille une
faible lueur. (N'oubliez pas d'inscrire la Clé de Cuivre dans la
case des Objets Spéciaux de votre Feuille d'Aventure.) Un petit
feu, où un poulet est en train de rôtir à la broche, éclaire la salle
de Garde située en bas de la tour. Une gourde d'eau est accrochée
au dossier d'une chaise en fer forgé et, posée sur le sol, juste à
côté, se trouve une épée dont la lame est effilée comme un rasoir.
Vous pouvez prendre l'un de ces deux objets, ou même les deux
si vous le désirez. Dans ce cas, inscrivez-les sur votre Feuille
d'Aventure (notez la gourde dans la case Sac à Dos). Tout à coup,
vous entendez les Drakkars dévaler à grand bruit l'escalier de la
tour. Ils ne tarderont pas à vous rejoindre et vous devez prendre
une décision rapide.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        add_to_inventory("CLÉ DE CUIVRE")
    st.success("La Clé de Cuivre a été ajoutée à vos Objets Spéciaux.")

    pickup_button("GOURDE", key="gourde", label="Prendre la Gourde")
    pickup_button("ÉPÉE", key="epee", label="Prendre l'Épée")

    st.write_stream(stream_text('Si vous désirez sortir de la tour par la porte donnant au nord, rendez-vous au :'))
    st.page_link("tomes/tome5/page_246.py", label="246", icon="📄")

    st.write_stream(stream_text('Si vous préférez affronter les Drakkars, préparez-vous à combattre et rendez-vous au :'))
    st.page_link("tomes/tome5/page_231.py", label="231", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
