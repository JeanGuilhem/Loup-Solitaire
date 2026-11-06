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
from utils import called_cookies, stream_text

# fait posé : « cheval » (le pur-sang bai fourni par les frères de Gwynian)

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=175, book=6)

fr_text = """
Lorsque la cloche de l'observatoire sonne les douze coups de
minuit, vous êtes déjà fin prêt à sortir par le portail qu'on vous
avait désigné. Vous longez ensuite un passage dallé pendant
quelque temps, puis vous arrivez devant une porte de fer. Celle-ci
s'ouvre en grinçant, et un courant d'air humide, où des relents
d'humus se mêlent à des fragrances étrangement sucrées, vous
souffle en plein visage. Devant vous, un escalier étroit s'élève
dans les ténèbres. Vous avancez avec d'infinies précautions sur
les marches glissantes. Tout en haut de l'escalier, un tunnel
grossièrement creusé s'enfonce vers l'ouest. Vous vous y engagez
et vous parvenez peu après à une autre porte en fer. Gwynian a
tenu parole : de l'autre côté, vous trouvez un superbe pur-sang
bai, sellé et prêt à être monté. Vous chevauchez à vive allure
jusqu'à un croisement qui rejoint la grand-route. A la lumière
blafarde de la lune, vous distinguez un poteau indiquant deux
directions : Amory et Soren. Reportez-vous à la carte figurant au
début du livre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        set_flag("cheval")

    st.write_stream(stream_text("Si vous choisissez la grand-route vers Amory, rendez-vous au :"))
    st.page_link("tomes/tome6/page_331.py", label="331", icon="📄")

    st.write_stream(stream_text("Si vous préférez prendre vers Soren, rendez-vous au :"))
    st.page_link("tomes/tome6/page_267.py", label="267", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
