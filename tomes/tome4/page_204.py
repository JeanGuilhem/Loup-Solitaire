import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, handle_repas, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=204, book=4)

fr_text = """
Vous contournez un village aux maisonnettes de bois orange et
vous traversez les champs en direction d'une éminence boisée.
Au-delà de ce monticule, vous pénétrez dans une forêt dense et
vous découvrez bientôt un ruisseau d'eau fraîche et
bouillonnante. Vous vous désaltérez longuement et vous vous
rendez compte alors que vous êtes affamé. Il vous faut prendre
immédiatement un Repas sinon vous perdrez 3 points
d'ENDURANCE. A la nuit tombée, vous parvenez dans la ville de
Maaken. Les ruines sinistres et envahies de mauvaises herbes de
cette cité fantôme s'étendent comme un vaste cimetière baigné
de la clarté lugubre d'une lune bientôt pleine. Un long
gémissement retentit comme la plainte d'âmes errantes et
désespérées : c'est le cri des gorges de Maaken. Vous n'avez pas
dormi depuis presque deux jours et la fatigue vous submerge.
Ramenant votre cape de Guerrier Kaï autour de vos épaules, vous
vous allongez donc pour prendre quelques heures de repos. Vous
aurez besoin, en effet, de toutes vos forces pour mener à bien la
tâche terrifiante qui vous attend.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    handle_repas()

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_142.py", label="142", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
