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

check_inventory(current_page_number=11, book=6)

fr_text = """
La ville d'Eula a été transformée en un gigantesque camp
militaire, et ses habitants l'ont désertée depuis longtemps pour
fuir vers le nord, abandonnant leurs maisons et leurs bêtes à une
horde de soldats cupides. Ceux-ci, venus des quatre coins du pays,
côtoient des mercenaires sans scrupules et des combattants au
passé trouble, qui ne sont unis que par leur avidité commune.
Tandis que vous regardez les importantes troupes marcher en
direction d'un rideau de fumée noire s'élevant au sud, vous sentez
soudain votre cœur défaillir : Tekaro, la ville où se trouve la
Pierre de la Sagesse, est une cité assiégée, une cité capable de
résister à l'assaut de 10 000 hommes d'armes ! Alors que vous
chevauchez en direction du front à travers les champs noircis et
dévastés par la bataille et les retranchements bordant la Quarle,
vous maudissez en votre for intérieur cette guerre qui risque de
mettre en péril le succès de votre quête.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_280.py", label="280", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
