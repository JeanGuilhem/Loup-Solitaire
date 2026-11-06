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

check_inventory(current_page_number=289, book=6)

fr_text = """
Vous galopez dans l'obscurité le long de la rue mal pavée. Vous
êtes maintenant hors de danger. Vous vous arrêtez sur une petite
place pour permettre à votre cheval de boire à un abreuvoir qui se
trouve à côté d'un petit porche en pierre. Tandis que votre
monture se désaltère, vous observez le va-et-vient des habitants
de la ville. Des nombreux cabarets qui bordent la place vous
parviennent les chants joyeux de consommateurs ivres. Tout à coup,
deux mariniers sortent d'une taverne et commencent à se battre à
coups de tesson et de couteau, encouragés par les cris de leurs
compagnons qui parient des poignées de Pièces d'Or sur l'issue du
combat. Mais le combat dégénère bientôt en une rixe générale, et
vous décidez de quitter rapidement les lieux pour ne pas être
entraîné dans la mêlée malgré vous.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_332.py", label="332", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
