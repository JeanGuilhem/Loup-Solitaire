import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=323, book=5)

fr_text = """
L'explosion est suivie d'un énorme nuage de fumée qui envahit la
cabine située à l'arrière du pont. Tandis que le bruit de la
détonation retentit à travers la plaine de sel désolée, vous
percevez le cri d'agonie d'un Kraan blessé qui tombe en
tourbillonnant. L'une de ses ailes est percée d'un large trou. La
fumée se disperse peu à peu et laisse apparaître le visage
grimaçant d'un Nain au hublot de la cabine. Des traces de suie
noircissent ses joues rubicondes et accentuent la blancheur de
ses dents. Le Nain tient un tube de métal encore fumant, que
vous prenez de prime abord pour un bâton magique. Puis vous
remarquez que chaque membre de l'équipage est muni d'une
arme identique. Les étranges tubes crachent feu et flammes en
direction des Kraans et c'est alors que vous identifiez ces armes
ainsi que leurs utilisateurs: ce sont les Nains du royaume
montagneux de Bor. Ceux-ci sont célèbres à travers tout le
Magnamund pour leurs ingénieuses inventions, et notamment
pour ces redoutables armes, que vous voyez pour la première fois
en action. Les Kraans sont affolés par le bruit et s'enfuient à tire-
d'aile sans que les Drakkars puissent les retenir. L'ancêtre du
fusil n'a fait qu'une seule victime, mais l'effet de dissuasion n'en
est pas moins efficace ! La déroute des assaillants vient de sauver
le vaisseau de l'espace de la catastrophe. Banedon reprend le
gouvernail et redresse rapidement le vaisseau jusqu'à ce qu'il se
trouve en face des cimes assombries des montagnes du sud et de
la faille caractéristique marquant l'entrée du passage du Dahir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Utilisez la Table de Hasard pour obtenir un chiffre.'))
    roll = hazard_roll(key='hazard')
    if roll is not None:
        if 0 <= roll <= 2:
            st.write_stream(stream_text('Si vous avez tiré un chiffre compris entre 0 et 2, rendez-vous au :'))
            st.page_link("tomes/tome5/page_250.py", label="250", icon="📄")
        elif 3 <= roll <= 9:
            st.write_stream(stream_text('Si vous avez tiré un chiffre compris entre 3 et 9, rendez-vous au :'))
            st.page_link("tomes/tome5/page_312.py", label="312", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
