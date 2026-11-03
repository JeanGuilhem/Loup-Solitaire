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

check_inventory(current_page_number=37, book=4)

fr_text = """
Vous faites signe au conducteur de la roulotte de tête de s'arrêter.
La caravane s'immobilise bientôt et un petit homme au visage
lunaire, vêtu d'une tunique rose vif ouvre à la volée la porte
arrière de la roulotte. Descendant du véhicule, il se met à hurler
en injuriant le conducteur et ne consent à s'interrompre que pour
rajuster la large ceinture qui entoure son énorme ventre. Puis,
voyant vos hommes, il laisse alors échapper un cri étranglé et,
d'un geste précipité, saisit la poignée d'un sabre qui pend à sa
ceinture. « Des brigands ! des voleurs ! » s'écrie-t-il en s'efforçant
d'arracher le sabre à son fourreau ouvragé. Des visages inquiets
apparaissent aux fenêtres de la roulotte, mais leur expression se
change bientôt en un sourire. Les voyageurs ont reconnu les
uniformes du Sommerlund. « Calme-toi, Yesu, crie une vieille
femme, ce sont des patrouilleurs sommerlundais. Ils ne te
voleront pas ton or. » Des éclats de rire retentissent dans toutes
les roulottes lorsque le petit homme gras dégaine soudain son
sabre avec tant de force qu'il tourne sur lui-même, puis trébuche
et tombe sur le sol. « Il faut pardonner à Yesu, vous dit la vieille
femme, il ne vous veut aucun mal, c'est la Contrée des Pillards
qui le rend aussi nerveux. » Vous demandez à la vieille femme
d'où ils viennent et où ils se rendent. Elle vous apprend alors que
la caravane transporte une troupe de musiciens et d'acteurs qui
ont voyagé longtemps, quittant leur terre natale de Clœasia à l'est
pour donner une série de représentations. Leur dernier spectacle
s'est déroulé à Eshnar, mais il fut décevant : la ville en effet
semblait aussi silencieuse qu'un tombeau et les habitants venus
les entendre avaient l'air triste et découragé. Les musiciens se
rendent à présent à Holmgard en espérant y trouver un public
plus enthousiaste. « La nuit tombe, fait remarquer la vieille
femme, peut-être accepterez-vous de camper avec nous en
compagnie de vos hommes ? Ce serait pour nous un honneur et
nous serions heureux de vous distraire en vous proposant des
chants, des danses et du théâtre. » Vous remarquez aussitôt une
lueur d'espoir dans le regard de vos hommes qui attendent avec
impatience votre décision.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez camper avec les troubadours, rendez-vous au :"))
    st.page_link("tomes/tome4/page_182.py", label="182", icon="📄")

    st.write_stream(stream_text("Si vous préférez continuer en direction de Ruanon, rendez-vous au :"))
    st.page_link("tomes/tome4/page_247.py", label="247", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
