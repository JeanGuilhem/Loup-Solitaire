import streamlit as st
from inventory import (
    check_inventory,
    choose_gifts,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=15, book=2)

fr_text = """
Il n'a plus l'air soupçonneux, à présent, mais surpris. «Je pensais que
vous étiez un imposteur, Seigneur Kaï, dit-il, et je dois vous avouer que
j'avais l'intention de vous donner une leçon que vous n'auriez jamais
oubliée votre vie durant. Pardonnez-moi d'avoir douté de vous mais
votre récit m'a paru si effrayant que je n'ai pu me résoudre à y croire, de
peur qu'il ne fût vrai. J'ai fait le serment de défendre cette frontière et il
m'est impossible de quitter la tour, mais si l'un quelconque des objets
que je possède peut être utile à votre quête, sachez que je vous en fait
volontiers don. » Il dispose alors sur une grande table de chêne les
objets suivants et vous invite à choisir l'un d'eux : Glaive, Masse
d'Armes, Bâton, Potion de Guérison (une dose qui vous redonne 3
points d'ENDURANCE), 3 Repas, 1 Sac à Dos, 12 Pièces d'Or. Vous
faites votre choix et vous vous apprêtez à quitter la tour. L'homme vous
indique du doigt la direction à prendre. « Lorsque vous serez parvenu
au chenal de Ryner, suivez le chemin orienté au nord. Vous arriverez
alors à un pont que gardent des soldats du roi. Quand ils vous
demanderont le mot de passe, vous répondrez : "Crépuscule." La route
au-delà du pont mène à Port Bax. Que Dieu vous aide, Loup Solitaire. »
Vous remerciez ce valeureux guerrier et vous vous mettez en chemin. Il
vous faut cependant abandonner votre cheval car il vous serait
impossible de franchir sur son dos la forêt dense qui s'étend devant
vous.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    choose_gifts(
        {
            "Glaive": ("GLAIVE", 1),
            "Masse d'Armes": ("MASSE D'ARMES", 1),
            "Bâton": ("BÂTON", 1),
            "Potion de Guérison (3 points d'ENDURANCE)": ("PETITE POTION DE GUÉRISON", 1),
            "3 Repas": ("REPAS", 3),
            "1 Sac à Dos": ("SAC À DOS", 1),
            "12 Pièces d'Or": (None, 12),
        },
        1,
        key="gift",
        label="Choisissez l'un des objets du garde",
    )
    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_244.py", label="244", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
