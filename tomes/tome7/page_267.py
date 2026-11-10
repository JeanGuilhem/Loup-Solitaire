import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=267, book=7)

fr_text = """
Vous examinez le trône étincelant et l'estrade en fer noir sur
laquelle il repose. Vous découvrez un pentacle profondément
gravé dans l'or et vous en suivez le contour avec le doigt. Vous
entendez alors, couvrant le vacarme de la destruction, un bruit
ressemblant au tintement de milliers de clochettes. Dans les
ténèbres au-dessus du trône, vous apercevez une lueur qui
descend lentement vers vous et, peu après, une grande partie de
l'estrade baigne dans une scintillante colonne de lumière bleue.
Vous levez le bras et, au moment où vous serrez la Pierre de
Sagesse de Herdos, une onde d'énergie vous parcourt le corps
(votre total d'ENDURANCE retrouve son niveau initial). Vos
sens frémissent et un regain de force dissipe la fatigue de votre
terrible épreuve. Vous pouvez maintenant faire face à la situation
à partir de nouvelles bases. La colonne de lumière est un
transporteur magique, un rayon où la gravité est presque réduite
à zéro. En pénétrant dans cette colonne de lumière, vous allez
être emporté à la surface de Kazan-Oud. Sans hésitation, vous
rangez la Pierre de la Sagesse dans votre poche et vous entrez
dans le rayon magique.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(st.session_state.total_endurance - st.session_state.endurance)
    st.metric(label="Endurance", value=st.session_state.endurance)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_200.py", label="200", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
