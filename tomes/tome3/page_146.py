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
from utils import stream_text, called_cookies, hazard_roll

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."
fr_unknown_item = "Vous ne possédez pas cet objet."

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=146, book=3)

fr_text = """
Centimètre par centimètre vous vous glissez vers l'arrière du
traîneau mais, tout à coup, vous entendez la glace craquer: la
crevasse est en train de s'élargir.
« Sautez ! » hurle Fenor tandis que le traîneau bascule dans le
vide. Vous vous préparez à bondir, mais votre pied se prend dans
les cordes qui maintiennent le matériel.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    has_glaive = has_item("GLAIVE DE SOMMER")
    has_matter = has_kai("Maîtrise Psychique de la Matière")
    st.write_stream(stream_text("Si vous disposez du Glaive de Sommer, rendez-vous au :"))
    if has_item("GLAIVE DE SOMMER"):
        st.page_link("tomes/tome3/page_43.py", label="43", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome3/page_43.py", label="43", icon="📄", disabled=True)
    st.write_stream(stream_text("Si vous possédez la Discipline Kaï de la Maîtrise Psychique de la Matière, rendez-vous au :"))
    if has_kai("Maîtrise Psychique de la Matière"):
        st.page_link("tomes/tome3/page_121.py", label="121", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome3/page_121.py", label="121", icon="📄", disabled=True)
    if not has_glaive and not has_matter:
        st.write_stream(stream_text("Si vous ne possédez ni l'un ni l'autre, utilisez la Table de Hasard pour obtenir un chiffre."))
        number = hazard_roll()
        if number is not None and 1 <= number <= 4:
            st.write_stream(stream_text("Rendez-vous au :"))
            st.page_link("tomes/tome3/page_226.py", label="226", icon="📄")
        elif number is not None and number >= 5:
            st.write_stream(stream_text("Rendez-vous au :"))
            st.page_link("tomes/tome3/page_266.py", label="266", icon="📄")
        elif number == 0:
            st.write_stream(stream_text("Vous avez tiré le 0 : rendez-vous au :"))
            st.page_link("tomes/tome3/page_312.py", label="312", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
