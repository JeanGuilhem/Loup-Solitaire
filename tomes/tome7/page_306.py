import streamlit as st
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

check_inventory(current_page_number=306, book=7)

fr_text = """
Utilisant votre Discipline Magnakaï, vous concentrez votre
attention sur l'étrange plaque triangulaire fixée aux barreaux.
Vous comprenez bientôt son utilité : en trouvant le nombre total
de triangles contenus dans le dessin et en plaçant l'aiguille sur le
chiffre correspondant sur le cadran, vous êtes certain d'ouvrir la
herse en toute sécurité.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Retournez au 11 et étudiez le dessin. Lorsque vous penserez avoir la réponse, rendez-vous au paragraphe qui porte le même numéro."))
    st.page_link("tomes/tome7/page_11.py", label="Revoir le dessin (11)", icon="📄")
    code = st.number_input("Nombre total de triangles (de 1 à 40)", min_value=1, max_value=40, value=None, step=1, key="code_306")
    if code == 13:
        st.page_link("tomes/tome7/page_13.py", label="13", icon="📄")
    elif code is not None:
        st.write("*Ce n'est pas le bon nombre de triangles : recomptez avant d'abaisser le levier.*")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
