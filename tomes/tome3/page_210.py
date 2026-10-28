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

check_inventory(current_page_number=210, book=3)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Vous pouvez prendre l'arme du Barbare si vous le souhaitez : il
s'agit d'une épée en os incrustée de dents. En examinant son
cadavre, vous découvrez un Bracelet d'Or passé à son poignet
droit.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write("Vous pouvez prendre l'épée en os du Barbare :")
    pickup_button("ÉPÉE D'OS", key="epee_os", label="Prendre l'épée en os")
    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï du Sixième Sens, rendez-vous au :"))
    if has_kai("Le Sixième Sens"):
        st.page_link("tomes/tome3/page_316.py", label="316", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome3/page_316.py", label="316", icon="📄", disabled=True)
    st.write_stream(
        stream_text(
            "Si vous souhaitez vous emparer du Bracelet d'Or, inscrivez-le dans vos Objets Spéciaux et "
            "rendez-vous au :"
        )
    )
    if not has_item("BRACELET D'OR"):
        pickup_button("BRACELET D'OR", key="bracelet", label="Prendre le Bracelet d'Or")
    if has_item("BRACELET D'OR"):
        st.page_link("tomes/tome3/page_236.py", label="236", icon="📄")
    else:
        st.write_stream(stream_text("Prenez d'abord le Bracelet d'Or."))
        st.page_link("tomes/tome3/page_236.py", label="236", icon="📄", disabled=True)
    st.write_stream(
        stream_text(
            "Si vous ne souhaitez pas prendre le Bracelet, hâtez-vous de repartir le long du couloir en "
            "direction d'un croisement situé un peu plus loin. Rendez-vous alors au :"
        )
    )
    st.page_link("tomes/tome3/page_215.py", label="215", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
