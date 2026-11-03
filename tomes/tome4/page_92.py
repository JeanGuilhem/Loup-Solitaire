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

check_inventory(current_page_number=92, book=4)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Le lendemain à midi, vous parvenez aux abords d'Eshnar. Au
sud, les collines boisées montent en pente douce vers les
magnifiques sommets enneigés de la chaîne de Maaken. C'est un
spectacle extraordinaire qui contraste singulièrement avec la
laideur d'Eshnar et l'aspect lugubre du Pays Sauvage qui s'étend
au nord. Vous chevauchez le long de l'unique rue de cette ville
délabrée et vous arrivez enfin devant une grande taverne : « La
Pioche et la Pelle ». Vos hommes sont épuisés et ont grand
besoin de manger et de se reposer.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez entrer dans cette taverne, rendez-vous au :"))
    st.page_link("tomes/tome4/page_132.py", label="132", icon="📄")

    st.write_stream(stream_text("Si vous préférez continuer le long de la rue, rendez-vous au :"))
    st.page_link("tomes/tome4/page_301.py", label="301", icon="📄")

    st.write_stream(stream_text("Enfin, si vous maîtrisez la Discipline Kaï du Sixième Sens, rendez-vous au :"))
    if has_kai("Le Sixième Sens"):
        st.page_link("tomes/tome4/page_210.py", label="210", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome4/page_210.py", label="210", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
