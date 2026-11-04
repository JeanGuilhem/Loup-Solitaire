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

check_inventory(current_page_number=350, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Tandis que vous vous élancez à découvert, une autre décharge
d'énergie jaillit du poing du Seigneur des Ténèbres. L'éclair
explose à la base du pilier qui s'effondre, suivi bientôt par le
plafond qui s'écroule dans un énorme grondement. L'onde de
choc vous projette au sol, vous aplatissant violemment contre les
dalles de marbre glacé. Vous perdez 3 points d'ENDURANCE.
Vous percevez encore le rire de Haakon qui s'élève au-dessus du
vacarme que font les blocs de pierre en tombant. Son rire se fait
de plus en plus aigu et vous ressentez simultanément une
horrible douleur à la tête.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-3)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-3)

    st.write_stream(stream_text('Si vous maîtrisez la Discipline Kaï du Bouclier Psychique, rendez-vous au :'))
    if has_kai("Bouclier psychique"):
        st.page_link("tomes/tome5/page_253.py", label="253", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_253.py", label="253", icon="📄", disabled=True)

    st.write_stream(stream_text('Si vous ne maîtrisez pas cette Discipline, rendez-vous au :'))
    if has_kai("Bouclier psychique"):
        st.page_link("tomes/tome5/page_369.py", label="369", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome5/page_369.py", label="369", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
