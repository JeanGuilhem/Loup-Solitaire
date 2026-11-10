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

check_inventory(current_page_number=133, book=7)

fr_text = """
Vous exercez rapidement votre Science Médicale pour sauver la
vie de votre compagnon, concentrant tout votre pouvoir sur les
plaies qui déforment son visage et déchirent sa gorge. Vous
parvenez à arrêter l'hémorragie et vous sentez le cœur du blessé
battre plus régulièrement. Hélas, ce n'est qu'un bref répit, car
l'homme a la colonne vertébrale brisée, et vous savez que vous ne
pouvez rien faire de plus pour lui ; dans cette sinistre forteresse,
il ne survivra pas longtemps à une telle blessure. L'espace de
quelques instants, il reprend conscience et s'efforce d'articuler
quelques mots : « Attention au dédale, Homme du Nord... Le
vert... c'est... la mort... » Sur ces paroles énigmatiques, ses yeux
se ferment et il sombre dans un sommeil sans retour. Ainsi que le
veut la coutume dans son pays, vous posez son épée sur sa
poitrine, signifiant ainsi qu'un brave guerrier est tombé au
champ de bataille.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez abandonner là le corps de votre infortuné compagnon puis continuer votre chemin, rendez-vous au :"))
    st.page_link("tomes/tome7/page_323.py", label="323", icon="📄")

    st.write_stream(stream_text("Si vous préférez fouiller rapidement son corps avant de partir, rendez-vous au :"))
    st.page_link("tomes/tome7/page_227.py", label="227", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
