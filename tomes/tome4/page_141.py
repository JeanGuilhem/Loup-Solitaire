import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, handle_repas, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=141, book=4)

fr_text = """
Vous n'êtes pas allé bien loin, lorsque soudain éclate un orage qui
déverse sur vos têtes une pluie torrentielle. En quelques minutes,
la route sèche et poussiéreuse se transforme en marécage. Il vous
sera impossible d'établir votre campement sous cette pluie
battante et vous décidez donc de poursuivre votre chemin toute
la nuit en espérant que l'orage cessera bientôt. Au cours de cette
nuit passée à cheval, il vous faudra prendre un Repas, sinon vous
perdrez 3 points d'ENDURANCE. Au matin, la pluie a cessé,
mais cette épreuve vous a épuisés, vous et vos hommes.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    handle_repas()

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_253.py", label="253", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
