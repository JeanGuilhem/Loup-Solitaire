import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=189, book=2)

fr_text = """
« Vous êtes un imposteur ! » s'écrie-t-il en dégainant son arme. Avant
que vous n'ayez pu réagir, la lame de son épée vous écorche le bras et
vous perdez 2 points d'ENDURANCE. L'homme s'est précipité sur
vous ; sous le choc, vous franchissez la porte ouverte à reculons, vous
trébuchez et vous tombez tous deux tête la première au bas des
escaliers, dans un échange de jurons retentissants. Vous vous relevez
ensuite en titubant mais le chevalier, lui, est déjà debout et a ramassé
son épée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)

    st.write_stream(stream_text("Si vous souhaitez le combattre, rendez-vous au :"))
    st.page_link("tomes/tome2/page_162.py", label="162", icon="📄")

    st.write_stream(
        stream_text(
            "Si vous préférez vous enfuir dans la forêt en abandonnant votre cheval, rendez-vous au :"
        )
    )
    st.page_link("tomes/tome2/page_244.py", label="244", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
