import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=252, book=3)

fr_text = """
« Ton heure est venue ! » crie une voix, mais c'est celle de Loi-Kymar
et non celle de Vonotar. Une touffe d'herbes jetée dans les
airs vient frapper le mage félon en pleine poitrine. Un instant
plus tard, l'infâme traître bossu se trouve empêtré dans un
enchevêtrement de plantes qui l'emprisonnent de la tête aux
pieds. Loi-Kymar parvient à son tour à franchir le fossé et vous
rejoint sur la plate-forme. « Prenez soin de lui ôter ses bagues et
ses amulettes, recommande-t-il tout en cherchant sa Crosse de la
Guilde, car c'est un maître en matière de fourberie, et ce serait
dommage qu'il manque la petite fête de bienvenue que le
Sommerlund lui réserve pour son retour. Le sang-froid du vieil
homme vous émerveille : ce terrible affrontement, en effet, ne lui
a pas fait perdre son calme. « Ah ! la voici ! » annonce-t-il d'un
ton triomphal en trouvant sous le Trône du Brumalmarc sa
Crosse de la Guilde. Vous lui montrez alors votre carte de Kalte
en lui indiquant l'endroit où est ancré le Cardonal. « Je n'ai pas
besoin de cela, répond-il avec une nuance de mépris, les cartes
sont toujours fausses et je préfère m'en remettre à mon propre
sens de l'orientation. » Le vieux magicien lève alors sa Crosse et
un rayon aveuglant jaillit aussitôt de son extrémité. Il décrit
ensuite trois larges cercles dans les airs et la salle du Trône du
Brumalmarc se transforme instantanément en un kaléidoscope
aux multiples couleurs.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_350.py", label="350", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
