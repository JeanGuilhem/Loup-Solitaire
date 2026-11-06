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

check_inventory(current_page_number=83, book=6)

fr_text = """
Le vieil homme plisse ses petits yeux de souris et vous dévisage
attentivement avant de vous répondre : « Ce n'est qu'une
légende... Certains prétendent que cette Pierre renferme un
grand pouvoir, d'autres affirment que ce pouvoir n'existe que
dans l'imagination de ceux qui s'acharnent à se l'approprier.
Quoi qu'il en soit, on a perdu la trace de la Pierre de la
Sagesse depuis des centaines d'années, et nul ne sait
aujourd'hui où elle se trouve. » Vous sentez que le vieux
magicien ne vous dit pas tout ce qu'il sait au sujet de cette
pierre légendaire.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez lui révéler votre identité et la nature exacte de votre quête, rendez-vous au :"))
    st.page_link("tomes/tome6/page_119.py", label="119", icon="📄")

    st.write_stream(stream_text("Si vous préférez ne rien dévoiler à ce propos, prenez congé de votre interlocuteur et rendez-vous au :"))
    st.page_link("tomes/tome6/page_239.py", label="239", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
