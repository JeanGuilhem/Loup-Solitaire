import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=192, book=2)

fr_text = """
Les marins ivres poussent des grognements satisfaits, et l'argent change
de mains tandis qu'on prend les paris. Vous remarquez alors que votre
adversaire adresse un clin d'œil à deux de ses compagnons qui
s'avancent aussitôt vers vous. Sans hésiter une seconde, vous vous
levez d'un bond et vous frappez le marin d'un coup de poing au visage.
Le choc est si rude qu'il est projeté en arrière et s'écroule dans les bras
de ses deux complices, les entraînant dans sa chute. Vous les laissez se
débattre et vous vous dirigez vers la sortie. Mais, lorsque vous atteignez
la porte, un autre marin au visage repoussant tire son épée et vous
bloque le passage. Avant que vous n'ayez eu le temps de réagir,
cependant vous entendez un bruit sourd et l'homme tombe à genoux.
Derrière lui se tient la serveuse, une grosse massue de bois à la main.
Elle vous sourit et vous la remerciez en lui adressant un clin d'oeil mais
ce n'est pas le moment de vous attarder et vous filez par la porte dans la
rue obscure recouverte de pavés. Vous courez quelques minutes dans le
noir et vous apercevez alors une écurie et un relais de diligence dont les
contours se dessinent dans l'ombre. Les hurlements furieux des marins
retentissent à vos oreilles tandis que vous courez vers le bâtiment ; par
chance une échelle extérieure vous permet de grimper dans un grenier à
foin où vous vous réfugiez pour la nuit sans risque d'être découvert.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_32.py", label="32", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
