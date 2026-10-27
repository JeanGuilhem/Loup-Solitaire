import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=113, book=2)

fr_text = """
Lorsque Banedon vous a donné le Pendentif à l'Etoile de Cristal, il vous
a parlé de cet homme : c'est Vonotar le Traître - un sorcier renégat de la
Guilde des Magiciens de Toran. Il est passé maître dans l'art de la
magie noire et les Maîtres des Ténèbres en personne l'ont investi d'un
grand pouvoir. Ce sont ses agents qui ont essayé de vous tuer au cours
de votre mission et c'est lui qui commande la flotte des vaisseaux
fantômes. Si vous anéantissez Vonotar, vous anéantirez par là même la
force maléfique qui donne son pouvoir à la flotte des bateaux fantômes
et à son équipage.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Vous pouvez grimper en haut de la tour et attaquer Vonotar en vous rendant au :"))
    st.page_link("tomes/tome2/page_73.py", label="73", icon="📄")
    st.write_stream(stream_text("Si vous préférez ne pas risquer votre vie en vous mesurant à ce puissant magicien, fuyez ce navire en sautant par-dessus bord et rendez-vous au :"))
    st.page_link("tomes/tome2/page_267.py", label="267", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
