import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=154, book=7)

fr_text = """
Vous vous aplatissez contre la paroi et vous regardez dévaler le
tronc d'arbre avec un effroi grandissant. L'énorme tronc passe
au-dessus du vide, puis heurte violemment les marches, à
quelques centimètres de l'endroit où vous vous trouvez. Sous le
choc, des morceaux de branches éclatées vous entaillent
profondément la joue et vous éraflent les côtes. La douleur vous
arrache un cri et vous perdez 3 points d'ENDURANCE. L'arbre
termine sa course sur la plage en contrebas ; il se plante avec
force dans le sable noir, et vous le voyez vibrer pendant quelques
secondes, tel un gigantesque javelot. Après avoir essuyé le sang
qui ruisselle sur votre visage, vous regardez à nouveau l'escalier
éventré : comment donc allez-vous pouvoir le franchir ?
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-3)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-3)

    rope = has_item("CORDE")
    st.write_stream(stream_text("Si vous possédez une Corde, rendez-vous au :"))
    st.page_link("tomes/tome7/page_310.py", label="310", icon="📄", disabled=not rope)

    st.write_stream(stream_text("Sinon, rendez-vous au :"))
    st.page_link("tomes/tome7/page_211.py", label="211", icon="📄", disabled=rope)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
