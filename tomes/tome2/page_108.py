import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    is_new_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=108, book=2)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
L'une des roues se coince dans une ornière et trois de ses gros rayons de
bois se brisent sous le choc. Il vous faut interrompre votre voyage et
remplacer la roue avant de pouvoir repartir vers Port Bax. Vous vous
proposez d'aider le conducteur en soulevant la diligence à l'aide d'un
levier, puis en plaçant un petit tronc d'arbre sous l'essieu afin qu'on
puisse glisser la nouvelle roue sur son axe. Vous pesez de tout votre
poids sur la grosse branche qui fait office de levier lorsque les chevaux
se cabrent soudain puis s'élancent en avant. La branche aussitôt se
détend comme un ressort et vous frappe en plein visage en vous
projetant à terre. Vous êtes à moitié assommé et vous perdez 2 points
d'ENDURANCE. Le conducteur a moins de chance que vous car la
diligence lui a passé sur le corps. Le malheureux meurt dans vos bras
après avoir réussi, dans un ultime effort, à vous murmurer ces quelques
mots à l'oreille: « Pas... un accident... j'ai vu... ».
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)
    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï du Sixième Sens, rendez-vous au :"))
    if has_kai("Le Sixième Sens"):
        st.page_link("tomes/tome2/page_343.py", label="343", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome2/page_343.py", label="343", icon="📄", disabled=True)
        st.write_stream(stream_text("Sinon, rendez-vous au :"))
        st.page_link("tomes/tome2/page_168.py", label="168", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
