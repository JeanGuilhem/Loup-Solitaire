import streamlit as st
from inventory import (
    add_to_inventory,
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    is_new_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=40, book=2)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Il faut quatorze jours pour mobiliser l'armée et préparer la flotte de
Durenor. Pendant tout ce temps, vous êtes l'hôte du roi, et vous
demeurez à Hammardal, la capitale du royaume. Chaque jour qui passe
accroît votre inquiétude : que deviennent vos compatriotes dans la ville
assiégée de Holmgard ? Auront-ils la force de résister encore
longtemps aux Maîtres des Ténèbres ? Puissent-ils tenir jusqu'à votre
retour, c'est la prière que vous formulez sans cesse. Vous vivez cet exil
à contrecœur en faisant chaque jour les exercices nécessaires pour vous
maintenir en bonne condition physique ; vous vous adonnez également
à la méditation. Un herboriste de Durenor, un certain Madin Rendalim
est venu vous rendre visite. Sa science dans l'art de guérir est célèbre
d'un bout à l'autre des Fins de Terre et il vous redonne tous vos points
d'ENDURANCE ; vous disposez donc à présent du même total
d'ENDURANCE qu'au tout début de votre mission. Madin Rendalim
vous fait don par la même occasion d'une fiole de Laumspur: il s'agit
d'une puissante potion de guérison qui vous permettra de récupérer 5
points d'ENDURANCE si vous la buvez après un combat. La fiole,
cependant, ne contient qu'une seule dose (vous inscrivez cette potion
sur votre Feuille d'Aventure dans la case Objets contenus dans votre
Sac à Dos). Malheureusement, l'herboriste vous apporte également de
mauvaises nouvelles: on a découvert le cadavre du Lieutenant Général
Rhygar dans la forêt, près de l'entrée du tunnel de Tarnalin. Il a été tué
par un Monstre d'Enfer.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        add_to_inventory("FIOLE DE LAUMSPUR")
    if is_new_page():
        before = st.session_state.endurance
        change_endurance(st.session_state.total_endurance)
        st.session_state["visibility_rendalim"] = st.session_state.endurance - before
    st.metric(label="Endurance", value=st.session_state.endurance, delta=st.session_state.get("visibility_rendalim") or 0)
    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï du Sixième Sens, rendez-vous au :"))
    if has_kai("Le Sixième Sens"):
        st.page_link("tomes/tome2/page_97.py", label="97", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome2/page_97.py", label="97", icon="📄", disabled=True)
    st.write_stream(stream_text("Dans le cas contraire, rendez-vous au :"))
    st.page_link("tomes/tome2/page_242.py", label="242", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
