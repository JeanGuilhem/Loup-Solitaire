import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_weapon,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=244, book=3)

fr_no_weapon = "Vous n'avez pas d'arme."

fr_text = """
Vous vous approchez de l'autel à pas prudents. La Statue est
froide et apparemment inanimée, mais vous sentez que
quelqu'un, ou quelque chose, est enfermé à l'intérieur. Vous avez
même l'impression d'entendre des cris désespérés qui implorent
la liberté.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez fracasser la Statue à l'aide d'une arme, rendez-vous au :"))
    if has_weapon():
        st.page_link("tomes/tome3/page_150.py", label="150", icon="📄")
    else:
        st.write_stream(stream_text(fr_no_weapon))
        st.page_link("tomes/tome3/page_150.py", label="150", icon="📄", disabled=True)
    st.write_stream(
        stream_text(
            "Si vous n'avez pas d'arme ou si vous préférez quitter le temple à l'instant et vous diriger vers "
            "l'arcade située au nord, rendez-vous au :"
        )
    )
    st.page_link("tomes/tome3/page_306.py", label="306", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
