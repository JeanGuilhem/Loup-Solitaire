import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    set_flag,
    show_illustrations,
    show_map,
    spend_gold,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=220, book=6)

fr_text = """
La plaque rouillée par les intempéries, qui est vissée sur le socle,
indique qu'il s'agit d'une statue de Vynar Jupe. C'était le chef
d'une horde de brigands qui rançonnait les voyageurs et plus
particulièrement les marchands. Mais, malgré les nombreux
méfaits et meurtres qu'il a commis, il est devenu populaire car il
était audacieux et très rusé et, surtout, parce qu'il n'a jamais pillé
les habitants de son hameau natal. Finalement, il fut pris avec
une vingtaine de ses hommes, et, après leur procès à Amory, la
hache du bourreau mit fin à leurs tristes exploits. Il y a une fente
dans le ventre de la statue par où l'on peut jeter des Pièces d'Or.
La plaque mentionne aussi que quiconque honore la statue de
Vynar Jupe obtiendra en retour sa protection contre les voleurs
et autres bandits de grand chemin. Si vous souhaitez faire un
don, placez quelques Pièces d'Or dans la statue avant de quitter
le petit village, (n'oubliez pas de rayer le nombre de Pièces d'Or
que vous donnez sur votre Feuille d'Aventure.)
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # Fait posé : « don à la statue de Vynar Jupe »
    if not st.session_state.get("visibility_don_220"):
        amount = st.number_input(
            "Pièces d'Or à glisser dans la statue", min_value=1, max_value=max(1, st.session_state.purse),
            value=1, step=1, key="don_220",
        )
        if st.button("Faire un don", disabled=st.session_state.purse < 1):
            if spend_gold(int(amount)):
                set_flag("don à la statue de Vynar Jupe")
                st.session_state["visibility_don_220"] = int(amount)
                st.rerun()
    else:
        st.write(f"*Vous avez glissé {st.session_state['visibility_don_220']} Pièce(s) d'Or dans la statue.*")

    st.write_stream(stream_text("Rendez-vous à présent au :"))
    st.page_link("tomes/tome6/page_73.py", label="73", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
