import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    remove_from_inventory,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=165, book=4)

fr_text = """
Vous revenez auprès des troubadours au moment où ils
s'apprêtent à servir le dîner. Le bouillon qui fume dans la
marmite vous semble fort appétissant.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    own_meal = st.session_state.get("visibility_own_meal")

    st.write_stream(stream_text('Si vous souhaitez partager leur repas, rendez-vous au :'))
    st.page_link("tomes/tome4/page_319.py", label="319", icon="📄", disabled=bool(own_meal))

    st.write_stream(stream_text("Si vous préférez vous en abstenir, vous devrez manger vos propres provisions ou perdre 3 points d'ENDURANCE. Rendez-vous au 13 pour prendre votre propre Repas en assistant au spectacle donné par les musiciens."))
    if st.button("Prendre votre propre Repas", key="own_meal", disabled=bool(own_meal)):
        if not st.session_state.get("visibility_own_meal"):
            if has_kai("La Chasse"):
                message = "Grâce à votre Discipline Kaï de la Chasse, vous trouvez votre nourriture par vous-même."
            elif remove_from_inventory("REPAS"):
                message = "Vous avez mangé. 1 Repas vous a été retiré."
            elif remove_from_inventory("MOISSON DE LAUMSPUR"):
                change_endurance(3)
                message = "Vous mangez votre Moisson de Laumspur : +3 points d'ENDURANCE."
            else:
                change_endurance(-3)
                message = "Vous n'aviez pas de Repas. Vous perdez 3 points d'ENDURANCE."
            st.session_state["visibility_own_meal"] = message
            st.rerun()
    if own_meal:
        st.write(f"*{own_meal}*")
        st.metric(label="Endurance", value=st.session_state.endurance)
        st.page_link("tomes/tome4/page_13.py", label="13", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
