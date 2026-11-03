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

check_inventory(current_page_number=312, book=4)

fr_text = """
Tout autour de vous, les ruines résonnent du fracas des armes et
des cris de guerre. Ces cavaliers vêtus d'armures ne sont pas des
brigands ordinaires ; ils combattent avec une discipline et une
habileté dont ne sont pas coutumiers les hors-la-loi du Pays
Sauvage.
Vous enjambez le cadavre du Guerrier et vous rassemblez vos
hommes. L'ennemi a encerclé vos chevaux et il vous faut agir vite
si vous voulez l'empêcher de vous les voler. Vous menez une
charge parmi les ruines, et vous repoussez vos agresseurs qui
s'enfuient en déroute dans l'obscurité. Cependant, lorsque vous
atteignez l'extrémité du temple, vous vous apercevez qu'il ne
vous reste plus que onze chevaux. Les autres ont disparu. Après
avoir mûrement réfléchi, vous décidez de prendre dix
patrouilleurs avec vous pour continuer votre expédition et de
renvoyer les autres à Holmgard avec mission de rapporter au roi
ce qui s'est passé. Tandis que la faible lueur de l'aube se répand
peu à peu dans le ciel, vos dix compagnons et vous-même
adressez un triste adieu à ceux qui vont devoir retourner à pied
dans la capitale pour avertir le monarque.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre."))
    roll = hazard_roll()
    if roll is not None:
        if roll <= 2:
            st.write_stream(stream_text("Si vous tirez un chiffre de 0 à 2, rendez-vous au :"))
            st.page_link("tomes/tome4/page_120.py", label="120", icon="📄")
        else:
            st.write_stream(stream_text("De 3 à 9, rendez-vous au :"))
            st.page_link("tomes/tome4/page_51.py", label="51", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
