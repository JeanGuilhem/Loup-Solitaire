import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=289, book=5)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
Le trône commence à tourner. Un terrible hurlement parvient à
vos oreilles puis se change presque instantanément en une série
de grognements rauques évoquant une langue dure et gutturale
que vous n'avez jamais entendue auparavant. Des mots et des
bruits, tels qu'une bouche humaine jamais n'articula, roulent à
travers la pièce comme des éclats de tonnerre. C'est le langage
noir parlé par Haakon, Seigneur d'Aarnak et Seigneur des
Ténèbres d'Helgedad. Tandis qu'il se lève lentement du trône, la
voix sépulcrale, surnaturelle, sortant de sa bouche, continue à
retentir. Il tient au creux de sa main gantée une pierre
étincelante. Une petite flamme bleue est retenue en son cœur.
Brusquement, le langage d'Haakon se transforme et vous pouvez
entendre une langue qui vous est familière : le langage du
Sommerlund ! « Ton heure est venue, Seigneur Kaï ! » Soudain,
un craquement assourdissant retentit : une redoutable puissance
est en train de naître ! En effet, quelques secondes plus tard, un
tourbillon de flammes bleues se dirige vers votre tête.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez le Glaive de Sommer, rendez-vous au :"))
    if has_item("GLAIVE DE SOMMER"):
        st.page_link("tomes/tome5/page_311.py", label="311", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome5/page_311.py", label="311", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne possédez pas cet Objet Spécial, rendez-vous au :"))
    if has_item("GLAIVE DE SOMMER"):
        st.page_link("tomes/tome5/page_219.py", label="219", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome5/page_219.py", label="219", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
