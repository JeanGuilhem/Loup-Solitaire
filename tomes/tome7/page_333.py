import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    is_new_page,
    remove_from_inventory,
    show_illustrations,
    show_map,
)
from text import fr_unknown_magnakai
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=333, book=7)

fr_text = """
Vous introduisez la clé dans la minuscule serrure et vous sentez
un picotement dans les doigts. Vous entendez un bruissement,
comme un faible souffle de vent et vous lâchez la clé qui disparaît
rapidement. (Rayez cet Objet Spécial de votre Feuille
d'Aventure.) Sans bruit, la grande porte s'ouvre, et vous pénétrez
dans une pièce aux murs de pierre. La porte se referme derrière
vous et, en vous retournant, vous apercevez, profondément gravé
sur la surface, un serpent enroulé sur lui-même avec le chiffre
123 marqué sur ses écailles. Notez ce chiffre dans la marge de
votre Feuille d'Aventure, cela pourrait vous être utile
ultérieurement. Dans un râtelier suspendu près de la porte, vous
découvrez une lance et un bâton. Les deux armes sont en parfait
état malgré l'air chaud et humide. Au fond de la pièce, deux
tunnels éclairés par des torches descendent vers le nord et l'est.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        remove_from_inventory("CLÉ D'OR")
    st.info("La Clé d'Or a disparu : elle est rayée de vos Objets Spéciaux. Notez le chiffre 123, gravé sur le serpent.")
    # la lance et le bâton du râtelier : le texte ne dit pas qu'on peut les prendre

    st.write_stream(stream_text("Si vous souhaitez entrer dans le tunnel nord, rendez-vous au :"))
    st.page_link("tomes/tome7/page_187.py", label="187", icon="📄")
    st.write_stream(stream_text("Si vous préférez entrer dans le tunnel est, rendez-vous au :"))
    st.page_link("tomes/tome7/page_101.py", label="101", icon="📄")
    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de l'Exploration, rendez-vous au :"))
    if has_magnakai("Exploration"):
        st.page_link("tomes/tome7/page_139.py", label="139", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome7/page_139.py", label="139", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
