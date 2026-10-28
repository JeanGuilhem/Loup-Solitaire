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

check_inventory(current_page_number=160, book=3)

fr_text = """
Votre matériel de transport est constitué de deux traîneaux tirés
chacun par un attelage de chiens Kanu. Cette race vigoureuse est
uniquement élevée à Kalte et on ne trouve pas meilleurs chiens
de traîneau. Leur épaisse fourrure fauve, leur poitrail puissant,
leur robustesse et leur ardeur qui ne faiblit jamais, même dans
les climats les plus froids, les rendent particulièrement aptes à
accomplir la tâche qui les attend. Chaque traîneau contient
suffisamment de vivres et de matériel pour mener à bien votre
mission. Quant à vos trois guides, Irian, Fenor et Dyce, ce sont
des trappeurs expérimentés pour qui les techniques de survie
dans les régions polaires n'ont pas de secrets. De plus, ils
connaissent bien les périls cachés qui abondent dans les terres de
Kalte. Dès que les chiens sont attelés, vous prenez place sur l'un
des traîneaux en compagnie de Dyce, tandis que les autres
ouvrent la voie sur l'autre traîneau. En contemplant l'étendue
glacée de la banquise de Liouk, vous apercevez une lueur blanche
à l'horizon : c'est le glacier de Viad dont la coulée de glace vient
se jeter sur la banquise. L'air vif et limpide de Kalte donne une
fausse impression des distances : on dirait que le glacier se
trouve à une dizaine de kilomètres, alors qu'en fait il est distant
d'au moins 100 kilomètres. La première journée de votre voyage
se passe bien et vous parcourez un bon nombre de kilomètres.
Lorsque, enfin, le soleil se couche, vous décidez d'établir votre
campement pour la nuit. Vous vous arrêtez au milieu d'un cercle
formé par des piliers de glace qui se sont dressés sous la pression
de la banquise sans cesse en mouvement. Les traîneaux sont
rangés côte à côte et la tente installée juste devant. On trouve
ensuite un abri où les chiens pourront passer la nuit, puis l'heure
vient de préparer le dîner. Vous êtes tous rassemblés sous la
tente lorsqu'un terrible rugissement retentit soudain au-dehors.
« Par tous les dieux ! s'écrie Irian, un Bakanal ! » Les Bakanals
sont de grandes créatures carnivores qui vivent à proximité des
côtes de Kalte. Ils se nourrissent habituellement de gaillelots ou
de petites ostrelles qui abondent au bord de la mer. Ce Bakanal,
cependant, a été attiré par l'odeur des chiens et il s'apprête à les
attaquer, bien décidé à en dévorer plusieurs d'un coup.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez sortir de la tente pour vous lancer à l'attaque du Bakanal, rendez-vous au :"))
    st.page_link("tomes/tome3/page_78.py", label="78", icon="📄")
    st.write_stream(stream_text('Si vous maîtrisez la Discipline Kaï de la Chasse, rendez-vous au :'))
    if has_kai("La Chasse"):
        st.page_link("tomes/tome3/page_204.py", label="204", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome3/page_204.py", label="204", icon="📄", disabled=True)
    st.write_stream(stream_text('Si vous maîtrisez la Discipline Kaï de la Communication Animale, rendez-vous au :'))
    if has_kai("Communication Animale"):
        st.page_link("tomes/tome3/page_318.py", label="318", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome3/page_318.py", label="318", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
