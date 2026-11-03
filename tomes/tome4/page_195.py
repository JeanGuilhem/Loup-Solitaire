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

check_inventory(current_page_number=195, book=4)

fr_text = """
Quelqu'un déverrouille la porte qui, à en juger par le bruit, doit
être fermée à l'aide d'une lourde barre de fer. Un homme
d'aspect robuste, vêtu d'une tunique de cuir apparaît à l'entrée de
la taverne. « Bienvenue dans ma modeste auberge, Seigneur Kaï,
dit-il, pardonnez ma méfiance, mais la région est très dangereuse
et la moindre erreur pourrait nous coûter la vie. » Vous faites
signe à vos hommes d'emmener leurs chevaux à l'écurie et vous
suivez le tenancier de la taverne. A l'intérieur, la salle ressemble
davantage à une armurerie qu'à une auberge. Des carquois
remplis d'arcs sont posés devant chaque fenêtre fermée par des
volets cloutés de fer, et des lances sont alignées contre le mur du
fond. Il n'y a dans la salle que trois hommes jeunes qui ont
chacun un air de ressemblance très prononcé avec le tenancier.
L'un de ces jeunes gens a la tête entourée de bandages. Vous
demandez à l'homme qui vous a ouvert le prix qu'il vous en
coûtera pour passer la nuit ici en compagnie de vos patrouilleurs.
« Ce sera gratuit », répond-il à votre grande surprise. Il déplace
alors les tables pour que vos soldats puissent s'installer sur le
plancher. « Votre présence ici cette nuit, poursuit-il, a beaucoup
plus de valeur pour nous que des Pièces d'Or. Nous subissons en
effet des attaques incessantes de brigands depuis la dernière
pleine lune. » Dès que le dernier de vos hommes est revenu des
écuries, les portes sont à nouveau fermées et verrouillées. Il a
commencé à pleuvoir et vos patrouilleurs semblent
singulièrement soulagés de se trouver à l'abri, au chaud et au sec.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez interroger le tenancier de la taverne au sujet des attaques de brigands, rendez-vous au :'))
    st.page_link("tomes/tome4/page_239.py", label="239", icon="📄")

    st.write_stream(stream_text("Si vous préférez lui demander s'il a eu des nouvelles en provenance de Ruanon, au cours du mois dernier, rendez-vous au :"))
    st.page_link("tomes/tome4/page_266.py", label="266", icon="📄")

    st.write_stream(stream_text("Enfin, si vous n'estimez pas nécessaire de poser d'autres questions à cet homme, préparez-vous à une nuit de sommeil en vous rendant au :"))
    st.page_link("tomes/tome4/page_324.py", label="324", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
