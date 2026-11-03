import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=246, book=4)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
Vous avancez avec précaution dans l'obscurité en prenant soin de
tâter le sol devant vous à l'aide de votre arme. Vous ignorez alors
que deux yeux observent chacun de vos mouvements. Dans les
ténèbres se cache en effet une créature satanique. Il s'agit d'un
Démoniak, un vampire assoiffé de sang. Son attaque rapide et
silencieuse est indolore, bien que redoutable. Avant de vous être
aperçu que ce parasite s'est accroché dans votre dos, vous avez
déjà perdu 8 points d'ENDURANCE.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-8)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-8)

    st.write_stream(stream_text('Si vous êtes toujours vivant et que vous possédiez le Glaive de Sommer, rendez-vous au :'))
    if has_item("GLAIVE DE SOMMER"):
        st.page_link("tomes/tome4/page_34.py", label="34", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome4/page_34.py", label="34", icon="📄", disabled=True)

    st.write_stream(stream_text('Si vous êtes toujours vivant mais que vous ne disposiez pas de cette arme, rendez-vous au :'))
    st.page_link("tomes/tome4/page_85.py", label="85", icon="📄", disabled=has_item("GLAIVE DE SOMMER"))

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
