import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

fr_unknown_item = "Vous ne possédez pas cet objet."

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=173, book=3)

fr_text = """
La salle du Trône du Brumalmarc est une vaste pièce dans
laquelle se dresse une sorte de plateau central constitué de blocs
de glace disposés les uns sur les autres. Sur cette plate-forme se
trouve le Trône du Brumalmarc, un trône aussi vieux qu'Ikaya
elle-même. Vonotar y est assis, entouré de gros volumes et
d'étranges accessoires de nécromancien. Il est absorbé dans son
étude et ne vous voit pas entrer. Il reste ainsi quelques instants
sans soupçonner votre présence lorsque, soudain, Loi-Kymar
éternue. « Qui ose me déranger ? » siffle alors Vonotar en se
levant du Trône du Brumalmarc et en cherchant l'intrus du
regard. Lorsqu'il vous voit, il a une sorte de hoquet et une
expression horrifiée transforme son visage. Aussitôt, sa main
cherche hâtivement à saisir une longue Crosse noire : c'est là son
bâton de magicien. Il a l'air d'un assassin que l'on vient de
surprendre en train de commettre un crime particulièrement
abominable. Vous vous hâtez de dégainer votre arme et vous
commencez à escalader la pyramide de cristal. Vous êtes
parfaitement conscient qu'il va falloir faire vite si vous voulez
parvenir à le maîtriser et à le capturer vivant. Lorsque vous
atteignez le bord de la plateforme, vous voyez un large cercle de
blocs de cristal s'enfoncer dans le sol, autour du Trône. Un
profond fossé se forme ainsi entre Vonotar et vous. S'élevant
alors de cette tranchée, vous entendez une série de cris et de
grognements terrifiants qui n'ont rien d'humain. Vous vous
préparez à combattre mais vous ne vous attendiez certainement
pas à voir surgir l'épouvantable créature qui vient d'apparaître
sous vos yeux. Un monstre énorme, verdâtre, répugnant, rampe
en effet hors de l'ombre. Sa tête informe est une gigantesque
masse de tentacules et de ventouses qui laissent suinter une
mucosité gluante, noire et putride. Au centre de cet amas
tremblotant palpite un œil jaune et hideux. Ce monstre est
entièrement soumis à Vonotar qui lui ordonne de s'avancer vers
vous.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    effigy = has_item("EFFIGIE")
    sommerswerd = has_item("GLAIVE DE SOMMER")
    st.write_stream(stream_text('Si vous possédez une Effigie, rendez-vous au :'))
    if effigy:
        st.page_link("tomes/tome3/page_34.py", label="34", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome3/page_34.py", label="34", icon="📄", disabled=True)
    st.write_stream(stream_text("Si vous n'en avez pas, mais si vous disposez en revanche du Glaive de Sommer, rendez-vous au :"))
    st.page_link("tomes/tome3/page_164.py", label="164", icon="📄", disabled=effigy or not sommerswerd)
    st.write_stream(stream_text("Si vous n'avez ni l'un ni l'autre, rendez-vous au :"))
    st.page_link("tomes/tome3/page_200.py", label="200", icon="📄", disabled=effigy or sommerswerd)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
