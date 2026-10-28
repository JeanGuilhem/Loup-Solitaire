import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=273, book=3)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Vous allez voyager en traîneau jusqu'à Ikaya. Vous disposez de
deux traîneaux chargés de vivres et de matériel et tirés par des
attelages de chiens Kanu. Il s'agit d'une race de chiens de
traîneaux particulièrement robustes que l'on élève uniquement
dans les terres de Kalte. Leur épaisse fourrure fauve et leur
puissant poitrail, ainsi que leur ardeur bien connue les rendent
parfaitement aptes à accomplir la rude tâche qui les attend. Vos
trois guides, Irian, Fenor et Dyce, sont tous des trappeurs
expérimentés. Les techniques de survie dans les déserts glacés
n'ont plus de secrets pour eux et ils connaissent bien les
multiples dangers que recèle le pays de Kalte. Dès que les chiens
sont attelés, vous montez sur l'un des traîneaux en compagnie
d'Irian et vous faites signe aux autres d'ouvrir la voie. En
contemplant l'étendue glacée de la banquise de Liouk, vous
apercevez au loin une tache blanche étincelante : c'est la plaine
de Hrod qui se reflète ainsi sous le soleil. « Ne vous y fiez pas, il
s'agit en fait d'un mirage, avertit Irian, les yeux brillants sous son
capuchon de fourrure. La plaine de glace se reflète dans
l'atmosphère en donnant l'impression qu'elle se trouve à 6 ou 7
kilomètres mais, en fait, elle est distante d'au moins 60
kilomètres. Les apparences peuvent être trompeuses dans les
terres de Kalte. » Le temps est clair et aucun vent ne souffle, ce
qui vous permet de parcourir une distance appréciable dès ce
premier jour. A la nuit tombée, vous établissez votre camp. Les
traîneaux sont rangés côte à côte et la tente dressée sous un roc
en saillie qui offre un bon abri contre le vent.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï du Sixième Sens, rendez-vous au :"))
    if has_kai("Le Sixième Sens"):
        st.page_link("tomes/tome3/page_35.py", label="35", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome3/page_35.py", label="35", icon="📄", disabled=True)
        st.write_stream(stream_text("Sinon, rendez-vous au :"))
        st.page_link("tomes/tome3/page_112.py", label="112", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
