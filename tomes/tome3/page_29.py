import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import stream_text, hazard_roll, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=29, book=3)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."
fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
La crevasse s'élargit de plus en plus. Vous voyez Fenor sauter et
atterrir sans dommage au bord du gouffre. Vous vous apprêtez à
bondir à votre tour lorsque vous vous apercevez avec horreur que
votre pied gauche se trouve pris dans les cordages du traîneau.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous possédez le Glaive de Sommer, rendez-vous au :'))
    if has_item("GLAIVE DE SOMMER"):
        st.page_link("tomes/tome3/page_43.py", label="43", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome3/page_43.py", label="43", icon="📄", disabled=True)

    st.write_stream(
        stream_text(
            'Si vous possédez la Discipline Kaï de la Maîtrise Psychique de la Matière, rendez-vous '
            'au :'
        )
    )
    if has_kai("Maîtrise Psychique de la Matière"):
        st.page_link("tomes/tome3/page_121.py", label="121", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome3/page_121.py", label="121", icon="📄", disabled=True)

    if not has_item("GLAIVE DE SOMMER") and not has_kai("Maîtrise Psychique de la Matière"):
        st.write_stream(
            stream_text(
                "Si vous n'avez ni l'un ni l'autre, utilisez la Table de Hasard pour obtenir un chiffre."
            )
        )
        roll = hazard_roll()
        if roll is not None and 1 <= roll <= 4:
            st.page_link("tomes/tome3/page_226.py", label="226", icon="📄")
        elif roll is not None and roll >= 5:
            st.page_link("tomes/tome3/page_266.py", label="266", icon="📄")
        elif roll == 0:
            st.page_link("tomes/tome3/page_312.py", label="312", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
