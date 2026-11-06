import streamlit as st
from inventory import (
    add_arrows,
    buy_button,
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    sell_button,
    show_illustrations,
    show_map,
    spend_gold,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=98, book=6)

fr_text = """
Une forte odeur de poussière et de métal rouillé vous prend à la
gorge lorsque vous pénétrez dans le magasin d'armes. Là, des
armes de toutes sortes sont entassées sur de grands rayonnages,
formant des empilements confus qui s'élèvent jusqu'au plafond.
Les prix sont marqués à la craie sur une grande ardoise
accrochée au-dessus du comptoir :

- Glaive : 7 Pièces d'Or
- Poignard : 2 Pièces d'Or
- Sabre : 3 Pièces d'Or
- Marteau de guerre : 6 Pièces d'Or
- Lance : 5 Pièces d'Or
- Masse d'armes : 4 Pièces d'Or
- Hache : 3 Pièces d'Or
- Arc : 7 Pièces d'Or
- Bâton : 3 Pièces d'Or
- Épée : 4 Pièces d'Or
- Flèches : 1 Pièce d'Or les deux

Vous pouvez acquérir ce que vous voulez, dans la limite de vos
moyens, bien sûr. Par ailleurs, l'armurier achètera d'occasion
certaines armes que vous possédez et dont vous voulez peut-être
vous débarrasser. Dans ce cas, il vous les paiera 1 Pièce d'Or
de moins que le tarif indiqué ci-dessus.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.subheader("Acheter")
    buy_button("GLAIVE", 7, key="t6_98_achat_0")
    buy_button("POIGNARD", 2, key="t6_98_achat_1")
    buy_button("SABRE", 3, key="t6_98_achat_2")
    buy_button("MARTEAU DE GUERRE", 6, key="t6_98_achat_3")
    buy_button("LANCE", 5, key="t6_98_achat_4")
    buy_button("MASSE D'ARMES", 4, key="t6_98_achat_5")
    buy_button("HACHE", 3, key="t6_98_achat_6")
    buy_button("ARC", 7, key="t6_98_achat_7")
    buy_button("BÂTON", 3, key="t6_98_achat_8")
    buy_button("ÉPÉE", 4, key="t6_98_achat_9")
    # flèches : 1 Pièce d'Or les deux, autant de fois que l'on veut (il faut un Carquois)
    if st.button("Acheter 2 flèches (1 Couronne)", key="t6_98_fleches",
                 disabled=not has_item("CARQUOIS") or st.session_state.purse < 1 or st.session_state.get("arrows", 0) >= 6):
        if spend_gold(1):
            add_arrows(2)
            st.rerun()
    st.caption(f"Flèches dans votre Carquois : {st.session_state.get('arrows', 0)}/6")

    st.subheader("Vendre (1 Pièce d'Or de moins que le tarif)")
    sell_button("GLAIVE", 6, key="t6_98_vente_0")
    sell_button("POIGNARD", 1, key="t6_98_vente_1")
    sell_button("SABRE", 2, key="t6_98_vente_2")
    sell_button("MARTEAU DE GUERRE", 5, key="t6_98_vente_3")
    sell_button("LANCE", 4, key="t6_98_vente_4")
    sell_button("MASSE D'ARMES", 3, key="t6_98_vente_5")
    sell_button("HACHE", 2, key="t6_98_vente_6")
    sell_button("ARC", 6, key="t6_98_vente_7")
    sell_button("BÂTON", 2, key="t6_98_vente_8")
    sell_button("ÉPÉE", 3, key="t6_98_vente_9")

    st.write_stream(stream_text("Faites les modifications qui s'imposent sur votre Feuille d'Aventure avant de quitter le magasin, puis rendez-vous au :"))
    st.page_link("tomes/tome6/page_275.py", label="275", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
