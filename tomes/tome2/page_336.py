import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=336, book=2)

fr_text = """
En une fraction de seconde, l'éclair change de direction, attiré par le
Glaive de Sommer qui en absorbe aussitôt l'énergie aussi facilement
qu'une éponge absorbe une goutte d'eau. C'est là un des pouvoirs du
Glaive, comme vous l'avez appris au cours de votre entraînement : il
vous protège de toute magie et vient ainsi de vous épargner une mort
certaine. Le sorcier lance alors un juron, arrache une pierre précieuse de
son turban richement orné et la jette à vos pieds. Une flamme en jaillit
instantanément et un nuage vert s'élève vers vous : c'est un gaz puissant
dont l'odeur acide vous fait suffoquer. Pour échapper à ce gaz délétère,
vous êtes contraint de sauter sur le pont et le sorcier profite de cette
diversion pour s'enfuir du vaisseau fantôme à bord d'un canot dont il
actionne les rames avec une véritable frénésie.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez vous aussi quitter le vaisseau fantôme en plongeant dans la mer, rendez-vous au :"))
    st.page_link("tomes/tome2/page_109.py", label="109", icon="📄")
    st.write_stream(stream_text("Si vous préférez essayer de rejoindre un navire de la flotte de Durenor au prix de quelques combats, rendez-vous au :"))
    st.page_link("tomes/tome2/page_185.py", label="185", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
