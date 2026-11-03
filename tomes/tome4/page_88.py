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

check_inventory(current_page_number=88, book=4)

fr_text = """
Une odeur fétide vous monte aux narines en vous donnant des
haut-le-cœur et en vous étouffant à moitié. Vous vous protégez la
bouche et le nez, puis vous faites un pas en arrière en
brandissant votre arme, prêt à frapper la créature qui ondule
vers vous à une allure impressionnante. Vos hommes portent des
coups d'épée à ses mâchoires grandes ouvertes, mais leurs lames
ne font qu'égratigner la peau grise et luisante du monstre avant
que celui-ci les avale vivants. Le Ver de Pierre poursuit
inexorablement son avance et il est bientôt sur vous : impossible
de vous échapper, vous devrez le combattre jusqu'à la mort de
l'un de vous deux. Cette créature est invulnérable à la Discipline
Kaï de la Puissance Psychique.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("VER DE PIERRE", 15, 38)], psychic_immune=True)
    if outcome == "win":
        st.write_stream(stream_text("Si vous remportez la victoire, rendez-vous au :"))
        st.page_link("tomes/tome4/page_321.py", label="321", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
