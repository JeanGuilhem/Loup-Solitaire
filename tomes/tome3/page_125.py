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

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=125, book=3)

fr_text = """
Vous avez marché pendant deux heures environ le long du
passage qui descend en pente douce et régulière sur toute sa
longueur ; d'après vos estimations, vous vous trouvez à présent à
peu près 60 mètres plus bas qu'au début de votre exploration et
vous atteignez enfin une vaste caverne de glace au centre de
laquelle s'étend un lac. Il est recouvert d'une fine couche de
glace, et l'eau au-dessous semble obscure et profonde. Vous vous
agenouillez sur la rive pour scruter ces mystérieuses profondeurs
et vous distinguez alors une grande forme noire qui glisse près de
la surface. Il y a donc un être vivant sous cette couche de glace, et
un être d'une taille gigantesque. Soudain, vous entendez des
grognements derrière vous : ce sont ceux d'un Languabarb. Les
bruits viennent du tunnel. Il n'existe qu'une seule issue qui
permette de quitter la caverne : c'est un autre tunnel qui s'ouvre
dans la paroi opposée, de l'autre côté du lac.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez traverser le lac en courant sur sa surface gelée, rendez-vous au :"))
    st.page_link("tomes/tome3/page_322.py", label="322", icon="📄")
    st.write_stream(stream_text("Si vous préférez attendre le Languabarb et le combattre, rendez-vous au :"))
    st.page_link("tomes/tome3/page_207.py", label="207", icon="📄")
    st.write_stream(stream_text("Enfin, si vous maîtrisez la Discipline Kaï du Camouflage, rendez-vous au :"))
    if has_kai("Le Camouflage"):
        st.page_link("tomes/tome3/page_96.py", label="96", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome3/page_96.py", label="96", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
