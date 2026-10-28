import streamlit as st
from inventory import (
    add_to_inventory,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import stream_text, handle_repas, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=12, book=3)

fr_text = """
Le matériel et les vivres sont rapidement déballés et répartis
entre vous. Vous recevez des provisions qui représentent
l'équivalent de 3 Repas, des Couvertures en Fourrure et une
Corde. Inscrivez tous ces éléments sur votre Feuille d'Aventure
en sachant que les Couvertures en Fourrure prennent dans votre
Sac à Dos la place de deux objets normaux. Il vous est impossible
d'emmener les chiens Kanu dans les montagnes et vous êtes donc
contraint de les abandonner ici, de même que les traîneaux. Vous
vous encordez avec vos guides, et vous vous mettez en route en
direction d'un étroit passage qui s'enfonce entre les pics sombres
et sinistres. Tout d'abord, l'escalade ne présente pas de difficultés
mais, bientôt, la pente de glace lisse devient abrupte et votre
progression est beaucoup plus malaisée. Un vent se lève qui
forme des tas de neige poudreuse contre les blocs de glace et la
visibilité est alors réduite à quelques mètres. Les tas de neige
sont trompeurs et parfois profonds. A deux reprises, vous vous y
enfoncez jusqu'à la poitrine et les autres doivent venir vous
dégager. Cette nuit-là, vous dressez votre tente sur une surface
de granite recouverte de glace qui surplombe un profond ravin.
Vous êtes épuisé et vous vous endormez presque au cours du
Repas (n'oubliez pas de rayer ce Repas de votre Feuille
d'Aventure). « Est-ce que vous parlez un peu la langue des
Barbares des Glaces ? demande Dyce qui essaie d'entretenir la
conversation. Pour ma part, je ne connais que quelques mots,
Myjavik, par exemple. » Lorsque vous lui demandez ce que ce
mot signifie, il observe un instant de silence puis vous répond :
« Terreur... Myjavik signifie terreur. » Soudain, un bruit
impressionnant retentit à l'extérieur de la tente. On dirait le
rugissement d'un gros animal.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        # matériel imposé, donné avant le Repas du soir ; ce qui ne rentre pas reste à prendre plus bas
        missing = []
        for name in ["REPAS", "REPAS", "REPAS", "COUVERTURE DE FOURRURE", "CORDE"]:
            if not add_to_inventory(name):
                missing.append(name)
        st.session_state["visibility_p12_missing"] = missing
    handle_repas()
    missing = st.session_state.get("visibility_p12_missing") or []
    if missing:
        st.warning("Faute de place, une partie du matériel n'a pas pu être rangée. Faites de la place dans l'onglet Inventaire, puis prenez-le :")
        for index, name in enumerate(missing):
            pickup_button(name, key=f"p12_{index}", label=f"Prendre : {name}")

    st.write_stream(
        stream_text(
            "Si vous souhaitez tirer votre épée et aller voir de quoi il s'agit, rendez-vous au :"
        )
    )
    st.page_link("tomes/tome3/page_180.py", label="180", icon="📄")

    st.write_stream(
        stream_text(
            'Si vous préférez retenir votre souffle en restant aussi immobile que possible, '
            'rendez-vous au :'
        )
    )
    st.page_link("tomes/tome3/page_259.py", label="259", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
