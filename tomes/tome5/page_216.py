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

check_inventory(current_page_number=216, book=5)

fr_text = """
Vous arrivez bientôt dans un jardin public où se trouve
rassemblée une petite foule autour d'une fontaine en ruine. Les
membres de l'auditoire écoutent le discours passionné d'un
homme vêtu de rouge des pieds à la tête. Ils portent tous un
foulard de la même couleur qui leur recouvre le bas du visage. «
Ce sont des Adu-Kaw, les voilés, dit Banedon nerveusement. Il
semble qu'ils soient en train de déclarer la guerre à leurs
ennemis de toujours : les hommes de Tefa. » Puis Badenon et
vous allez vous mettre à l'ombre d'un Toab, où vous pourrez
écouter discrètement la suite du discours. L'orateur dénonce à
présent les abus des Tefarims, qui réclament des droits de
passage exorbitants pour pouvoir traverser leur ville sans
incident et emprunter la grande voie menant à Kara Kala. Peu à
peu, les discours de l'homme amènent les spectateurs au
paroxysme de leur agitation. Soudain, l'homme vêtu de rouge
montre du doigt l'endroit où vous vous trouvez et s'écrie: «
Regardez : des espions Tefarims ! »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez tenter de raisonner cette bande de fanatiques qui s'avance vers vous, l'arme au poing, rendez-vous au :"))
    st.page_link("tomes/tome5/page_284.py", label="284", icon="📄")

    st.write_stream(stream_text("Si vous préférez suivre l'exemple de Banedon et vous enfuir à toutes jambes, rendez-vous au :"))
    st.page_link("tomes/tome5/page_340.py", label="340", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
