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

check_inventory(current_page_number=200, book=7)

fr_text = """
Les éruptions sont de plus en plus violentes ; des pierres et des
débris de métal sont projetés jusqu'en haut de la salle de trône.
Certains blocs de pierre atteignent la taille d'un cheval, mais ils
semblent retomber très lentement autour du rayon, tandis que
vous êtes attiré malgré vous vers le toit. Soudain, le rayon
disparaît, et vous vous retrouvez sur un socle circulaire, au centre
d'un temple en ruine, près du corps de garde du donjon. Pendant
un instant, vous êtes aveuglé par la lumière du jour, puis
lentement vos yeux s'habituent et vous regardez les eaux
scintillantes du lac Khor et la ville de Herdos poindre à l'horizon.
Le sol est secoué par de constantes vibrations, les bâtiments
commencent à s'écrouler et les murs de la forteresse se lézardent
de façon inquiétante. Sans perdre un instant, vous vous
précipitez vers la sortie, tandis que les éclairs du pouvoir
agonisant de Kazan-Oud déchirent le ciel. En haut des marches,
vous contemplez à nouveau le lac, loin en contrebas.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez descendre l'escalier qui mène à la vieille jetée, rendez-vous au :"))
    st.page_link("tomes/tome7/page_122.py", label="122", icon="📄")

    st.write_stream(stream_text("Si vous préférez essayer de descendre vers la plage, rendez-vous au :"))
    st.page_link("tomes/tome7/page_309.py", label="309", icon="📄")

    st.write_stream(stream_text("Si vous voulez plonger dans le lac du haut de la falaise, rendez-vous au :"))
    st.page_link("tomes/tome7/page_254.py", label="254", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
