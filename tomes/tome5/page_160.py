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

check_inventory(current_page_number=160, book=5)

fr_text = """
La peur de perdre votre bras est plus grande que le désir que vous avez de quitter cette ville hostile. Vous devez
impérativement vous procurer de l'herbe d'Oede, même si cela
signifie que vous allez devoir vous rendre à l'endroit que vous
redoutez le plus : le Grand Palais. Vous suivez l'allée sinueuse à
travers le Mikarum et vous arrivez au Horm-tas-Lallaim : la
Sépulture des Princesses. Derrière le tombeau se dresse le Grand
Palais, tel un imposant panthéon blanc. Vous vous rappelez tout
à coup une vieille légende que vous racontait votre maître Kaï, il
y a bien longtemps : La vengeance du Zakhan noir. Le Zakhan
noir était un tyran brutal, le plus cruel d'une lignée sanguinaire
qui régna jadis sur le Désert. La barbarie de ce règne est restée
gravée à jamais dans la mémoire des habitants des régions des
Fins de Terre. Ce Zakhan fit construire le Grand Palais par son
armée d'esclaves faits prisonniers dans les pays qu'il conquit à la
pointe de l'épée. Le Palais devint son obsession ; il dirigeait lui-
même les travaux et punissait personnellement les ouvriers
lorsque les travaux prenaient le moindre retard. Il massacrait ses
sujets sans discrimination et de la manière la plus terrifiante. Le
mode d'exécution qu'il appréciait le plus consistait à scier la
pauvre victime en deux des pieds à la tête jusqu'à ce que les deux
parties du corps tombent au sol. Mais c'est surtout après
l'exécution massive des esclaves qui avaient construit le Grand
Palais qu'il est devenu aux yeux de tous le plus grand criminel de
son temps. Il supprima en effet tous les esclaves afin que ses
ennemis ne puissent jamais connaître l'existence des chambres
secrètes renfermant les trésors. Parmi les victimes se trouvaient
ses deux filles, Kebilla et Sousse, qui s'étaient opposées
ouvertement à la cruauté de leur père et avaient essayé
d'empêcher ce massacre. Dans une rage aveugle, il ordonna
qu'elles fussent les premières à mourir. Il aurait mieux valu pour
le Zakhan et pour la Vassagonie qu'il mourût ce jour-là. Il vécut
encore deux ans, mais rongé par le remords, il se prit en horreur
et sombra dans le désespoir. Dans le Grand Palais, le silence de la
nuit était souvent rompu par les cris et les gémissements du
Zakhan qui errait tel un spectre dans les pièces du Palais à la
recherche de ses filles. Lorsqu'il mourut, il fut enterré à leurs
côtés, dans la Sépulture des Princesses. D'où vous êtes, vous
pouvez voir deux entrées qui donnent accès au Grand Palais :
une porte hérissée de pointes dans la muraille nord et une arcade
dans la muraille ouest, fermée par une herse. Le Palais est
habituellement très bien gardé, mais il y a peu de sentinelles
aujourd'hui, car la plupart sont parties à votre recherche dans la
ville.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous désirez approcher par la porte nord, rendez-vous au :'))
    st.page_link("tomes/tome5/page_126.py", label="126", icon="📄")

    st.write_stream(stream_text('Si vous préférez vous approcher de la porte ouest, rendez-vous au :'))
    st.page_link("tomes/tome5/page_79.py", label="79", icon="📄")

    st.write_stream(stream_text('Enfin, si vous préférez trouver un autre moyen de pénétrer dans le Palais, rendez-vous au :'))
    st.page_link("tomes/tome5/page_49.py", label="49", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
