import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
    spend_gold,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=27, book=6)

fr_text = """
Eperonnant votre cheval le long de la pente escarpée qui mène
jusqu'au manoir, vous passez au grand galop sous la porte à
tourelles qui en marque l'entrée et vous faites halte près d'une
petite remise dont les murs s'ornent de ferronneries délicatement
ouvragées. Tout à coup, la partie supérieure d'une porte d'écurie
s'ouvre à la volée, et la tête hirsute d'un jeune garçon apparaît
dans l'encadrement. « Voulez un Pass pour Amory ? vous
demande-t-il effrontément. Ce sera 3 Pièces d'Or. » Sur ces mots,
le gamin brandit un rectangle de carton bleu et il tend l'autre
main, paume retournée, en attendant son dû.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez lui demander ce qu'est un Pass, rendez-vous au :"))
    st.page_link("tomes/tome6/page_273.py", label="273", icon="📄")

    st.write_stream(stream_text("Si vous acceptez d'emblée de payer les 3 Pièces d'Or sans discuter, rendez-vous au 304."))
    if st.button("Payer 3 Couronnes", disabled=st.session_state.purse < 3):
        spend_gold(3)
        st.switch_page("tomes/tome6/page_304.py")

    st.write_stream(stream_text("Si vous préférez ignorer la proposition du jeune garçon, reprenez votre route et rendez-vous au :"))
    st.page_link("tomes/tome6/page_146.py", label="146", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
