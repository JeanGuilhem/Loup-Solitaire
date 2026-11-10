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

check_inventory(current_page_number=315, book=7)

fr_text = """
Le couloir tout entier est violemment secoué par toute une série
d'éruptions qui tordent le fer et font s'écrouler les murs. Les
affreux serviteurs de Zahda s'agitent autour de vous en poussant
des cris de terreur dans la panique la plus totale tandis qu'ils
cherchent désespérément à fuir Kazan-Oud. Des jets de gaz
enflammé jaillissent des fissures du sol, et vous courez le plus
rapidement possible parmi les décombres de la forteresse qui
s'effondre, essayant de grimper, de ramper et de sauter par-
dessus les nombreux obstacles qui se dressent devant vous. Des
créatures du labyrinthe envahissent maintenant tous les niveaux,
ajoutant encore à la panique et au carnage tandis qu'elles
dévorent les malheureux qui se trouvent sur leur chemin. Vous
parcourez plus d'un kilomètre le long du passage en ruine avant
de trouver un escalier intact. Il monte en serpentant dans
l'obscurité et, tandis que vous gravissez les marches jonchées de
gravats, des flammes vous lèchent les pieds. Les cris provenant
des niveaux inférieurs sont maintenant complètement recouverts
par le vacarme assourdissant des explosions et le crépitement
des flammes. Vous êtes au bord de l'évanouissement lorsque
vous émergez enfin des ténèbres dans l'éclatante lumière du jour.
Vous trébuchez et vous tombez, momentanément aveuglé.
Cependant, vos yeux s'habituent peu à peu à la lumière. Vous
vous relevez et apercevez les remparts en ruine et, très loin en
dessous, les eaux miroitantes du lac Khor. Les murs de la
forteresse s'écroulent rapidement, et le sol est constamment
ébranlé par de violentes secousses. Vous courez à toutes jambes à
travers l'entrée principale tandis que le pouvoir agonisant de
Kazan-Oud jette des éclairs dans le ciel. En haut d'un escalier en
ruine, vous regardez le rivage loin en contrebas.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez descendre l'escalier vers la vieille jetée en pierre, rendez-vous au :"))
    st.page_link("tomes/tome7/page_122.py", label="122", icon="📄")
    st.write_stream(stream_text("Si vous voulez vous frayer un chemin vers la plage, rendez-vous au :"))
    st.page_link("tomes/tome7/page_309.py", label="309", icon="📄")
    st.write_stream(stream_text("Si vous préférez plonger dans l'eau, depuis la falaise, rendez-vous au :"))
    st.page_link("tomes/tome7/page_254.py", label="254", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
