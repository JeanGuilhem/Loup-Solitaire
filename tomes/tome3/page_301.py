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

check_inventory(current_page_number=301, book=3)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."
fr_one_kai = "Vous maîtrisez au moins l'une de ces Disciplines Kaï."

fr_text = """
« Nous sommes à l'étage où se trouve la salle du Trône du
Brumalmarc, murmure Loi-Kymar en regardant à travers une
fente de la porte de la cuisine. Elle est située au bout de ce
couloir. » Deux Barbares des Glaces sont assis près des portes
incrustées de pierreries qui donnent accès à la grande salle du
Trône. Ils sont protégés de la tête aux pieds par d'étranges
armures en os et armés d'épées de cristal. Le vieux magicien se
tourne vers vous et dit : « Avec eux, il faut agir vite et en silence. »
Il tire alors de ses poches trois bocaux et marmonne une
incantation en mélangeant leurs contenus dans un bol de pierre.
Il prend ensuite un pichet d'eau dont il verse quelques gouttes
sur la mixture : aussitôt, un filet de fumée bleue s'élève du bol.
« Voici qui fera taire les gardes si nous parvenons à placer le bol
suffisamment près d'eux. »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï du Camouflage, rendez-vous au :"))
    if has_kai("Le Camouflage"):
        st.page_link("tomes/tome3/page_122.py", label="122", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome3/page_122.py", label="122", icon="📄", disabled=True)
    st.write_stream(stream_text("Si vous possédez la Discipline Kaï de la Maîtrise Psychique de la Matière, rendez-vous au :"))
    if has_kai("Maîtrise Psychique de la Matière"):
        st.page_link("tomes/tome3/page_228.py", label="228", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome3/page_228.py", label="228", icon="📄", disabled=True)
    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï de la Chasse, rendez-vous au :"))
    if has_kai("La Chasse"):
        st.page_link("tomes/tome3/page_347.py", label="347", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome3/page_347.py", label="347", icon="📄", disabled=True)
    st.write_stream(stream_text("Si vous ne maîtrisez aucune de ces Disciplines, rendez-vous au :"))
    if not (has_kai("Le Camouflage") or has_kai("Maîtrise Psychique de la Matière") or has_kai("La Chasse")):
        st.page_link("tomes/tome3/page_179.py", label="179", icon="📄")
    else:
        st.write_stream(stream_text(fr_one_kai))
        st.page_link("tomes/tome3/page_179.py", label="179", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
