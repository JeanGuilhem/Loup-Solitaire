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

check_inventory(current_page_number=219, book=4)

fr_text = """
Il vous faut une demi-heure pour reprendre vos esprits et
localiser l'endroit où vous vous trouvez à présent. Vous vous
apercevez bientôt que vous êtes au pied d'un énorme crassier qui
émerge de la rivière souterraine. A moins de 6 mètres de son
sommet, une faible lueur éclaire un long tunnel de pierre qui sert
de plan incliné. Il vous est possible d'y grimper, bien que cette
escalade soit difficile et périlleuse. Il vous faut une heure d'efforts
pour arriver enfin au sommet du crassier. Vous pénétrez alors
dans le petit tunnel désert où vous trouvez un chariot de mine
près de l'entrée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez examiner ce chariot, rendez-vous au :'))
    st.page_link("tomes/tome4/page_167.py", label="167", icon="📄")

    st.write_stream(stream_text('Si vous préférez ne pas y prêter attention, vous monterez la pente escarpée de ce tunnel en vous rendant au :'))
    st.page_link("tomes/tome4/page_185.py", label="185", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
