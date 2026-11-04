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

check_inventory(current_page_number=336, book=5)

fr_text = """
Debout sur une plate-forme fortifiée située au centre de l'étrange
vaisseau se tient un jeune homme blond aux yeux perçants. Vous
le reconnaissez immédiatement : c'est Banedon, le jeune
magicien Sommerlundois qui vous avait donné le Pendentif à
l'Étoile de Cristal dans les ruines de Raumas, lorsque vous lui
aviez vous-même sauvé la vie lors d'une embuscade dressée par
des Giaks. Vous êtes tellement ébahi de le retrouver en cet
endroit que vous ne remarquez pas qu'un filet de sang s'écoule
du bec de votre Itikar. La créature est agonisante et pousse
soudain un ultime et pitoyable gémissement. Ses ailes se
raidissent et sa tête tombe mollement sur le côté après un
dernier sursaut. Vous basculez dans le vide et votre estomac se
tord tandis que vous tombez comme une pierre vers le lac Inrahim.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Utilisez la Table de Hasard pour obtenir un chiffre.'))
    roll = hazard_roll(key='hazard')
    if roll is not None:
        if 0 <= roll <= 4:
            st.write_stream(stream_text('Si vous avez tiré un chiffre compris entre 0 et 4, rendez-vous au :'))
            st.page_link("tomes/tome5/page_374.py", label="374", icon="📄")
        elif 5 <= roll <= 8:
            st.write_stream(stream_text('Si vous avez tiré un chiffre compris entre 5 et 8, rendez-vous au :'))
            st.page_link("tomes/tome5/page_254.py", label="254", icon="📄")
        elif 9 <= roll <= 9:
            st.write_stream(stream_text('Si vous avez tiré un 9, rendez-vous au :'))
            st.page_link("tomes/tome5/page_261.py", label="261", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
