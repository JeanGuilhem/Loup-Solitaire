import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=309, book=3)

fr_text = """
Vous fouillez les cadavres des Barbares et vous découvrez, passée
au cou de l'un d'eux, une chaînette à laquelle est accroché un
Triangle de Pierre Bleue. Si vous souhaitez conserver cet objet,
inscrivez-le sur votre Feuille d'Aventure dans la case Objets
Spéciaux. Vous êtes affamé et vous dévorez gloutonnement la
carcasse rôtie en ne cessant d'engloutir la viande que pour
cracher parfois quelques os. Bientôt, vous remarquez que le feu
allumé devant vous brûle dans une demi-sphère de métal. Une
autre demi-sphère est posée sur le sol de glace, un peu plus loin,
et vous constatez que les deux moitiés s'ajustent parfaitement
pour former une sphère complète. Lorsque vous séparez à
nouveau les deux moitiés, le feu continue de brûler à l'intérieur :
c'est donc un feu perpétuel qui est enfermé dans ce globe. Si vous
souhaitez conserver cette Sphère de Feu, rangez-la dans votre
tunique et inscrivez-la sur votre Feuille d'Aventure dans la case
Objets Spéciaux. Vous finissez alors les derniers restes de viande
encore attachés aux os et vous retournez dans le tunnel.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if not has_item("TRIANGLE DE PIERRE BLEUE"):
        pickup_button("TRIANGLE DE PIERRE BLEUE", key="triangle", label="Prendre le Triangle de Pierre Bleue")
    if not has_item("SPHÈRE DE FEU"):
        pickup_button("SPHÈRE DE FEU", key="sphere", label="Prendre la Sphère de Feu")
    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome3/page_132.py", label="132", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
