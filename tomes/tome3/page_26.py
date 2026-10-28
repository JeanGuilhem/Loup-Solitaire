import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    has_kai,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=26, book=3)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."
fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
En dehors des épées d'os, vous trouvez également un poignard et
une masse d'armes, tous deux taillés également dans de l'os. Les
Barbares portent aussi à leur poignet gauche de curieux
Bracelets. Ils sont tout à fait lisses, sans aucune marque ni
inscription et semblent en or massif.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("POIGNARD", key="poignard", label="Prendre le poignard en os")
    pickup_button("MASSE D'ARMES", key="masse", label="Prendre la masse d'armes en os")

    st.write_stream(
        stream_text(
            "Si vous souhaitez prendre l'un de ces Bracelets, passez-le à votre poignet et notez-le "
            "sur votre Feuille d'Aventure dans la case Objets Spéciaux. Rendez-vous ensuite au :"
        )
    )
    if not has_item("BRACELET D'OR"):
        pickup_button("BRACELET D'OR", key="bracelet", label="Prendre un Bracelet d'Or")
    if has_item("BRACELET D'OR"):
        st.page_link("tomes/tome3/page_187.py", label="187", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome3/page_187.py", label="187", icon="📄", disabled=True)

    st.write_stream(
        stream_text(
            'Si vous ne souhaitez pas prendre de Bracelet, vous pouvez poursuivre vos investigations '
            'en vous rendant au :'
        )
    )
    st.page_link("tomes/tome3/page_63.py", label="63", icon="📄")

    st.write_stream(stream_text('Enfin, si vous maîtrisez la Discipline Kaï du Sixième Sens, rendez-vous au :'))
    if has_kai("Le Sixième Sens"):
        st.page_link("tomes/tome3/page_231.py", label="231", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome3/page_231.py", label="231", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
