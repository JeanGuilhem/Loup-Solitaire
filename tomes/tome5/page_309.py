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

check_inventory(current_page_number=309, book=5)

fr_text = """
Alors que vous pénétrez dans les écuries, l'odeur forte des
Douggas vous prend à la gorge et vous ne pouvez vous empêcher
de vous boucher le nez tout en serrant les dents avec une grimace
de dégoût. Un jeune garçon se met à rire de votre réaction et
s'écrie : « Je donnerai ma main à couper que vous n'êtes pas
d'Ikaresh, vous ! » Puis il se met à imiter votre moue, révélant
dans sa mimique une rangée de dents abîmées. « Sais-tu où je
pourrais trouver Tipasa le Vagabond ? » demande Banedon tout
en brandissant un anneau d'argent. Une lueur de convoitise brille
soudain dans les yeux du garçon à la vue du métal étincelant. 
« Mais oui, bien sûr ! réplique-t-il avec empressement. Remontez
l'allée et prenez la première ruelle à votre gauche. Le vieux
vagabond y habite la maison à la porte bleue. » D'une
chiquenaude, Banedon lance l'anneau en l'air et le gamin s'en
saisit au vol avec avidité. Vous quittez ensuite rapidement les
lieux et vous commencez à chercher la ruelle que l'on vous a
indiquée. Au moment même où vous l'atteignez, vous entendez le
jeune garçon pousser un cri de déception : l'anneau vient de se
volatiliser au creux de sa main ! Sans y accorder plus d'attention,
vous vous engagez dans la ruelle sombre et malpropre au bout de
laquelle vous découvrez enfin la maison à la porte bleue.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome5/page_206.py", label="206", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
