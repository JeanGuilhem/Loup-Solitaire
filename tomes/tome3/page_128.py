import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=128, book=3)

fr_text = """
Lorsque la porte de pierre s'ouvre en grinçant, l'homme, dans
une réaction de surprise, rejette la tête en arrière.
« Qui est là ? » murmure-t-il d'une voix fluette et étranglée. Ses
yeux brillent dans l'ombre de son capuchon en lambeaux. Puis
soudain, il semble vous reconnaître et se relève d'un bond. « Un
Seigneur Kaï ! s'exclame-t-il, les dieux soient loués ! Je m'appelle
Tygon et je suis un marchand de Ragadorn. Les Barbares des
Glaces m'ont capturé à Liouk et amené ici. J'attends à présent
d'être reçu en audience par leur nouveau Brumalmarc, le sorcier
du Sommerlund qu'ils appellent Vonotar. Il semble que ce soit
lui qui doive décider de mon sort. Mais si vous me délivrez de ce
pentagramme magique, je ferai de mon mieux pour vous aider. »
Ce pentagramme ne vous est pas inconnu : il s'agit en effet d'un
cercle de claustration, une prison magique qui ne peut être
détruite que de l'extérieur. Pour libérer cet homme, il vous suffit
d'effacer une partie du cercle tracé sur le sol.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez le libérer, rendez-vous au :"))
    st.page_link("tomes/tome3/page_170.py", label="170", icon="📄")
    st.write_stream(stream_text("S'il vous est arrivé de vous rendre à Ragadorn, vous voudrez peut-être lui poser quelques questions sur cette ville afin de dissiper les soupçons que vous pourriez avoir quant à son identité véritable ; rendez-vous pour cela au :"))
    st.page_link("tomes/tome3/page_11.py", label="11", icon="📄")
    st.write_stream(stream_text("Enfin, si vous préférez refermer la porte de la cellule et retourner dans le couloir principal, rendez-vous au :"))
    st.page_link("tomes/tome3/page_254.py", label="254", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
