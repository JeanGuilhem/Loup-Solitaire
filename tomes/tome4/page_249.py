import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=249, book=4)

fr_text = """
Vous vous précipitez vers la barricade et vous arrachez un arc des
mains d'un soldat mort. Vous avez repéré le chef de la cavalerie
ennemie. C'est un Guerrier de haute taille, à la peau sombre et au
nez droit et fin. Il est en train de rassembler ses hommes au pied
de la tour de guet. Il vous faut absolument le tuer avant qu'il n'ait
pu regrouper ses troupes sinon, le capitaine Gayal et ses soldats
seront impitoyablement massacrés. Vous encochez une flèche et
vous bandez votre arc. La corde tendue s'enfonce dans la chair de
vos doigts, tandis que vous visez.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous possédez la Discipline Kaï de la Maîtrise des Armes (quelle que soit l'arme dont il s'agit) vous ajouterez 2 au chiffre que vous aurez tiré."))
    roll = hazard_roll()
    if roll is not None:
        total = roll + (2 if has_kai("La Maîtrise des armes") else 0)
        if has_kai("La Maîtrise des armes"):
            st.write(f"*Maîtrise des Armes : +2, soit un total de {total}.*")
        if total <= 3:
            st.write_stream(stream_text('Si vous obtenez un total de 0 à 3, rendez-vous au :'))
            st.page_link("tomes/tome4/page_153.py", label="153", icon="📄")
        elif total <= 7:
            st.write_stream(stream_text('De 4 à 7, rendez-vous au :'))
            st.page_link("tomes/tome4/page_323.py", label="323", icon="📄")
        else:
            st.write_stream(stream_text('De 8 à 11, rendez-vous au :'))
            st.page_link("tomes/tome4/page_39.py", label="39", icon="📄")


    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
