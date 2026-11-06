import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    sell_button,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=76, book=6)

fr_text = """
Le propriétaire de l'Auberge des Épées Croisées a l'habitude de
jeter dehors, sans ménagement, ceux qui n'ont pas les moyens de
payer. Vous voici donc dans une bien fâcheuse situation, puisque
vous n'avez plus un sou en poche et que l'on a sonné le
couvre-feu depuis une heure. Et vous savez que tout homme se
trouvant dans les rues passé ce délai est passible
d'emprisonnement immédiat s'il est pris par le guet. Par
conséquent, plutôt que de prendre un tel risque et mettre en
péril le succès de votre quête, mieux vaut vendre quelques-uns
de vos objets personnels afin d'avoir l'argent nécessaire pour
passer la nuit à l'auberge. Le mercenaire bedonnant, celui qui
avait pris les paris et empoché votre mise, se déclare prêt à
vous acheter certains articles de la liste ci-dessous (et
uniquement ceux-ci), au prix suivant :
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # le mercenaire n'achète que les articles de sa liste
    sell_button("ÉPÉE", 3, key="t6_76_0")
    sell_button("POIGNARD", 1, key="t6_76_1")
    sell_button("GLAIVE", 6, key="t6_76_2")
    sell_button("SABRE", 2, key="t6_76_3")
    sell_button("MASSE D'ARMES", 3, key="t6_76_4")
    sell_button("BAGUE EN RUBIS", 10, key="t6_76_5")
    sell_button("MARTEAU DE GUERRE", 5, key="t6_76_6")
    sell_button("LANCE", 4, key="t6_76_7")
    sell_button("HACHE", 2, key="t6_76_8")
    sell_button("ARC", 5, key="t6_76_9")
    sell_button("BÂTON", 2, key="t6_76_10")
    sell_button("BROCHE EN ARGENT", 7, key="t6_76_11")

    st.write_stream(stream_text("Il vous faut, au minimum, 2 Pièces d'Or pour passer une nuit à l'Auberge des Épées Croisées. Si vous voulez vendre une partie de votre équipement, effectuez les modifications qui s'imposent sur votre Feuille d'Aventure, puis rendez-vous au :"))
    st.page_link("tomes/tome6/page_336.py", label="336", icon="📄", disabled=st.session_state.purse < 2)

    st.write_stream(stream_text("Si vous ne désirez pas vous séparer de quoi que ce soit, ou si le mercenaire ne trouve rien d'intéressant parmi ce que vous lui proposez, alors vous devez partir à vos risques et périls à travers les rues de la ville, en espérant que le guet ne vous prendra pas... Rendez-vous alors au :"))
    st.page_link("tomes/tome6/page_138.py", label="138", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
