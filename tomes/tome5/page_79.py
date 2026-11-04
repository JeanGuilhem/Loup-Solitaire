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

check_inventory(current_page_number=79, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Une rangée d'arbres projette une ombre épaisse qui dissimule
votre approche. La herse est abaissée et seuls deux soldats
montent la garde, là où il devrait y en avoir au moins une dizaine.
Soudain, vous entendez un grincement métallique tandis que la
herse se lève lentement. Les deux Gardes s'effacent pour laisser
passer une troupe de cavaliers sortant du Palais. Les chevaux
s'éloignent au galop en soulevant un épais nuage de poussière
qui enveloppe les Gardes de la tête aux pieds. Ceux-ci se mettent
à tousser et à éternuer, puis ils se ruent vers un abreuvoir pour
apaiser leur gorge desséchée par la poussière. La herse est
toujours levée et le porche n'est plus surveillé.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous décidez de gagner la herse en vous faufilant derrière les Gardes qui sont en train de se désaltérer, rendez-vous au :"))
    st.page_link("tomes/tome5/page_86.py", label="86", icon="📄")

    st.write_stream(stream_text("Si vous voulez les attaquer tandis qu'ils ont le dos tourné, rendez-vous au :"))
    st.page_link("tomes/tome5/page_119.py", label="119", icon="📄")

    st.write_stream(stream_text("Si vous maîtrisez les Disciplines Kaï du Camouflage et de la Chasse, rendez-vous au :"))
    if has_kai("Le Camouflage") and has_kai("La Chasse"):
        st.page_link("tomes/tome5/page_170.py", label="170", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_170.py", label="170", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
