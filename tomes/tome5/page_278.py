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

check_inventory(current_page_number=278, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Vous courez, courbé en deux, vers votre Glaive que vous saisissez
par la garde, puis vous vous élancez rapidement pour vous
mettre à l'abri derrière un autre pilier. Soudain, un éclair jaillit
du poing du Seigneur des Ténèbres et vient exploser à la base de
la colonne derrière laquelle vous êtes caché. Le pilier s'effondre
dans un fracas assourdissant et la violence de la déflagration
vous projette en arrière. Le rire cruel d'Haakon s'élève au-dessus
du bruit des pierres qui s'écrasent au sol et une douleur atroce
vous vrille le crâne.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï du Bouclier Psychique, rendez-vous au :"))
    if has_kai("Bouclier psychique"):
        st.page_link("tomes/tome5/page_223.py", label="223", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_223.py", label="223", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne maîtrisez pas cette Discipline, rendez-vous au :"))
    if has_kai("Bouclier psychique"):
        st.page_link("tomes/tome5/page_379.py", label="379", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome5/page_379.py", label="379", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
