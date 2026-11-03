import streamlit as st
from combat import combat
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

check_inventory(current_page_number=284, book=4)

fr_text = """
Vous ordonnez à vos hommes de se déployer sur une seule ligne
et d'avancer vers les brigands. Lorsqu'ils ne sont plus qu'à une
centaine de mètres de l'ennemi, vous donnez le signal de
l'attaque. Le vent vous cingle le visage en vous portant l'écho des
cris de guerre qui retentissent dans la plaine. Les adversaires, se
précipitant à la rencontre les uns des autres, se heurtent avec une
formidable violence. Vous êtes vous-même à demi assommé par
le choc lorsque votre cheval vient frapper de plein fouet le flanc
d'une monture ennemie. L'animal et son cavalier sont projetés à
terre. Quant à vous, vous vacillez sur votre selle, et vous ne
parvenez pas à éviter un coup de lance qui ouvre une blessure
dans votre cuisse. Vous perdez aussitôt 3 points d'ENDURANCE
avant de vous tourner vers votre agresseur pour le combattre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-3)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-3)
    outcome = combat([("GUERRIER PILLARD", 16, 25)], flee_after=0)
    if outcome == "fled":
        st.write_stream(stream_text('Vous avez le droit de prendre la fuite à tout moment en vous rendant au :'))
        st.page_link("tomes/tome4/page_89.py", label="89", icon="📄")
    elif outcome == "win":
        st.write_stream(stream_text('Si vous remportez la victoire, rendez-vous au :'))
        st.page_link("tomes/tome4/page_7.py", label="7", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
