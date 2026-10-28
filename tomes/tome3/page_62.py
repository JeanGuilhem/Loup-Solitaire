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
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=62, book=3)

fr_text = """
Tandis que la lumière du jour décline peu à peu, le blizzard se
met à souffler sur la banquise en faisant claquer sans relâche la
toile de votre tente. Ce bruit lancinant s'ajoutant à la douleur de
vos doigts et de vos orteils vous met les nerfs à vif et vous
commencez à souhaiter n'avoir jamais mis les pieds dans cet
enfer glacé. Puis, au beau milieu de la nuit, le vent déchire le
bord de la toile et la force de la rafale disperse vos vivres et votre
équipement. Vous êtes contraint de passer le reste de la nuit à
plat ventre, appuyé sur les coudes, vos doigts gelés crispés sur la
toile pour l'empêcher de s'envoler. Une gadoue à moitié gelée se
glisse sous vos Couvertures de Fourrure et lorsque l'aube se lève,
vos vêtements, gelés à leur tour, sont devenus tout raides. Vous
perdez 3 points d'ENDURANCE.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-3)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-3)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_167.py", label="167", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
