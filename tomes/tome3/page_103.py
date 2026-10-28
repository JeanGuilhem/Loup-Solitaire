import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=103, book=3)

fr_text = """
Le lendemain, un fort vent se lève en provenance du nord. Des
heures durant, il vous souffle au visage sans un instant de répit.
La banquise de Liouk se transforme peu à peu, au fur et à mesure
de votre avance, en une masse de blocs de glace déchiquetés qui
pointent leurs arêtes vers le ciel. Vous ne parvenez à progresser
que lentement et avec difficulté. Vers midi, vous tremblez de
froid, vos lèvres gercées saignent et les rafales de vent glacé vous
ont recouvert des pieds à la tête d'une fine pellicule de neige.
Vous dirigez votre traîneau vers un étroit passage qui marque la
jonction entre la banquise et la plaine de Hrod. Ce défilé vous
protège du vent et, pour la première fois de la journée, vous
bénéficiez d'une bonne visibilité. Soudain, des cris au-dessus de
votre tête vous indiquent que vous n'êtes pas, vos guides et vous-même,
les seules créatures à avoir choisi cet endroit pour vous
abriter. Quelques secondes plus tard, en effet, trois gros Bakanals
sautant du mur de glace se jettent sur vos traîneaux et y
atterrissent dans un grand fracas. Votre compagnon de traîneau,
Irian, est projeté sur la glace et tombe assommé. Un Bakanal
affamé vous empêche de lui porter secours et il est inutile de
tenter d'échapper à la créature Carnivore : il vous faut la
combattre jusqu'à la mort de l'un de vous deux.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("BAKANAL", 19, 30)])
    if outcome == "win":
        st.write_stream(stream_text("Si vous sortez vainqueur de l'affrontement, rendez-vous au :"))
        st.page_link("tomes/tome3/page_305.py", label="305", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
