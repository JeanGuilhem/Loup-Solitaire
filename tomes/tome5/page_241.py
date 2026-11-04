import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=241, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Une fois hors de la grotte, Banedon et vous partez en direction
d'Ikaresh sans perdre une minute. Lorsque vous arrivez près des
faubourgs de la ville, vous passez devant une petite hutte ronde
où une chèvre est attachée à une mangeoire près de la porte. Un
homme apparaît dans l'encadrement et vous souhaite la
bienvenue. Il porte sa main à son front en signe d'amitié, puis
vous invite à entrer dans son humble demeure.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez accepter son invitation, rendez-vous au :"))
    st.page_link("tomes/tome5/page_225.py", label="225", icon="📄")

    st.write_stream(stream_text("Si vous préférez décliner son offre et poursuivre votre route vers Ikaresh, rendez-vous au :"))
    st.page_link("tomes/tome5/page_272.py", label="272", icon="📄")

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï du Sixième Sens, rendez-vous au :"))
    if has_kai("Le Sixième Sens"):
        st.page_link("tomes/tome5/page_365.py", label="365", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_365.py", label="365", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
