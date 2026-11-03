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

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=331, book=4)

fr_text = """
Vous découvrez bientôt un puits de mine qui descend
verticalement dans le flanc de la colline. L'entrée en est
partiellement dissimulée par des buissons d'épines que vos
hommes se hâtent de dégager. Vous remarquez alors une échelle
fixée à la paroi du puits. Il s'agit là sans doute d'une issue de
secours des mines de Maaken qui sillonnent les profondeurs des
contreforts de la chaîne. Si vous parveniez à découvrir l'une des
galeries principales de ces mines, il vous serait alors possible de
rejoindre Ruanon par les souterrains. Vous vous penchez au bord
du puits et vous scrutez l'obscurité au-dessous. Une telle odeur
d'humidité et de pourriture s'échappe du trou que vous décidez
d'envoyer le plus léger de vos hommes essayer l'échelle pour
vérifier si elle est encore solide. Tout semble aller pour le mieux :
votre éclaireur, en effet, atteint bientôt l'entrée d'un tunnel situé
au fond du puits et vous crie de le suivre. Ce tunnel mène à une
salle de forme ovale grossièrement taillée dans la roche. Un
étrange liquide gluant brille sur le sol.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if has_kai("Communication Animale"):
        st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï de la Communication Animale, rendez-vous au :"))
        st.page_link("tomes/tome4/page_41.py", label="41", icon="📄")
    else:
        st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï de la Communication Animale, rendez-vous au :"))
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome4/page_41.py", label="41", icon="📄", disabled=True)
    st.write_stream(stream_text("Sinon, vous chercherez une issue en vous rendant au :"))
    if has_kai("Communication Animale"):
        st.page_link("tomes/tome4/page_276.py", label="276", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome4/page_276.py", label="276", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
