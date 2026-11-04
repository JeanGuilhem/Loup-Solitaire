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

check_inventory(current_page_number=56, book=5)

fr_text = """
En fouillant dans les paniers qui jonchent le sol de la petite
embarcation, vous trouvez une mallette en cuir finement
ouvragée. Après en avoir soulevé le fermoir de cuivre, vous
découvrez que cette mallette contient un Jakan, c'est-à-dire un
arc utilisé par les pêcheurs de la côte vassagonienne. Vous êtes
ravi de votre trouvaille, mais vous déchantez soudain en
constatant qu'il n'y a malheureusement qu'une seule flèche dans
l'étui. Sur le port, à côté de l'attelage de Maouk, vous remarquez
qu'il y a un petit magasin aux murs passés à la chaux, où sont
alignées, sur le balcon du premier étage, de grosses bonbonnes
de verre. Vous tendez lentement la corde de l'arc et vous visez
soigneusement l'une de ces bonbonnes, mais il vous sera difficile
d'atteindre votre cible et vous n'avez de plus qu'une seule et
unique chance de réussir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous possédez la Discipline Kaï de la Maîtrise des Armes (quelle que soit l'arme), ajoutez 2 points au chiffre que vous venez de tirer."))
    roll = hazard_roll()
    if roll is not None:
        bonus = 2 if has_kai("La Maîtrise des armes") else 0
        total = roll + bonus
        if bonus:
            st.write(f"*Bonus : +{bonus}, soit un total de {total}.*")
        if total <= 3:
            st.write_stream(stream_text("Si le total obtenu est compris entre 0 et 3, rendez-vous au :"))
            st.page_link("tomes/tome5/page_7.py", label="7", icon="📄")
        else:
            st.write_stream(stream_text("Si ce total est compris entre 4 et 11, rendez-vous au :"))
            st.page_link("tomes/tome5/page_28.py", label="28", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
