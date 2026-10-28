import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=326, book=3)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Au bout d'un moment d'intense concentration, l'image de la
serrure se forme peu à peu dans votre esprit. Cette serrure est
protégée par un enchantement, mais votre Discipline Kaï,
soutenue par votre farouche détermination, finit par l'emporter.
Vous entendez en effet un cliquetis indiquant que vos efforts ont
été couronnés de succès. Vous avez dû, cependant, dépenser une
énergie considérable et vous perdez 1 point d'ENDURANCE.
Quelques instants plus tard, le lourd couvercle de pierre s'ouvre
tout seul et silencieusement, laissant apparaître un magnifique
Casque d'Argent.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-1)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-1)
    st.write_stream(stream_text("Si vous souhaitez vous coiffer de ce Casque, rendez-vous au :"))
    st.page_link("tomes/tome3/page_308.py", label="308", icon="📄")
    st.write_stream(stream_text("Si vous préférez le laisser là où il est, vous pouvez poursuivre votre chemin en montant l'escalier ; rendez-vous pour cela au :"))
    st.page_link("tomes/tome3/page_323.py", label="323", icon="📄")
    st.write_stream(stream_text("Enfin, si vous maîtrisez la Discipline Kaï du Sixième Sens, rendez-vous au :"))
    if has_kai("Le Sixième Sens"):
        st.page_link("tomes/tome3/page_127.py", label="127", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome3/page_127.py", label="127", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
