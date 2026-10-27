import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    is_new_page,
    lose_all_weapons,
    show_illustrations,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=337, book=2)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Lorsque vous n'êtes plus qu'à une cinquantaine de mètres du rivage,
vous vous laissez glisser dans l'eau et vous nagez vers la terre ferme.
Bientôt, vous atteignez enfin la plage ; vous êtes épuisé et vous vous
traînez sur le sable jusqu'aux dunes qui s'élèvent un peu plus loin et à
l'abri desquelles vous pouvez reprendre haleine. En plus de la fatigue,
la faim vous tenaille mais il vous faut d'abord faire l'inventaire de ce
qui vous reste. Vous avez réussi à conserver vos Pièces d'Or, votre Sac
à Dos et les Objets Spéciaux dont vous n'avez pas été contraint de vous
séparer au cours de la tempête. Vos armes en revanche sont perdues.
Prenez quelques
minutes de repos. Vous vous relevez ensuite et vous parcourez à pied
quelques centaines de mètres. Là, vous trouvez de petits arbres aux
branches contournées qui portent des fruits violets.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        lose_all_weapons()
    st.warning("Vos armes sont perdues : elles ont été retirées de votre inventaire.")

    st.write_stream(stream_text("Si vous souhaitez manger ces fruits, rendez-vous au :"))
    st.page_link("tomes/tome2/page_228.py", label="228", icon="📄")
    st.write_stream(stream_text("Si vous préférez ne pas les manger, vous perdrez 3 points d'ENDURANCE avant de vous rendre au :"))
    if st.button("171 (-3 ENDURANCE)", key="no_fruit", icon="📄"):
        change_endurance(-3)
        st.switch_page("tomes/tome2/page_171.py")
    st.write_stream(stream_text("Enfin, si vous maîtrisez la Discipline Kaï de la Chasse, rendez-vous au :"))
    if has_kai("La Chasse"):
        st.page_link("tomes/tome2/page_139.py", label="139", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome2/page_139.py", label="139", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
