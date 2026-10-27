import streamlit as st
from inventory import (
    buy_button,
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=283, book=2)

fr_text = """
Vous êtes impressionné par l'abondance et la diversité des
marchandises exposées : il y a là des soies et des épices en provenance
des bazars de Vassagonia, des pierres précieuses des mines de Bor, les
plus belles armes et cuirasses forgées par les armuriers de Durenor, des
fourrures de Kalte, des étoffes de Cloeasia et sur toutes les tables les
mets et les boissons les plus variés qui s'offrent à l'appétit des visiteurs.
Au centre du magasin, les prix de toutes les marchandises sont indiqués
sur de grandes peaux de chèvre suspendues au plafond. L'une de ces
listes attire tout particulièrement votre attention : en voici le détail :
ÉPÉES 4 Couronnes pièce
POIGNARDS 2 Couronnes pièce
GLAIVES 6 Couronnes pièce
LANCES 5 Couronnes pièce
METS DÉLICATS 2 Couronnes par Repas
ANNEAUX D'OR 8 Couronnes pièce
COUVERTURES DE FOURRURE 3 Couronnes pièce
SACS À DOS 1 Couronne pièce
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous avez suffisamment d'argent pour cela, vous pourrez acheter ce qui vous plaira dans la liste ci-dessus."))
    buy_button("ÉPÉE", 4, key="epee", label="Acheter : Épée (4 Couronnes)")
    buy_button("POIGNARD", 2, key="poignard", label="Acheter : Poignard (2 Couronnes)")
    buy_button("GLAIVE", 6, key="glaive", label="Acheter : Glaive (6 Couronnes)")
    buy_button("LANCE", 5, key="lance", label="Acheter : Lance (5 Couronnes)")
    buy_button("REPAS", 2, key="repas", label="Acheter : Mets délicats, 1 Repas (2 Couronnes)")
    buy_button("ANNEAU D'OR", 8, key="anneau", label="Acheter : Anneau d'Or (8 Couronnes)")
    buy_button("COUVERTURE DE FOURRURE", 3, key="couverture", label="Acheter : Couverture de Fourrure (3 Couronnes)")
    buy_button("SAC À DOS", 1, key="sac", label="Acheter : Sac à Dos (1 Couronne)")

    st.write_stream(stream_text("Lorsque vous aurez modifié en conséquence votre Feuille d'Aventure, vous quitterez le magasin par une porte latérale en vous rendant au :"))
    st.page_link("tomes/tome2/page_245.py", label="245", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
