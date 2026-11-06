import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    show_illustrations,
    show_map,
)
from text import fr_unknown_magnakai
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=39, book=6)

fr_text = """
La poursuite vous conduit au cœur des nombreuses collines qui
entourent Varetta. La grand-route plonge et serpente de vallée en
vallée, entrecoupée de temps à autre par des torrents tumultueux,
puis elle remonte à travers les forêts denses qui bordent des
précipices et des failles d'une profondeur vertigineuse. Vous
perdez souvent les cavaliers de vue, mais votre remarquable
maîtrise des Disciplines Kaï de la Chasse et de l'Orientation vous
permet de suivre leur trace. Cependant, la piste se brouille
lorsque vous atteignez un petit village perché au bord d'un à-pic
bordé d'arbres. Vous remarquez toutefois qu'au bout de la bourgade
il y a un sentier pierreux qui coupe la grand-route pour monter
abruptement à travers les arbres.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez continuer par la grand-route, rendez-vous au :"))
    st.page_link("tomes/tome6/page_143.py", label="143", icon="📄")

    st.write_stream(stream_text("Si vous préférez suivre le sentier escarpé, rendez-vous au :"))
    st.page_link("tomes/tome6/page_241.py", label="241", icon="📄")

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de l'Exploration, rendez-vous au :"))
    if has_magnakai("Exploration"):
        st.page_link("tomes/tome6/page_117.py", label="117", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome6/page_117.py", label="117", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
