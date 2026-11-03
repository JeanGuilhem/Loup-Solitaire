import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, handle_repas, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=247, book=4)

fr_text = """
Vos hommes semblent déçus par votre décision. Mais vous êtes
leur chef et ce sont des soldats d'élite du Sommerlund. Ils
obéissent donc sans discuter et sans manifester le moindre signe
de mécontentement. Tandis que vous avancez en direction du
sud, l'obscurité de la nuit enveloppe bientôt la grand-route et
vous êtes contraints de vous arrêter et de dresser le camp sur le
bas-côté. Les hommes rassemblent du bois pour faire du feu et
une sentinelle reçoit pour mission de surveiller les chevaux. Vous
avez faim, il vous faut donc prendre un Repas, sinon vous
perdrez 3 points d'ENDURANCE. La nuit se passe sans incident ;
à l'aube vous levez le camp et vous poursuivez votre chemin à
travers la Contrée des Pillards.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    handle_repas()

    st.write_stream(stream_text('Utilisez la Table de Hasard pour obtenir un chiffre.'))
    roll = hazard_roll()
    if roll is not None:
        if roll <= 4:
            st.write_stream(stream_text('Si vous tirez un chiffre de 0 à 4, rendez-vous au :'))
            st.page_link("tomes/tome4/page_171.py", label="171", icon="📄")
        else:
            st.write_stream(stream_text('De 5 à 9, rendez-vous au :'))
            st.page_link("tomes/tome4/page_25.py", label="25", icon="📄")


    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
