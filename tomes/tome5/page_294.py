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

check_inventory(current_page_number=294, book=5)

fr_text = """
Vous apercevez le jeune magicien qui abaisse son bâton, un pâle
sourire éclairant son visage marqué par la douleur. « Hélas, je
n'ai pas été assez vif pour me protéger également », dit-il d'une
voix lasse tandis que vous vous agenouillez à côté de lui et que
vous arrachez la lance qui le cloue au sol. La blessure est sérieuse
et vous vous empressez de la panser avec des bouts de tissu
arrachés à son habit bleu foncé. C'est alors que le sorcier se
présente. « Je m'appelle Banedon, chef d'expédition de la guilde
de l'Étoile de Cristal, dit-il d'une voix faible et tremblante. Quant
à vous, vous n'avez pas besoin de vous présenter, Loup Solitaire,
car vous êtes le seul à pouvoir attirer de telles créatures si loin de
chez elles. » Puis il regarde, tout autour du vaisseau du ciel, les
cavaliers qui chevauchent les Kraans. « Aidez-moi à me relever.
Nous devons fuir avant qu'ils ne nous forcent à atterrir. » Vous
soulevez le sorcier qui s'empare aussitôt du gouvernail du
bateau : une sphère de cristal étincelante aux multiples facettes,
plantée au bout d'une mince baguette d'argent. A peine sa main
a-t-elle effleuré le cristal qu'il se produit une immense explosion.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_323.py", label="323", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
