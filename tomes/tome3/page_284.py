import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=284, book=3)

fr_text = """
Après avoir parcouru une centaine de mètres, vous vous
retrouvez dans une immense caverne qui s'étend dans toutes les
directions aussi loin que le regard peut porter. Vous venez de
pénétrer dans les Grottes de Kalte et vous contemplez en ce moment même un monde inconnu que très peu de
Sommerlundais ont eu l'occasion de voir. Ce gigantesque
labyrinthe souterrain fut construit par les Anciens en des temps
très reculés, bien avant que les Sommerlundais eussent mis le
pied sur les terres de Magnamund. Ses larges tunnels, ses
temples, ses cavernes ont abrité une race de créatures pour qui la
glace était un environnement naturel et, sous ces voûtes, a retenti
l'écho de leurs pas et de leurs voix. Des coupes de M'iare sont
toujours suspendues aux plafonds, baignant les cavernes de leur
lumière éternelle. Vous marchez d'un bon pas pendant presque
six heures avant d'arriver au bord d'une petite rivière au cours
rapide. Sur la berge opposée, vous apercevez un tunnel qu'il vous
faut emprunter pour poursuivre votre chemin. L'eau est
profonde, et le seul moyen de la franchir consiste à prendre pied
sur des morceaux de glace qui flottent à sa surface, en sautant de
l'un à l'autre. Vous pourriez ainsi atteindre l'autre rive, mais c'est
une tentative risquée et périlleuse. Pour traverser la rivière, vous
devrez sauter trois blocs de glace au moins.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Discipline Kaï de la Chasse, vous aurez le droit d'ajouter 2 au chiffre que vous aurez tiré. Si votre total actuel d'ENDURANCE est inférieur à 8, vous devrez ôter 2 du chiffre donné par la Table."))
    roll = hazard_roll()
    if roll is not None:
        total = roll
        if has_kai("La Chasse"):
            total += 2
            st.write("*Chasse : +2.*")
        if st.session_state.endurance < 8:
            total -= 2
            st.write("*ENDURANCE inférieure à 8 : -2.*")
        st.write(f"*Total : {total}.*")
        if total <= 3:
            st.page_link("tomes/tome3/page_94.py", label="94", icon="📄")
        else:
            st.page_link("tomes/tome3/page_176.py", label="176", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
