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

check_inventory(current_page_number=325, book=3)

fr_text = """
Le lendemain matin, le ciel est clair et il n'y a pas de vent. Les
rayons du soleil percent une fine couche de nuages en baignant
l'horizon d'une lueur rose pâle. Contemplant ce spectacle
magnifique, vous vous rappelez ce que vous ont dit un jour vos
Maîtres Kaï : la lumière de Kalte est unique, il n'en existe de
semblable nulle part ailleurs, dans les terres de Magnamund tout
au moins. Le matériel et la tente sont bientôt chargés sur les
traîneaux et vous quittez le défilé pour vous aventurer sur la
plaine de Hrod. Il vous faut désormais parcourir plus de 150
kilomètres d'une étendue glacée avant d'atteindre le défilé de la
Tempête. Tout d'abord, le voyage ne présente pas de difficultés.
Le vent a en effet balayé la plaine, rendant le sol parfaitement
lisse et aucune crevasse ne se cache sous la neige dure et
compacte. A l'aube du troisième jour, cependant, les choses
tournent mal. Vous êtes tiré d'un sommeil profond par Dyce qui
vous secoue l'épaule. De toute évidence, il a l'air terrifié. « Que se
passe-t-il ? » demandez-vous d'une voix endormie, le regard
encore brouillé. « A l'horizon... des Barbares des Glaces, répond
Dyce d'une voix hachée, ils sont vingt, peut-être plus. Ils ont cinq
traîneaux à voile et une escorte de guerriers. Je crois bien qu'ils
nous ont vus. » En un instant, vous vous arrachez tous à vos
Couvertures de Fourrure et vous commencez à replier la tente.
Dyce a raison, les Barbares des Glaces sont bien là, en effet, et ils
se dirigent vers vous en venant de l'ouest. « S'ils nous attrapent,
nous sommes morts, » avertit Fenor en achevant d'arrimer le
matériel sur les traîneaux. Les Barbares des Glaces des terres de
Kalte constituent une peuplade féroce et guerrière aux mœurs
nomades. Pendant des millénaires, ils ont sillonné ces déserts
glacés en chassant les animaux pour leur fourrure et en
domestiquant des mammouths. Les seuls contacts qu'ils
entretiennent avec le reste de Magnamund s'établissent au
comptoir de commerce de Liouk. En été, lorsque la banquise a
fondu autour de Liouk, ils se rendent dans la ville pour y
échanger leurs fourrures contre les armes et les outils qu'ils ne
peuvent fabriquer eux-mêmes, le bois et le fer n'existant pas à
l'état naturel dans les terres de Kalte. Ces Barbares éprouvent
une haine profonde pour tous les autres peuples et ils tuent sans
pitié quiconque vient s'aventurer dans leur domaine de glace.
Bientôt, vous entendez leurs cris de guerre, à moins de 5
kilomètres de distance et, pour la première fois depuis que vous
êtes arrivé à Kalte, vous priez le ciel qu'un blizzard se lève pour
vous permettre de leur échapper.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome3/page_216.py", label="216", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
