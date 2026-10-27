import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=26, book=2)

fr_text = """
Vous contemplez les orbites vides d'un cadavre ambulant. Mais
quelque défiguré qu'il soit, vous reconnaissez le visage du capitaine
Kelman. Vous vous trouvez en fait sur le pont du Sceptre Vert qui a
sombré vingt-quatre jours plus tôt au cours de la tempête. Le matin
même, l'épave du navire a été arrachée aux profondeurs obscures de la
mer et sa carcasse ira rejoindre la flotte des bateaux fantômes. Le
capitaine zombie tend vers vous une main aux doigts brisés et vous
supplie, d'une voix d'outre-tombe, de déposer sur le pont du navire le
Glaive de Sommer : « Déposez l'épée à vos pieds et mon âme alors
échappera à son tourment. »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez accéder à sa demande, rendez-vous au :"))
    st.page_link("tomes/tome2/page_248.py", label="248", icon="📄")
    st.write_stream(stream_text("Si vous préférez attaquer le capitaine, rendez-vous au :"))
    st.page_link("tomes/tome2/page_66.py", label="66", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
