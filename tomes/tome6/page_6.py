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

check_inventory(current_page_number=6, book=6)

fr_text = """
« Calmez-vous mes frères ! C'est bien lui le Seigneur Kaï. » Au
fur et à mesure que les vieillards effarouchés se remettent de
leur émotion, la stupéfaction fait place à un respect mêlé de
crainte. « Mon nom est Gwynian, dit enfin leur chef. Nous
attendions votre arrivée. » Sur ces mots, il montre du doigt les
cartes étalées sur la table, ainsi qu'un gros télescope fixé sur
une plate-forme, juste sous le dôme du toit. «Les étoiles
prédisent les événements à venir et sont pour nous des
conseillères, reprend le vieil homme. Nous sommes au courant de
votre quête et nous savons que les sentiments qui guident vos pas
à la recherche de la Pierre de la Sagesse sont purs et droits.
Nous sommes prêts à vous aider, mais je dois vous avertir que
certains membres de notre confrérie redoutent les pouvoirs de
cette Pierre. Ces derniers ont préféré ne pas tenir compte de la
sagesse des étoiles, et ils ont fait le vœu - ô combien stupide et
dangereux ! - de ne révéler à personne l'emplacement de la Pierre
de la Sagesse et de tuer quiconque chercherait à s'en emparer, de
peur de la voir tomber aux mains de n'importe qui et par crainte
que son pouvoir ne soit utilisé à de tristes fins. » Soudain, les
paroles de Gwynian sont interrompues par une série de coups
frappés à la porte de l'observatoire : votre cheval a sans doute
été repéré ! « Livrez-nous cet homme ! » tonitrue un chœur de voix
en colère. «Vite, nous devons partir sans perdre une seconde ! »
chuchote Gwynian en vous poussant vers une petite pièce. Puis il
tire un petit loquet bien dissimulé, et une porte dérobée s'ouvre
soudain pour découvrir un étroit passage. Au moment où vous vous
engagez dans les ténèbres, sous la conduite du vieux sage et de
ses compagnons, la porte de l'observatoire cède et vole en éclats
sous la pression de vos poursuivants.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_158.py", label="158", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
