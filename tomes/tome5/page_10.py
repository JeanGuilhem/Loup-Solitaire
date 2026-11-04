import streamlit as st
from inventory import (
    check_inventory,
    confiscate_equipment,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=10, book=5)

fr_text = """
Les Sharnazims vous encerclent et vous remettent brutalement
debout. Puis, ils s'emparent de votre Sac à Dos et vous délestent
de vos armes, de vos Objets Spéciaux et de vos Pièces d'Or
(inscrivez toutes les modifications sur votre Feuille d'Aventure).
On vous attache les mains avec une corde et l'on vous traîne de
force vers la Grand-Place où un attelage vous attend.
Vous êtes jeté dans la voiture et Maouk y grimpe à son tour,
savourant son triomphe. Puis il crie au cocher : « Au Grand
Palais, vite ! Le Zakhan attend son prisonnier avec impatience ! »
Vous luttez désespérément pour vous libérer de la corde qui
entaille douloureusement vos poignets, mais Maouk ne tarde pas
à s'apercevoir de votre manœuvre : il vous saisit violemment par
le bras et vous enfonce une aiguille dans la chair. Une sensation
de torpeur vous envahit et vous entendez résonner à vos oreilles
le rire sarcastique de Maouk lorsque vous sombrez dans
l'inconscience.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        confiscate_equipment()
    st.warning("Les Sharnazims vous ont pris votre Sac à Dos, vos armes, vos Objets Spéciaux et vos Pièces d'Or.")

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome5/page_69.py", label="69", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
