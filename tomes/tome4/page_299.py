import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=299, book=4)

fr_text = """
Vous disposez vos hommes côte à côte devant l'entrée de la mine.
Leurs boucliers forment un mur de bois et d'acier qui détourne
les flèches tirées par vos ennemis. Les brigands sautent bientôt
des arbres et abandonnent leurs arcs pour dégainer leurs longues
épées à la lame recourbée. Plusieurs d'entre eux trébuchent et
tombent à terre, mais leur chef les pousse en avant en leur
donnant de grands coups dans le dos du plat de sa hache de
guerre. L'homme est une brute repoussante vêtue d'une lourde
cotte de mailles en cuivre. Les premiers brigands se jettent sur le
mur de boucliers, en poussant des cris de guerre assourdissants.
Un déluge de coups s'abat sur vos hommes qui tiennent bon,
cependant, se défendant vaillamment contre l'ennemi qui tente
de les anéantir. La première vague de brigands recule en
chancelant. Ils ont les mains crispées sur leurs blessures, tandis
qu'une douzaine de leurs camarades restent étendus morts à vos
pieds. Aucun de vos hommes n'est tombé. Quant à vous, à peine
avez-vous pris le temps d'essuyer votre front éclaboussé de sang
que le chef ennemi se rue sur vous en brandissant sa hache de
guerre. A grands coups de son arme redoutable, il écarte les
boucliers de vos hommes et vous attaque. Il vous est impossible
de prendre la fuite. Vous devrez le combattre jusqu'à la mort de
l'un de vous deux.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("CHEF BRIGAND", 19, 29)])
    if outcome == "win":
        st.write_stream(stream_text('Si vous êtes vainqueur, rendez-vous au :'))
        st.page_link("tomes/tome4/page_121.py", label="121", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
