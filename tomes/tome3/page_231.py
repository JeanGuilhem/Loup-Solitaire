import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=231, book=3)

fr_text = """
Vous sentez qu'il y a là quelque chose d'anormal. Les terres de
Kalte, en effet, sont dépourvues de mines et, par conséquent,
tous les métaux, et pas seulement l'or, y sont considérés comme
un bien rare et précieux. Le seul moyen qu'ont les Barbares des
Glaces de se procurer du métal, c'est de l'échanger chaque été
contre des fourrures sur le marché de Liouk ; mais seul l'acier les
intéresse. Aussi en déduisez-vous que ces Bracelets sont portés
par obligation plutôt que par souci de coquetterie.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Si vous souhaitez passer l'un de ces Bracelets d'Or à votre poignet, inscrivez-le dans vos "
            "Objets Spéciaux et rendez-vous au :"
        )
    )
    if not has_item("BRACELET D'OR"):
        pickup_button("BRACELET D'OR", key="bracelet", label="Prendre un Bracelet d'Or")
    if has_item("BRACELET D'OR"):
        st.page_link("tomes/tome3/page_187.py", label="187", icon="📄")
    else:
        st.write_stream(stream_text("Prenez d'abord un Bracelet d'Or."))
        st.page_link("tomes/tome3/page_187.py", label="187", icon="📄", disabled=True)
    st.write_stream(
        stream_text(
            "Si vous préférez laisser ces Bracelets là où ils sont et poursuivre votre exploration d'Ikaya, "
            "rendez-vous au :"
        )
    )
    st.page_link("tomes/tome3/page_63.py", label="63", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
