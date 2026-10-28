import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=276, book=3)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Vous arrivez bientôt au croisement : là, le couloir dans lequel
vous vous trouvez aboutit à un autre passage orienté est-ouest.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez aller vers l'est, rendez-vous au :"))
    st.page_link("tomes/tome3/page_349.py", label="349", icon="📄")

    st.write_stream(stream_text("Si vous préférez aller vers l'ouest, rendez-vous au :"))
    st.page_link("tomes/tome3/page_50.py", label="50", icon="📄")

    st.write_stream(stream_text("Enfin, si vous maîtrisez les Disciplines Kaï de la Chasse ou de l'Orientation, rendez-vous au :"))
    if has_kai("La Chasse") or has_kai("L'Orientation"):
        st.page_link("tomes/tome3/page_219.py", label="219", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome3/page_219.py", label="219", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
