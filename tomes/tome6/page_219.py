import streamlit as st
from inventory import (
    can_shoot,
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

check_inventory(current_page_number=219, book=6)

fr_text = """
Tout à coup, un jeune seigneur fait irruption dans la taverne en
claquant la porte à toute volée. Il est vêtu d'un costume noir et or
resplendissant. Il ôte son manteau de velours avec ostentation,
puis il demande pompeusement à boire et à manger. Il ne faut
pas moins de trois serveuses et du tavernier pour s'occuper de lui
! Ses manières sont si hautaines et si insultantes que vous n'êtes
pas surpris de constater que son visage est couturé de cicatrices.
Cet homme doit être constamment en train de chercher querelle
et de provoquer des duels. Le jeune noble choisit lui-même de
s'asseoir à une table déjà occupée par un petit vieillard inoffensif.
Il commence à insulter le vieil homme puis, le saisissant à la
gorge d'une main, le soulève de son siège et le jette au sol. «
Espèce de vieux crapaud pleurnicheur, comment oses-tu t'asseoir
à ma table ? » s'écrie-t-il. Terrifié et ahuri, le petit homme
bredouille en vain une excuse. Le jeune noble se lève, repousse sa
chaise du pied, puis se penche sur le pauvre malheureux, la main
sur la garde de son épée. La foule des consommateurs assiste à la
scène avec délectation, comme à un spectacle des Arènes de
Vassagonie, car le noble a visiblement l'intention de tuer le
vieillard.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # le paragraphe 301 décoche une flèche : il faut un Arc, un Carquois et une flèche
    st.write_stream(stream_text("Si vous possédez un Arc, rendez-vous au :"))
    if can_shoot():
        st.page_link("tomes/tome6/page_301.py", label="301", icon="📄")
    else:
        st.write("*Il vous faut un Arc, un Carquois et une flèche.*")
        st.page_link("tomes/tome6/page_301.py", label="301", icon="📄", disabled=True)
    st.write_stream(stream_text("Si vous n'en possédez pas, rendez-vous au :"))
    if can_shoot():
        st.page_link("tomes/tome6/page_78.py", label="78", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome6/page_78.py", label="78", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
