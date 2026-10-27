import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    spend_gold,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=195, book=2)

fr_text = """
Au bout d'une heure de voyage, le cocher annonce : « Pont à péage, une
Couronne par personne. » Vous jetez un coup d'œil par la portière : la
pluie tombe à verse mais vous parvenez malgré tout à distinguer au loin
un pont de bois et une cabane en rondins. Un peu plus tard, le cocher
arrête la diligence devant la cabane et une créature repoussante apparaît
à la porte. C'est un Squall à la peau couverte de verrues. Les Squalls
appartiennent à la famille des Gloks mais ce sont des êtres peureux et
inoffensifs. Ils habitaient le Pays Sauvage au temps de la Lune Noire,
lorsque des milliers d'entre eux émigrèrent, abandonnant les Monts
Durncrag, pour échapper à la tyrannie de Vashna, le plus puissant des
Maîtres des Ténèbres. Le Squall demande à chaque passager de la
diligence de payer une Couronne le droit de franchir le pont. Vos
compagnons de voyage déposent chacun une Couronne sur une petite
assiette qu'ils vous tendent ensuite.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Si vous avez de quoi payer votre passage, donnez une Couronne à votre tour et poursuivez "
            "votre route en vous rendant au :"
        )
    )
    if st.button("Payer 1 Couronne (249)", disabled=st.session_state.purse < 1):
        if spend_gold(1):
            st.switch_page("tomes/tome2/page_249.py")

    st.write_stream(stream_text("Si vous n'avez pas d'argent, rendez-vous au :"))
    st.page_link("tomes/tome2/page_50.py", label="50", icon="📄", disabled=st.session_state.purse >= 1)
    if st.session_state.purse >= 1:
        st.caption("Vous avez de quoi payer votre passage.")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
