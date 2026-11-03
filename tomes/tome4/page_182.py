import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=182, book=4)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Les roulottes sont disposées en un cercle à l'intérieur duquel
vous établissez votre campement. Un patrouilleur reçoit pour
mission de surveiller les abords du camp. Les troubadours, quant
à eux, construisent une petite scène sur laquelle bientôt s'avance
Yesu. Il demande le silence puis annonce le titre de la pièce qui
va être jouée : « Les Vaillants Guerriers du Sommerlund ». C'est
là un programme qui provoque les cris d'enthousiasme de vos
hommes. Au cours de la représentation, un détail étrange attire
votre attention : l'un des acteurs utilise en effet une épée
véritable. Or, ce genre d'épée n'appartient qu'aux officiers de la
cavalerie du Sommerlund. A la fin de la pièce, vous vous
approchez de l'homme pour l'interroger au sujet de cette arme. Il
vous regarde alors d'un air inquiet puis s'enfuit dans l'obscurité
qui règne autour du camp.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    tracker = has_kai("L'Orientation") or has_kai("La Chasse")

    st.write_stream(stream_text("Si vous souhaitez le poursuivre et que vous maîtrisiez les Disciplines Kaï de l'Orientation ou de la Chasse, rendez-vous au :"))
    if tracker:
        st.page_link("tomes/tome4/page_332.py", label="332", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome4/page_332.py", label="332", icon="📄", disabled=True)

    st.write_stream(stream_text("Si ces Disciplines vous sont inconnues, mais que vous vouliez malgré tout poursuivre l'acteur, rendez-vous au :"))
    st.page_link("tomes/tome4/page_58.py", label="58", icon="📄", disabled=tracker)

    st.write_stream(stream_text("Si vous préférez le laisser s'enfuir, revenez auprès de vos hommes en vous rendant au :"))
    st.page_link("tomes/tome4/page_165.py", label="165", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
