import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=309, book=4)

fr_text = """
Vous suivez le tunnel pendant plus de trois heures avant d'arriver
dans une vaste salle, où aboutissent plusieurs autres souterrains
situés à différents niveaux. De larges rampes de pierre relient
chaque tunnel à celui qui se trouve immédiatement au-dessus ou
au-dessous. Quatre étages plus bas, des équipes de mineurs
poussent des chariots chargés de minerai. Des Gardes vêtus
d'armures écarlates les surveillent en les incitant à travailler plus
vite à grands coups de fouet et en hurlant des jurons. Le tunnel
dans lequel vous vous trouvez est situé au niveau le plus élevé, et
vous ne pouvez poursuivre votre chemin qu'en descendant une
rampe menant à un tunnel inférieur. Mais, à votre grande
consternation, vous constatez que chacune des rampes est gardée
par des hommes en armes. Avançant avec d'infinies précautions
vous jetez un coup d'œil par-dessus la rampe. Deux Gardes sont
assis au sommet d'une autre rampe devant l'entrée du tunnel qui
se trouve juste au-dessous. Ils éclatent de rire en se donnant de
grandes tapes dans le dos et en montrant du doigt une bouteille
de vin vide posée à leurs pieds. Après les avoir observés pendant
quelques minutes, ils vous semblent trop ivres pour faire
attention à vous. Vous décidez donc de tenter votre chance en
vous précipitant vers le tunnel dans l'espoir qu'ils ne vous
verront pas.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Discipline Kaï du Camouflage, vous ajouterez 4 à ce chiffre."))
    roll = hazard_roll()
    if roll is not None:
        total = roll + (4 if has_kai("Le Camouflage") else 0)
        if has_kai("Le Camouflage"):
            st.write(f"*Camouflage : +4, soit un total de {total}.*")
        if total <= 7:
            st.write_stream(stream_text("Si vous obtenez un total de 0 à 7, rendez-vous au :"))
            st.page_link("tomes/tome4/page_138.py", label="138", icon="📄")
        else:
            st.write_stream(stream_text("De 8 à 13, rendez-vous au :"))
            st.page_link("tomes/tome4/page_244.py", label="244", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
