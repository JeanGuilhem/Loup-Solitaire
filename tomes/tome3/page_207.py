import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=207, book=3)

fr_text = """
Vous distinguez la sombre silhouette de la créature qui fonce le
long du tunnel dans votre direction. Elle est assoiffée de sang et
frémissante de rage, prête à vous mettre en pièces. Vous songez
alors que, si vous sautez de côté lorsque la créature surgira du
tunnel, il se peut qu'elle vous rate et que, emportée par son élan,
elle tombe tête la première sur la mince couche de glace qui
recouvre le lac.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Si vous souhaitez tenter ce saut de côté lorsque le Languabarb bondira hors du tunnel, rendez- "
            "vous au :"
        )
    )
    st.page_link("tomes/tome3/page_80.py", label="80", icon="📄")
    st.write_stream(
        stream_text(
            "Si vous préférez rester où vous êtes et combattre le monstre quand il sera devant vous, rendez- "
            "vous au :"
        )
    )
    st.page_link("tomes/tome3/page_253.py", label="253", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
