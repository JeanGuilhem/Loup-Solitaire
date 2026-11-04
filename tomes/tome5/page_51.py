import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=51, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Une échelle glissante descend le long d'un puits sombre et
nauséabond. Prenant une profonde inspiration, vous commencez
à descendre après avoir refermé la trappe derrière vous. Une fois
arrivé au fond du puits, vos craintes sont confirmées: vous vous
trouvez à présent dans le Baga-Darooz, le principal égout de
Barrakeesh. Vous vous souvenez alors d'un membre de
l'équipage que l'on avait surnommé le putois, à cause de l'odeur
épouvantable qu'il dégageait.
Cet homme avait été condamné à passer un an dans le Baga-Darooz
pour un crime qu'il n'avait pas commis et il en était
ressorti tellement imprégné par la puanteur de l'égout qu'il
n'avait jamais pu s'en débarrasser ! Scrutant les ténèbres des
tunnels lugubres qui s'ouvrent devant vous, vous vous demandez
comment cet homme avait été capable de survivre dans ce
cloaque humide et malsain. Soudain, vous êtes dérangé dans vos
pensées par une série de craquements : les Sharnazims sont en
train de forcer la trappe. Des éclats de bois tombent en pluie sur
vous, libérant la lourde grille de fer qui vous heurte violemment
l'épaule en s'effondrant. Vous réprimez à grand-peine un
hurlement de douleur et vous perdez 1 point d'ENDURANCE.
Cette partie du Baga-Darooz est un carrefour d'où partent trois
tunnels. Vous devez rapidement choisir la direction que vous
allez prendre, car les hommes de Maouk sont déjà en train de
descendre l'échelle.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-1)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-1)
    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï de l'Orientation, rendez-vous au :"))
    if has_kai("L'Orientation"):
        st.page_link("tomes/tome5/page_173.py", label="173", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_173.py", label="173", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous voulez prendre le tunnel de gauche, rendez-vous au :"))
    st.page_link("tomes/tome5/page_96.py", label="96", icon="📄")

    st.write_stream(stream_text("Si vous souhaitez plutôt prendre celui de droite, rendez-vous au :"))
    st.page_link("tomes/tome5/page_145.py", label="145", icon="📄")

    st.write_stream(stream_text("Si, enfin, vous préférez passer par le tunnel qui se trouve juste en face de vous, rendez-vous au :"))
    st.page_link("tomes/tome5/page_13.py", label="13", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
