import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=167, book=3)

fr_text = """
Le vent tombe peu à peu, l'atmosphère s'éclaircit et le Glacier de
Viad se révèle alors dans toute sa splendeur. La surface lisse de la
glace ressemble à un tapis de neige étincelante incrustée de
pierres de toutes les couleurs : jaunes, violettes, bleues, vertes,
orange, cramoisies ; et les cristaux de glace brillent d'un tel éclat
que le plus somptueux bijou paraîtrait terne par comparaison. Le
mur de glace s'élève à 250 mètres de hauteur et ne présente pas
d'obstacle à l'escalade, bien qu'il soit très escarpé. Le temps est
beau, mais il vous faut presque une journée entière pour grimper
au sommet de la paroi de glace. Tout le matériel a été déchargé et
monté là-haut où on l'arrime à nouveau sur les traîneaux. Les
chiens Kanu jouent entre eux en se battant, et vos provisions
sont à tel point secouées par l'escalade qu'elles se sont
transformées à la fin de la journée en une infâme bouillie.
Lorsque tout est enfin terminé, vous êtes épuisé. La nuit tombe
et vous décidez donc d'établir votre campement dans l'abri que
vous offre une cuvette naturelle creusée dans la glace.
Vous avez sans nul doute bien mérité une bonne nuit de repos.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Utilisez la Table de Hasard pour obtenir un chiffre.'))
    roll = hazard_roll()
    if roll is not None and roll <= 6:
        st.write_stream(stream_text('Si vous tirez un chiffre de 0 à 6, rendez-vous au :'))
        st.page_link("tomes/tome3/page_85.py", label="85", icon="📄")
    elif roll is not None:
        st.write_stream(stream_text('De 7 à 9, rendez-vous au :'))
        st.page_link("tomes/tome3/page_300.py", label="300", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
