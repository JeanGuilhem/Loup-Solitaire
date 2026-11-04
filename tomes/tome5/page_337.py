import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=337, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Maintenant que la légère brise qui vous rafraîchissait à bord de la
Nef du ciel ne souffle plus, la chaleur des montagnes s'avère
presque insupportable. Vos pieds s'enfoncent profondément
dans le sable rouge et vous avancez avec peine, vous protégeant
le visage contre la poussière âcre que vous soulevez à chaque pas.
La seule végétation qui parvient à pousser sur cette terre désolée
est une herbe dure et tranchante comme l'acier, qui écorche le
cuir de vos bottes et de vos jambières. Alors que vous atteignez
les environs d'Ikaresh, vous passez à proximité d'une hutte
ronde. Une chèvre est attachée à une mangeoire, près de la porte,
et un homme surgit soudain dans l'encadrement. Il vous souhaite
la bienvenue d'un geste amical puis vous invite à entrer dans son
humble cabane.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous désirez accepter son invitation, rendez-vous au :'))
    st.page_link("tomes/tome5/page_225.py", label="225", icon="📄")

    st.write_stream(stream_text('Si vous préférez décliner poliment son offre et continuer votre route vers Ikaresh, rendez-vous au :'))
    st.page_link("tomes/tome5/page_272.py", label="272", icon="📄")

    st.write_stream(stream_text('Si vous maîtrisez la Discipline Kaï du Sixième Sens, rendez-vous au :'))
    if has_kai("Le Sixième Sens"):
        st.page_link("tomes/tome5/page_365.py", label="365", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_365.py", label="365", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
