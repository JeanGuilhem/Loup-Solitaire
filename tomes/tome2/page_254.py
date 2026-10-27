import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."
check_inventory(current_page_number=254, book=2)

fr_text = """
Pendant trois jours et trois nuits, vous avez suivi la route parallèle au
fleuve Durenon, en direction de la capitale. La vallée où coule la rivière
est une vaste région de riches terres cultivées adossées au flanc des
Monts d'Hammardal, l'une des chaînes de montagnes les plus hautes de
tout Magnamund. L'aube s'est levée sur le quatorzième jour de votre
quête lorsque six hommes vêtus de capes apparaissent en bordure de
votre camp. Le Lieutenant Général Rhygar est le premier à tirer son
épée. D'une voix forte, il demande à ces hommes ce qu'ils viennent
faire ici. Pour toute réponse, les six inconnus dégainent chacun une
épée noire. Rhygar alors appelle ses hommes au combat tandis que les
six étrangers vêtus de capes s'avancent vers nous.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez à votre tour dégainer votre arme et vous préparer à combattre, rendez-vous au :'))
    st.page_link("tomes/tome2/page_69.py", label="69", icon="📄")

    st.write_stream(stream_text('Si vous ne voulez pas vous battre, vous pouvez prendre la fuite en courant vers la forêt ; rendez-vous pour cela au :'))
    st.page_link("tomes/tome2/page_183.py", label="183", icon="📄")

    st.write_stream(stream_text('Enfin, si vous maîtrisez la Discipline Kaï du Sixième Sens, rendez-vous au :'))
    if has_kai("Le Sixième Sens"):
        st.page_link("tomes/tome2/page_344.py", label="344", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome2/page_344.py", label="344", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
