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

check_inventory(current_page_number=334, book=7)

fr_text = """
« Bien ! retentit la voix de Zahda lorsque vous pénétrez dans le
passage. Les lâches d'Elzian ont enfin envoyé un guerrier digne
de mon labyrinthe. » Ces mots évoquent en vous l'image du
Seigneur Zahda, assis sur son trône en or avec, au-dessus, l'objet
de votre quête : la Pierre de Sagesse de Herdos. Cette image
renforce votre résolution et vous êtes plus que jamais décidé à
triompher du labyrinthe maudit. Si vous parvenez à retrouver
votre chemin vers la salle du trône du Zahda, le succès de votre
quête sera à la portée de votre main. Vous continuez à avancer
dans le passage, l'esprit préoccupé par les différents problèmes et
les nombreux dangers que vous allez devoir affronter. Le passage
vire brusquement et vous voilà confronté à un de ces dangers.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_100.py", label="100", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
