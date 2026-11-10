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

check_inventory(current_page_number=138, book=7)

fr_text = """
Vous dégainez votre arme et vous portez un coup formidable au
cristal noir. Celui-ci se fend en deux, libérant toute sa puissance
maléfique en myriade d'étincelles noires. Les éclats de pierre
tombent au fond de l'abîme de feu qui entoure le trône de
Zahda, étouffant rapidement les flammes. « Maudit sois-tu,
Seigneur Kaï ! » rugit Zahda en surgissant de derrière son trône
en or. Il brandit une fine baguette de platine qu'il pointe sur
votre tête, puis il marmonne une incantation. Mais la puissance
du mal qu'il invoque demeure sourde à sa prière. Des
profondeurs du puits s'élève un grondement qui va en
s'amplifiant ; le sol se met à trembler, et une immense colonne de
feu illumine la salle du trône tout entière, tandis que jaillissent
des flots de lave en fusion. Zahda recule en chancelant, le visage
déformé par la peur. Il s'agenouille précipitamment au pied de
son trône, puis il effleure de ses doigts crochus un pentagramme
gravé dans l'or. Par-dessus le vacarme de la destruction, un autre
son s'élève alors, tel le tintement aigrelet de mille clochettes. Un
faisceau de lumière scintillante descend lentement des ténèbres
surplombant le trône, auréolant graduellement le corps de Zahda
jusqu'à ce que celui-ci soit entièrement enveloppé d'une gaine de
lumière bleue. Puis le corps s'élève dans les airs, comme soulevé
par d'invisibles mains.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez saisir la Pierre de la Sagesse et entrer, à votre tour, dans le rayon de lumière bleue, rendez-vous au :"))
    st.page_link("tomes/tome7/page_118.py", label="118", icon="📄")

    st.write_stream(stream_text("Si vous préférez vous emparer de la Pierre de la Sagesse et prendre immédiatement la fuite à travers le couloir d'acier, rendez-vous au :"))
    st.page_link("tomes/tome7/page_250.py", label="250", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
