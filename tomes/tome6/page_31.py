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

check_inventory(current_page_number=31, book=6)

fr_text = """
Le visage de la femme morte vous revient subitement en mémoire
lorsque vous regardez les yeux de Roark, noirs et étincelants dans
l'ombre de son chapeau à large bord. La ressemblance est tellement
frappante - même nez aquilin et même teint olivâtre - qu'ils ont
sûrement un lien de parenté. Soudain, les cavaliers surgissent et
se déploient en demi-cercle autour de vous. Une voix crie : « Aral
est morte, c'est l'homme du Nord qui l'a tuée !» A ces mots, le
visage de Roark s'empreint de haine, ses yeux se mettent à lancer
des éclairs de folie et ses lèvres à trembler de fureur. Puis il
déchire d'un geste rageur le devant de sa tunique et arrache de sa
chaîne une amulette accrochée autour de son cou. « Viens, Tagazin,
viens je t'en conjure ! Du fond du Puits de la Douleur Éternelle,
je te somme d'accourir ! » Cette odieuse incantation vous donne la
chair de poule et l'appréhension vous envahit. Vous parcourez
rapidement les alentours des yeux pour trouver une issue : la
seule possibilité serait de passer par le cimetière, juste entre
Roark et ses hommes. Mais au moment même où vous lancez votre
cheval sous le portail de pierre, une vision d'horreur vous glace
le sang !
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_270.py", label="270", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
