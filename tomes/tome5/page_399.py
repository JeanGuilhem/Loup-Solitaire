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

check_inventory(current_page_number=399, book=5)

fr_text = """
Banedon baisse son bâton, un pâle sourire désabusé se dessinant
sur son visage ravagé par la douleur. « Hélas, je n'ai pas été assez
vif pour me protéger, Loup Solitaire », dit-il en regardant son
bras. Vous posez un genou à terre et vous retirez la lance qui le
cloue au plancher. La blessure est sérieuse et vous vous hâtez de
déchirer son habit bleu sombre afin de confectionner un
pansement de fortune. Vous reconnaissez cet habit, car il s'agit
de celui des Maîtres de Voyage. Il semble que le jeune Banedon
soit monté en grade dans l'ordre des Magiciens depuis la
dernière fois où vous vous êtes rencontrés. « Décidément, nous
sommes condamnés à nous rencontrer en leur compagnie, dit-il
nerveusement tout en observant les Kraans et les Drakkars qui
les montent. Aide-moi à me relever, nous devons fuir avant qu'ils
ne nous obligent à gagner le sol. » Vous soutenez le magicien,
tandis qu'il saisit la barre du vaisseau: une sphère de cristal aux
mille facettes étincelantes, située à l'extrémité d'une mince tige
en argent. A peine a-t-il effleuré le cristal qu'une énorme
explosion retentit.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_323.py", label="323", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
