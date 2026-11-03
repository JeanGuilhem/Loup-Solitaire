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

check_inventory(current_page_number=295, book=4)

fr_text = """
Le Guerrier Pillard est étendu mort à vos pieds. « Vive le
Sommerlund ! » vous écriez-vous, tandis que le mur de boucliers
ennemis vacille et s'effondre. Vos hommes reprennent en chœur
ce cri de guerre et s'élancent sur les brigands. Les épées
gémissent en s'entrechoquant comme si le métal criait de
douleur à l'instar des hommes qui le brandissent. Le combat est
bref et sans merci. Les brigands jettent bientôt à terre leurs
boucliers et s'enfuient de la taverne en se fondant dans
l'obscurité humide de pluie. Vous rassemblez vos patrouilleurs et
vous vous précipitez vers les écuries ; votre cœur se met alors à
battre plus vite en constatant que les portes en sont grandes
ouvertes. Vous craignez le pire.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_345.py", label="345", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
