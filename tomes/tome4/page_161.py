import streamlit as st
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

check_inventory(current_page_number=161, book=4)

fr_text = """
Vous relevez le capuchon de votre cape de Seigneur Kaï et vous
vous accroupissez au fond du chariot vide en retenant votre
souffle. Par un interstice entre deux planches, vous apercevez
une procession d'hommes au visage hagard qui avancent vers
vous en traînant les pieds. Des Guerriers Pillards les escortent en
frappant ceux qui chancellent ou s'écartent des rangs. Une
soudaine secousse vous indique que le chariot est à présent
poussé le long du tunnel. En levant les yeux vous apercevez le
visage ruisselant de sueur d'un homme qui se penche vers vous.
« Fuyez à gauche quand je vous dirai : Allez-y ! » murmure
l'homme. Il relève alors la tête et vous ne pouvez plus voir son
visage. Lorsque le chariot émerge du tunnel, vous êtes ébloui par
la lumière du soleil. A travers l'interstice vous parvenez à voir
l'endroit vers lequel on pousse votre chariot. Il s'agit d'un
portique sous lequel s'arrête la voie ferrée, à quelque 15 mètres
au-dessus d'un énorme entassement de minerai. Vous n'avez pas
l'occasion cependant de poursuivre longtemps votre
contemplation : un ordre bref vous interrompt en effet : « Allez-y !
» murmure l'homme au visage ruisselant de sueur.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez sauter du chariot en courant vers la gauche, rendez-vous au :'))
    st.page_link("tomes/tome4/page_27.py", label="27", icon="📄")

    st.write_stream(stream_text('Si vous préférez sauter du chariot en courant vers la droite, rendez-vous au :'))
    st.page_link("tomes/tome4/page_144.py", label="144", icon="📄")

    st.write_stream(stream_text('Enfin, si vous estimez plus sage de ne pas tenir compte de ce conseil et de rester où vous êtes, rendez-vous au :'))
    st.page_link("tomes/tome4/page_294.py", label="294", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
