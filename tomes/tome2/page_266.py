import streamlit as st
from inventory import (
    buy_button,
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    sell_button,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=266, book=2)

fr_text = """
A votre entrée, une cloche retentit et un petit homme vêtu d'une veste
de cuir matelassée vous souhaite la bienvenue. Il est occupé à frotter
une armure rouillée à l'aide d'un tampon de paille de fer. Un petit
tableau de bois posé sur le comptoir indique le prix de chacune des
armes exposées :
ÉPÉES 4 Couronnes pièce
POIGNARDS 2 Couronnes pièce
GLAIVES 7 Couronnes pièce
SABRES 3 Couronnes pièce
MARTEAUX DE GUERRE 6 Couronnes pièce
LANCES 5 Couronnes pièce
MASSES D'ARMES 4 Couronnes pièce
HACHES 3 Couronnes pièce
BÂTONS 3 Couronnes pièce
Si vous possédez l'argent nécessaire, vous pouvez acheter l'une ou
l'autre de ces armes; et si vous souhaitez vendre une arme dont vous
voulez vous séparer, l'armurier vous l'achètera au prix indiqué sur son
tableau, moins 1 Couronne. Si vous désirez lui vendre une Masse
d'Armes par exemple, il vous en donnera 4-1 = 3 Couronnes.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write("**Acheter une arme :**")
    buy_button('ÉPÉE', 4, key="buy_épée", label="Acheter : Épée (4 Couronnes)")
    buy_button('POIGNARD', 2, key="buy_poignard", label="Acheter : Poignard (2 Couronnes)")
    buy_button('GLAIVE', 7, key="buy_glaive", label="Acheter : Glaive (7 Couronnes)")
    buy_button('SABRE', 3, key="buy_sabre", label="Acheter : Sabre (3 Couronnes)")
    buy_button('MARTEAU DE GUERRE', 6, key="buy_marteau_de_guerre", label="Acheter : Marteau de Guerre (6 Couronnes)")
    buy_button('LANCE', 5, key="buy_lance", label="Acheter : Lance (5 Couronnes)")
    buy_button("MASSE D'ARMES", 4, key="buy_masse_d_armes", label="Acheter : Masse d'Armes (4 Couronnes)")
    buy_button('HACHE', 3, key="buy_hache", label="Acheter : Hache (3 Couronnes)")
    buy_button('BÂTON', 3, key="buy_bâton", label="Acheter : Bâton (3 Couronnes)")
    st.write("**Vendre une arme (prix indiqué moins 1 Couronne) :**")
    if has_item('ÉPÉE'):
        sell_button('ÉPÉE', 3, key="sell_épée", label="Vendre : Épée (3 Couronnes)")
    if has_item('POIGNARD'):
        sell_button('POIGNARD', 1, key="sell_poignard", label="Vendre : Poignard (1 Couronnes)")
    if has_item('GLAIVE'):
        sell_button('GLAIVE', 6, key="sell_glaive", label="Vendre : Glaive (6 Couronnes)")
    if has_item('SABRE'):
        sell_button('SABRE', 2, key="sell_sabre", label="Vendre : Sabre (2 Couronnes)")
    if has_item('MARTEAU DE GUERRE'):
        sell_button('MARTEAU DE GUERRE', 5, key="sell_marteau_de_guerre", label="Vendre : Marteau de Guerre (5 Couronnes)")
    if has_item('LANCE'):
        sell_button('LANCE', 4, key="sell_lance", label="Vendre : Lance (4 Couronnes)")
    if has_item("MASSE D'ARMES"):
        sell_button("MASSE D'ARMES", 3, key="sell_masse_d_armes", label="Vendre : Masse d'Armes (3 Couronnes)")
    if has_item('HACHE'):
        sell_button('HACHE', 2, key="sell_hache", label="Vendre : Hache (2 Couronnes)")
    if has_item('BÂTON'):
        sell_button('BÂTON', 2, key="sell_bâton", label="Vendre : Bâton (2 Couronnes)")

    st.write_stream(stream_text("Apportez à votre Feuille d'Aventure toutes les modifications nécessaires en fonction de vos transactions, puis quittez la boutique après avoir souhaité une bonne nuit au petit homme. Au bout de la rue du Col Vert se trouvent à votre droite une grande écurie et un relais de diligence. Il fait noir à présent et il vous faut un abri pour la nuit. Vous apercevez alors une échelle, à l'extérieur du bâtiment ; vous y grimpez et vous arrivez dans un grenier à foin où vous pourrez vous installer confortablement et dormir jusqu'au lendemain. Rendez-vous au :"))
    st.page_link("tomes/tome2/page_32.py", label="32", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
