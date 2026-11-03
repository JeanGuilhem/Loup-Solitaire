import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    kai_rank,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=54, book=4)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Tandis que vous avancez le long du tunnel en pente, vous sentez
un courant d'air froid et humide vous frapper le visage. Les
parois du souterrain sont veinées de minerai étincelant qui
reflète la flamme de votre Torche en de multiples couleurs. En
contemplant ces lueurs dansantes, vous remarquez soudain que
le sol est couvert de petits champignons roses.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï de la Guérison et si vous avez le titre Kaï de Guerrier, rendez-vous au :"))
    if has_kai("La Guérison") and kai_rank() >= 8:
        st.page_link("tomes/tome4/page_4.py", label="4", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome4/page_4.py", label="4", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne maîtrisez pas cette Discipline ou si vous n'avez pas encore atteint ce rang, vous pouvez poursuivre votre chemin sur ce sol envahi de champignons en vous rendant au :"))
    st.page_link("tomes/tome4/page_65.py", label="65", icon="📄", disabled=has_kai("La Guérison") and kai_rank() >= 8)

    st.write_stream(stream_text("Il vous est également possible, si vous le souhaitez, de manger quelques-uns de ces champignons, rendez-vous pour cela au :"))
    st.page_link("tomes/tome4/page_201.py", label="201", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
