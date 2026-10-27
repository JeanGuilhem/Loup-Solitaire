import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=120, book=2)

fr_text = """
La chance est avec vous ; vous atterrissez en effet sans dommage sur le
pont du Kalkarm, un vaisseau de guerre de la flotte de Durenor. Les
marins y ont livré un rude combat dont ils sont sortis vainqueurs et ils
sont occupés pour le moment à détacher les grappins que leur avait
lancés l'un des bateaux fantômes. Emergeant d'un nuage de fumée,
Lord Axim apparaît ; son visage est ensanglanté et son bouclier porte la
trace de coups violents. « Dieu merci, vous êtes vivant, Loup Solitaire.
La bataille a été sans merci et nos pertes sont élevées, mais de vous voir
debout devant moi me met quelque baume au cœur », dit-il en vous
prenant par le bras pour vous emmener près du bastingage. « Regardez
là-bas, poursuit-il, leur vaisseau amiral est en feu. » A travers la brume
noirâtre provoquée par la bataille, vous distinguez l'énorme vaisseau
fantôme qui sombre sous un panache d'épaisse fumée. Pendant ce
temps les marins du Kalkarm ont réussi à détacher leur navire du
bateau fantôme qui les avait abordés et à l'éloigner des débris
parsemant la mer alentour. Un vent se lève qui enfle les voiles
déchirées et dissipe la fumée des combats. Lord Axim ordonne bientôt
que soit hissé le pavillon aux Armes Royales de Durenor afin que les
autres navires rescapés puissent rallier le Kalkarm. Pour la première
fois depuis le début de la bataille, vous pouvez distinguer les autres
navires de la flotte de Durenor et une vision stupéfiante s'offre alors à
vous car, à présent que le vaisseau amiral de la flotte ennemie a sombré
dans les flots, tous les autres bateaux fantômes retournent au fond de la
mer d'où les avait tirés la magie des Maîtres des Ténèbres. « Le charme
est rompu, dit Lord Axim, et nous avons remporté la victoire. »
Quelques minutes plus tard, il ne reste plus un seul vaisseau fantôme à
la surface de la mer.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_225.py", label="225", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
