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

check_inventory(current_page_number=6, book=7)

fr_text = """
« Bien ! retentit la voix de Zahda au moment où vous atteignez
l'autre côté du gouffre. Vous êtes très agile - mais il reste à voir si
votre intelligence est à la hauteur de vos muscles ! Sur ce point,
nous serons bientôt fixés... Ah ! Ah ! Ah ! » La voix déclenche
soudain l'apparition du Seigneur Zahda dans votre esprit. Il est
assis sur un grand trône en or massif, et l'objet de votre quête, la
Pierre de la Sagesse de Herdos, est suspendue dans les airs au-dessus de lui. C'est alors que vous trouvez subitement le moyen
de sortir de ce redoutable dédale : si vous arrivez à retourner
dans la Salle du Trône de Zahda, le succès de votre mission sera
assuré. Mais, avant d'y arriver, il vous reste de nombreux périls à
affronter. Justement, le premier vous attend au détour du
souterrain.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome7/page_100.py", label="100", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
