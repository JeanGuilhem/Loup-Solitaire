import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies, handle_repas

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=132, book=3)

fr_text = """
A moins que vous ne veniez de prendre un Repas, vous perdez 3
points d'ENDURANCE, tant vous êtes affamé. Vous poursuivez
votre chemin le long du tunnel pendant encore plus d'un
kilomètre, mais bientôt, vous êtes fatigué et vous vous arrêtez
pour dormir. Lorsque vous vous réveillez, vous vous sentez
mieux ; vous n'avez cependant aucune idée du temps qu'a duré
votre sommeil, car la lumière qui éclaire ces grottes ne change
jamais, qu'il fasse jour ou nuit. Vous reprenez votre marche en
continuant tout droit pendant des kilomètres. Vous traversez
plusieurs grottes immenses où se dressent d'imposants piliers de
cristal. Dans l'une de ces vastes cavernes, vous êtes fasciné par
une magnifique voûte de glace étincelante. Mais un peu plus loin,
un spectacle encore plus impressionnant vous attend. Un étroit
passage conduit en effet à une corniche qui longe le bord d'un
gouffre gigantesque de près d'un kilomètre de largeur. Vous
contournez ce vide terrifiant en essayant de ne pas baisser le
regard vers ses profondeurs agitées par les vents, à plusieurs
kilomètres au-dessous. Vous marchez sur la corniche depuis
seulement quelques minutes lorsqu'un bruit dans votre dos attire
votre attention. Vous jetez un coup d'œil en arrière et vous vous
apercevez alors avec horreur qu'un monstrueux serpent à deux
têtes vous suit à quelques mètres.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # « à moins que vous ne veniez de prendre un Repas » : vous avez mangé la carcasse rôtie au 295 ou au 309
    if is_new_page():
        st.session_state["t3_132_vient_de_manger"] = st.session_state.last_page_number in (295, 309)
    if st.session_state.get("t3_132_vient_de_manger"):
        st.success("*Vous venez de vous rassasier de viande rôtie : vous n'avez pas faim.*")
    else:
        handle_repas()
    st.write_stream(stream_text("Si vous maîtrisez les Disciplines Kaï de l'Orientation ou de la Communication Animale, rendez-vous au :"))
    if has_kai("L'Orientation") or has_kai("Communication Animale"):
        st.page_link("tomes/tome3/page_229.py", label="229", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome3/page_229.py", label="229", icon="📄", disabled=True)
        st.write_stream(stream_text("Dans le cas contraire, rendez-vous au :"))
        st.page_link("tomes/tome3/page_88.py", label="88", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
