import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    is_new_page,
    show_illustrations,
    show_map,
)
from text import fr_unknown_magnakai
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=250, book=7)

fr_text = """
Vous serrez dans votre main la Pierre de Sagesse de Herdos et
vous sentez une onde d'énergie vous parcourir tout le corps
(votre total d'ENDURANCE retrouve son niveau initial). Vos
sens frissonnent tandis qu'un regain de force dissipe la fatigue
causée par la terrible épreuve que vous venez de subir. Vous
pouvez maintenant faire face à la situation sur de nouvelles
bases. Une vibration secoue le sol métallique, signe avant-
coureur de la série d'éruptions qui vont détruire Kazan-Oud.
Vous descendez rapidement l'escalier en spirale et courez le long
du tunnel, malgré la chaleur et le bruit qui vous assaillent sans
relâche. Vous arrivez bientôt dans la grande galerie. Là, tout est
plongé dans un désordre indescriptible. Les favoris de Zahda, ses
gardes et ses esclaves courent en tous sens dans une panique
aveugle pour essayer d'échapper à la catastrophe finale.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        st.session_state["herdos_gain"] = st.session_state.total_endurance - st.session_state.endurance
        change_endurance(st.session_state.total_endurance)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=st.session_state.get("herdos_gain", 0))

    st.write_stream(stream_text("Si vous souhaitez essayer de monter l'escalier jusqu'à l'étage où se trouvent les cellules, rendez-vous au :"))
    st.page_link("tomes/tome7/page_300.py", label="300", icon="📄")

    st.write_stream(stream_text("Si vous préférez traverser le vestibule et continuer à suivre le tunnel à ce niveau, rendez-vous au :"))
    st.page_link("tomes/tome7/page_315.py", label="315", icon="📄")

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de l'Exploration ou de l'Intuition, rendez-vous au :"))
    if has_magnakai("Exploration") or has_magnakai("Intuition"):
        st.page_link("tomes/tome7/page_338.py", label="338", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome7/page_338.py", label="338", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
