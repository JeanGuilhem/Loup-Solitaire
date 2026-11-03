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

check_inventory(current_page_number=171, book=4)

fr_text = """
Vous parcourez des kilomètres dans le paysage désolé qui borde
la Voie de Ruanon. Cependant, en dépit de ce morne spectacle,
vos hommes semblent d'humeur joyeuse. Ils chantent des
chansons de marche pour essayer de rompre la monotonie du
voyage et oublier quelque peu les dangers qui les attendent. Au
cours de l'après-midi, des nuages d'orage s'amoncellent au
sommet des monts Durncrag, à l'ouest, et un lointain
grondement de tonnerre annonce une pluie imminente. A la fin
de l'après-midi, vos éclaireurs repèrent un relais de diligence, un
peu plus loin sur la route. C'est un grand bâtiment de pierre, aux
murs fortifiés, qui abrite une taverne.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez vous arrêter dans cette taverne pour la nuit, rendez-vous au :'))
    st.page_link("tomes/tome4/page_63.py", label="63", icon="📄")

    st.write_stream(stream_text('Si vous préférez affronter un éventuel orage et poursuivre votre chemin en direction du sud, rendez-vous au :'))
    st.page_link("tomes/tome4/page_141.py", label="141", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
