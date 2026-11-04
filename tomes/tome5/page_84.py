import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=84, book=5)

fr_text = """
Vous armant de courage, vous plongez dans l'eau putride et vous
commencez à nager en vous efforçant d'écarter l'écume grasse et
nauséabonde qui s'infiltre dans votre bouche et votre nez. A
moitié suffoqué par la puanteur, vous parvenez à traverser le
canal pour vous rendre dans le tunnel d'en face et vous vous
hissez péniblement sur l'étroit trottoir qui longe l'eau. Vous
commencez à trembler, mais ce n'est pas à cause de cet horrible
bain forcé : vous vous sentez fébrile ; votre épaule - qui avait été
blessée lorsque la trappe vous était retombée dessus - vous
élance douloureusement et votre bras ne réagit plus. Vous êtes
saisi d'une indicible angoisse lorsque vous réalisez ce qui vous
arrive.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_81.py", label="81", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
