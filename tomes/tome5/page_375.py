import streamlit as st
from combat import combat
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

check_inventory(current_page_number=375, book=5)

fr_text = """
Des gouttes de sueur perlent sur les visages des Gardes tandis
qu'ils essaient de recharger fiévreusement leurs arbalètes. Votre
attaque audacieuse les a quelque peu découragés et la peur les
rend maladroits. Une fois en haut des marches, vous passez à
l'attaque, tel un tigre se jetant sur sa proie. Votre premier coup
fait tomber l'arbalète des mains tremblantes d'un des Gardes
tandis que le second coup lui démet la mâchoire. L'homme
tombe du pont en hurlant et va s'écraser dans les jardins en
contrebas. Pendant ce temps, l'autre Garde a jeté son arbalète et
a dégainé une lourde masse d'armes. Il se rue sur vous avec des
éclairs de haine dans les yeux : le Garde que vous venez de tuer
était son frère et il a soif de revanche ! La fureur qui l'anime le
rend insensible à tout pouvoir psychique.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("GARDE DE LA TOUR", 17, 22)], psychic_immune=True)
    if outcome == "win":
        st.write_stream(stream_text("Si vous remportez le combat, vous pouvez entrer dans la tour, rendez-vous alors au :"))
        st.page_link("tomes/tome5/page_396.py", label="396", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
