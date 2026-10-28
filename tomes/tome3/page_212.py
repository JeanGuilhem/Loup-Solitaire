import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=212, book=3)

fr_text = """
Lorsque vous revenez sous la tente, Dyce prépare un délicieux
Repas qui vient à point pour vous remplir l'estomac et vous
redonner courage. Vous avez parcouru à présent une distance
appréciable et, en dépit des épreuves physiques que vous avez dû
supporter, vous vous sentez confiant et impatient de continuer.
Irian va chercher les Couvertures de Fourrure dans le traîneau et
vous vous préparez tous à passer une bonne nuit de sommeil. La
nuit, vous gardez toujours vos vêtements pour vous protéger du
froid et vous n'enlevez que vos bottes. Les quelques jours que
vous avez passés sur ces terres désolées ont suffi à vous en
apprendre long sur les techniques de survie. Lorsque vous vous
déchaussez, vous prenez garde à ce que vos bottes conservent
bien la forme de vos pieds : par ces températures glaciales, en
effet, elles ont tôt fait de geler et de devenir dures comme la
pierre ; vous avez alors toutes les peines du monde à les chausser
à nouveau si elles se sont déformées. Pour dénouer vos lacets,
vous devez ôter vos gants, mais il vous faut interrompre
l'opération à plusieurs reprises pour remettre vos moufles dès
que vous sentez la morsure du gel vous engourdir les doigts.
Lorsque vous êtes enfin pelotonné sous vos fourrures, vous
claquez encore des dents pendant quelques instants avant de
sombrer dans un profond sommeil, tandis que le vent mugit au
dehors.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome3/page_238.py", label="238", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
