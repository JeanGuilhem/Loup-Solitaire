import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_gold,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=220, book=2)

fr_text = """
En fouillant son cadavre, vous découvrez des preuves accablantes :
aucun doute, c'est bien lui qui a tenté de vous tuer. Dans l'une de ses
poches, vous trouvez une fiole à moitié vide de sève de gandurn, le
poison mortel qu'il avait versé dans vos aliments. Vous tombez ensuite
sur un parchemin écrit en langue Glok et dans lequel sont indiqués tous
les détails de votre voyage à Port Bax. C'est à Ragadorn qu'il a dû vous
repérer et c'est là également qu'il a élaboré ses plans pour vous tuer.
Vous remarquez aussi que son arme est une épée de Maître des
Ténèbres, à la lame d'acier noir forgée dans le feu d'Helgedad, la cité
infernale située au-delà des monts Durncrag. C'est le seul endroit, sur
toutes les terres de Magnamund, où l'on peut fabriquer de l'acier noir.
Mais la preuve irréfutable de son identité, vous la découvrez sur son
poignet gauche : c'est un tatouage qui représente un serpent. Les
brigands qui avaient essayé de vous tuer avant même que vous quittiez
Holmgard portaient exactement la même marque. La bourse du moine
contient 23 Pièces d'Or que vous pouvez conserver sans oublier de les
inscrire sur votre Feuille d'Aventure.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_gold(23)

    st.write_stream(stream_text('Rendez-vous ensuite au :'))
    st.page_link("tomes/tome2/page_33.py", label="33", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
