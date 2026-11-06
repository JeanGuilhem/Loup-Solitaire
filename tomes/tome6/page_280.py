import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    show_illustrations,
    show_map,
)
from text import fr_unknown_magnakai
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=280, book=6)

fr_text = """
Vous chevauchez le long d'un sentier boueux qui suit une corniche
surplombant un grand pont en pierre. De l'autre côté du pont
s'étend une ville dont les hautes murailles et la porte fortifiée
s'élèvent abruptement au-dessus du rivage. La seule façon
d'accéder à la ville est de traverser le pont. Vous regardez,
découragé, les nombreux archers postés tout le long du chemin de
ronde et les énormes chaudrons remplis de plomb fondu. De nombreux
cadavres sont entassés devant la porte de la ville à moitié
détruite, et les carcasses calcinées des tours de siège gisent au
pied des murailles. Vous apercevez aussi la flèche de la
cathédrale, éclairée par les innombrables foyers d'incendie qui
achèvent de se consumer dans le centre de Tekaro. Sans cette
maudite guerre, vous seriez sans doute dans la crypte dans moins
d'une heure. Devant vous, la route descend à pic vers un camp
entouré par un mur fait de terre séchée et de rondins. Les tentes
sont pleines de soldats blessés au cours des assauts innombrables
qui se sont déroulés sur le pont.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de la Science Médicale, vous pouvez vous arrêter pour soigner les blessés, rendez-vous au :"))
    if has_magnakai("Science Médicale"):
        st.page_link("tomes/tome6/page_42.py", label="42", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome6/page_42.py", label="42", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne maîtrisez pas cette Discipline, ou si vous ne souhaitez pas l'utiliser, vous poursuivez votre route, rendez-vous au :"))
    st.page_link("tomes/tome6/page_70.py", label="70", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
