import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    is_new_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=240, book=2)

fr_text = """
Après trois jours en mer durant lesquels il ne s'est rien passé, vous
commencez à trouver le temps long. Si vous maîtrisez la Discipline Kaï
de la Guérison, vous pouvez récupérer tous les points d'ENDURANCE
que vous avez éventuellement perdus depuis le début de votre aventure.
Vous retrouverez dans ce cas le total d'ENDURANCE dont vous
disposiez au départ. Si vous ne maîtrisez pas cette Discipline, vous ne
récupérerez que la moitié des points d'ENDURANCE perdus
(arrondissez au chiffre supérieur si le nombre à diviser par deux est
impair). Dans l'après-midi du quatrième jour, vous êtes sur le pont du
navire en train de bavarder avec un homme d'équipage lorsqu'une odeur
de brûlé se dégage soudain d'une des cales.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        lost = st.session_state.total_endurance - st.session_state.endurance
        healed = lost if has_kai("La Guérison") else (lost + 1) // 2
        st.session_state.visibility_healed = healed
        change_endurance(healed)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=st.session_state.get("visibility_healed", 0))

    st.write_stream(stream_text('Si vous souhaitez descendre dans cette cale, rendez-vous au :'))
    st.page_link("tomes/tome2/page_29.py", label="29", icon="📄")

    st.write_stream(stream_text("Si vous pensez qu'il est préférable de crier « Au feu ! », rendez-vous au :"))
    st.page_link("tomes/tome2/page_236.py", label="236", icon="📄")

    st.write_stream(stream_text("Enfin, si vous décidez plutôt d'aller prévenir le capitaine, rendez-vous au :"))
    st.page_link("tomes/tome2/page_101.py", label="101", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
