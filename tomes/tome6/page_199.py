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

check_inventory(current_page_number=199, book=6)

fr_text = """
Le prestidigitateur aux habits flamboyants fait surgir un bouquet
de fleurs dans l'oreille d'un marchand médusé, puis retire une
poule gloussante du jupon de sa femme. Il demande ensuite à la
bruyante assemblée de faire silence avant d'annoncer son
prochain tour. Deux enfants montent sur la scène. Ils sont tous
deux revêtus d'un grand voile noir attaché derrière la tête qui
dissimule tout leur corps, excepté les cheveux. « Je suis un
garçon », dit l'enfant aux cheveux noirs. « Je suis une fille», dit
celui aux cheveux blonds, de la même voix que le premier. Le
prestidigitateur s'avance vers eux et affirme qu'il s'agit bien d'un
garçon et d'une fille mais que l'un d'entre eux au moins ment. Il
demande au public : « Qui est qui ? » puis invite les gens à parier
sur la réponse.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez parier sur la réponse à cette devinette, rendez-vous au :"))
    st.page_link("tomes/tome6/page_245.py", label="245", icon="📄")

    st.write_stream(stream_text("Si vous ne le souhaitez pas, vous vous dirigez vers le bar pour vous enquérir d'une chambre pour la nuit. Rendez-vous au :"))
    st.page_link("tomes/tome6/page_253.py", label="253", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
