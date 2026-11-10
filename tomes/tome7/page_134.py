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

check_inventory(current_page_number=134, book=7)

fr_text = """
Vous réussissez à assimiler le pouvoir dirigé contre vous et à
renforcer d'autant l'effet de votre Foudroiement Psychique sur la
monstrueuse entité. La répercussion du flux provoque une
réaction explosive et irréversible ; soudain, un éclair aveuglant
jaillit, et la main se désintègre en menus morceaux. Vos tempes
battent douloureusement à l'issue de cette pénible épreuve
psychique (vous perdez 4 points d'ENDURANCE), mais vous
poussez un soupir de soulagement en voyant s'achever ce combat
à votre avantage.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-4)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-4)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_334.py", label="334", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
