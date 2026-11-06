import streamlit as st
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

check_inventory(current_page_number=5, book=6)

fr_text = """
Le chant du coq vient saluer la naissance du jour. Vous vous
habillez rapidement, puis vous rassemblez vos affaires. Dehors,
Cyrilus est déjà en train de vous attendre dans la cour de
l'auberge. «Quelle belle journée en perspective ! s'exclame-t-il
en pointant vers le ciel sans nuages sa fine canne de chêne. Je
pense que nous atteindrons sans difficultés l'Auberge du Mi-Chemin
avant la tombée de la nuit. » Après avoir pris congé de
l'aubergiste et de son fils, Cyrilus et vous montez en selle et
partez tous deux au petit trot dans la ruelle menant à la porte
est de la ville. Au milieu de la matinée, vous arrivez au pied de
collines vallonnées, plantées d'arbres à feuilles jaunes. Leur
sommet disparaît dans la brume, mais, de temps à autre, des rayons
de soleil viennent éclairer les verts herbages qui s'étendent en
contrebas. Le temps passe vite et agréablement, tandis que Cyrilus
vous raconte l'histoire de la région et les légendes qui s'y
rapportent. Grâce à lui, vous apprenez que les terres fertiles et
les riches royaumes qui bordent la Storn ont un passé mouvementé,
troublé par les guerres incessantes que se livraient entre eux les
ambitieux seigneurs de la région pour annexer les empires voisins
et soumettre à leur domination les populations rurales. Même à
présent, le royaume de Lyris se trouve en conflit avec le Magador,
la province de Delden livre bataille à la Salonie, qui elle-même
est en guerre avec la Slovie ! Des centaines d'hommes perdent la
vie au cours de ces combats sans trêve, et le pays se trouve
régulièrement pillé et dévasté. Seuls les mercenaires et les
charognards semblent tirer profit de cette agitation perpétuelle.
Au milieu de l'après-midi, vous arrivez en vue d'un petit village
situé au bord de la route. De nombreux chariots sont garés les uns
derrière les autres, et une foule de gens s'est rassemblée dans un
pré, non loin de la grand-route. Alors que vous passez près d'eux,
vous remarquez un grand écriteau en bois cloué sur l'un des
chariots :

**GRAND TOURNOI DE TIR A L'ARC**

Droit d'entrée : 2 Pièces d'Or

Premier prix : l'Arc en Argent de Duadon.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez participer au tournoi (droit d'entrée : 2 Pièces d'Or), rendez-vous au :"))
    st.page_link("tomes/tome6/page_141.py", label="141", icon="📄", disabled=not (st.session_state.purse >= 2))

    st.write_stream(stream_text("Si vous ne le désirez pas, ou si vous n'en avez pas les moyens, passez votre chemin et rendez-vous au :"))
    st.page_link("tomes/tome6/page_210.py", label="210", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
