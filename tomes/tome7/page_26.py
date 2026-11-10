import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_mastered,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=26, book=7)

fr_text = """
L'intérieur de la bulle est constitué de globules graisseux et
translucides qui amortissent la portée de vos coups. Utilisez la
Table de Hasard et ajoutez 3 au chiffre obtenu. Si vous maîtrisez
la Discipline Magnakaï de l'Art des Armes avec une épée,
déduisez 2 points de ce même chiffre. Le résultat final représente
le nombre de points d'ENDURANCE que vous perdez à cause du
manque d'oxygène avant de pouvoir sortir de cette prison
transparente.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # « Art des Armes avec une épée » = Science des Armes à l'Épée : -2 sur la perte
    sword_mastery = is_mastered("ÉPÉE")
    roll = hazard_roll()
    if roll is not None:
        loss = roll + 3 - (2 if sword_mastery else 0)
        # perte appliquée une seule fois par visite
        if not st.session_state.get("visibility_t7_26_bulle"):
            st.session_state["visibility_t7_26_bulle"] = True
            change_endurance(-loss)
        st.write(f"*{roll} + 3" + (" - 2 (Science des Armes à l'Épée)" if sword_mastery else "") + f" = {loss} points d'ENDURANCE perdus.*")
        st.metric(label="Endurance", value=st.session_state.endurance, delta=-loss)
        st.write_stream(stream_text('Si vous survivez à cette terrible épreuve, vous vous empressez de sortir de cet océan de bulles. Rendez-vous au :'))
        st.page_link("tomes/tome7/page_151.py", label="151", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
