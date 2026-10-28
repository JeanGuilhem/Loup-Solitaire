import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    set_flag,
    show_illustrations,
    show_map,
)
from utils import stream_text, handle_repas, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=8, book=3)

fr_text = """
L'odeur est infecte et vous essayez désespérément de retenir
votre respiration tandis que vous vous enduisez le torse de cette
graisse visqueuse ; lorsque l'huile vous pénètre dans la peau,
vous sentez se diffuser à l'intérieur de votre corps une chaleur
rayonnante, comme si vous vous trouviez près d'un feu. Et, plus
vous étalez de graisse, plus la chaleur augmente. Vous remarquez
également que l'épouvantable odeur se dissipe peu à peu.
« Lorsque l'huile imprègne votre peau, vous perdez l'odorat »,
explique Fenor. « Tant mieux, assure Dyce, sinon, je ne pourrais
plus supporter ma propre compagnie ! » L'huile de Bakanal offre
une excellente protection contre le froid mordant qui règne dans
les terres de Kalte et elle vous épargnera peut-être la perte de
précieux points d'ENDURANCE dans un proche avenir. Irian
reprend bientôt connaissance et plonge les mains dans la
carcasse du Bakanal pour bénéficier à son tour de l'huile
bienfaisante. Le jour décline rapidement et vous décidez donc
d'établir votre campement dans cet étroit passage. Vous préparez
un Repas, puis vous montez la garde à tour de rôle, au cas où les
Bakanals décideraient de revenir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        set_flag("huile de Bakanal")
    st.success("*Vous êtes enduit d'huile de Bakanal : elle vous protégera du froid.*")
    handle_repas()

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_325.py", label="325", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
