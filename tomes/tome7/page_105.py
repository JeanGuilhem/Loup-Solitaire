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

check_inventory(current_page_number=105, book=7)

fr_text = """
Vous vous précipitez vers votre compagnon et vous constatez
qu'il est encore en vie, malgré la quantité de sang qu'il a perdue.
Vous soignez sa blessure du mieux possible, mais il est très
grièvement atteint, et cela ne servira qu'à prolonger sa vie de
quelques minutes tout au plus. Vous lui faites part de votre quête
et de l'aide que vous avez trouvée auprès des Anciens Mages, puis
vous lui racontez votre voyage jusqu'à Herdos, à bord du
vaisseau de l'espace du Seigneur Paido. En entendant ce nom,
vous voyez son regard s'allumer. « Je m'appelle Kasin, dit-il dans
un souffle, le front trempé de sueur. Le Seigneur Paido est mon
frère. » Vous constatez en effet une ressemblance indéniable
entre les deux hommes : mêmes yeux de chat, même mâchoire
forte et carrée. « Je sais que je n'en ai plus pour longtemps,
Seigneur Kaï, mais je peux toutefois vous aider dans votre quête.
Écoutez-moi bien. Là-bas, derrière la tapisserie, vous trouverez
un passage secret qui mène directement au trône de Zahda. La
Pierre de la Sagesse de Herdos se trouve au-dessus du trône,
mais prenez garde, car Zahda l'a couplée à une Pierre du Mal
provenant du royaume de Naaros, dont il tire tout son pouvoir. Si
vous voulez réussir, il vous faudra d'abord détruire ce cristal
maléfique, ou bien vous en mourrez. Malheureusement, je ne
peux pas vous dire comment sortir de Kazan-Oud, car j'y suis
moi-même enfermé depuis fort longtemps, sans avoir pu trouver
une issue. Toutefois, si vous parvenez à regagner la plage,
rendez-vous à la vieille jetée en pierre ; c'est là que j'ai caché mon
bateau en arrivant, juste sous les marches... » A ce moment, vous
sentez la main de Kasin se crisper sur la vôtre, tandis qu'une
onde de douleur lui parcourt le corps. « ... Lorsque vous
retournerez à Elzian, reprend-il encore plus faiblement, dites à
mon frère que je ne suis pas mort pour rien... Que les dieux vous
protègent... Loup Solitaire ! » Sur ces derniers mots, les yeux de
Kasin se ferment définitivement, et vous faites le serment de
perpétuer sa mémoire dans le cœur des Vakeros, les illustres et
courageux guerriers dont il faisait partie.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("A présent, rendez-vous au :"))
    st.page_link("tomes/tome7/page_282.py", label="282", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
