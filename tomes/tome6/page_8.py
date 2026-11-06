import streamlit as st
from inventory import (
    add_to_inventory,
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    is_new_page,
    pickup_button,
    pickup_gold,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=8, book=6)

fr_text = """
Chanda étouffe un cri et tressaille au moment où vous lui portez
le coup de grâce. Dans un ultime accès de rage et de désespoir, il
tente de vous maudire, mais les mots lui restent dans la gorge et
il s'effondre, raide mort, à vos pieds. Vous retournez son corps
de la pointe de votre botte et vous le fouillez rapidement. Vous
découvrez sur lui 10 Pièces d'Or, un flacon de Potion de Laumspur
(il y en a suffisamment pour vous faire récupérer 3 points
d'ENDURANCE), ainsi qu'un plan de Varetta. (Inscrivez cette carte
dans la case Objets Spéciaux de votre Feuille d'Aventure, et
rangez-la soigneusement dans votre Sac à Dos.) Emportez également,
si vous le désirez, les autres objets trouvés sur la dépouille du
taxidermiste (Pièces d'Or et Potion de Laumspur), puis
dépêchez-vous de quitter cet endroit malsain.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page() and not has_item("PLAN DE VARETTA"):
        add_to_inventory("PLAN DE VARETTA")
    st.success("Le Plan de Varetta a été inscrit dans vos Objets Spéciaux.")
    pickup_gold(10, key="or_chanda")
    pickup_button("FLACON DE LAUMSPUR", key="laumspur", label="Prendre la Potion de Laumspur (3 points d'ENDURANCE)")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_16.py", label="16", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
