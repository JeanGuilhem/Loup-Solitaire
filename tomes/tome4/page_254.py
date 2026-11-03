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

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=254, book=4)

fr_text = """
Le tunnel descend sur plusieurs centaines de mètres. Vous
arrivez alors dans une grande salle au sol recouvert d'un
plancher. Deux rangées de traces de pas sont clairement visibles
dans la boue qui recouvre les planches pourries. Vous constatez
alors avec horreur qu'elles s'arrêtent au bord d'un trou béant.
Vous vous approchez avec précaution et vous jetez un coup d'œil
dans le trou. Vous apercevez aussitôt deux cadavres étendus au
fond d'un puits de vase. Vous avez retrouvé vos éclaireurs, mais
vous ne pouvez plus rien faire pour eux. Les planches de bois
commencent à s'affaisser sous vos pieds et vous vous hâtez de
vous éloigner du bord pour ne pas connaître un sort semblable.
Au-delà du puits, deux passages permettent de quitter cette salle,
l'un est orienté à l'est, l'autre au sud.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï de l'Orientation, rendez-vous au :"))
    if has_kai("L'Orientation"):
        st.page_link("tomes/tome4/page_326.py", label="326", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome4/page_326.py", label="326", icon="📄", disabled=True)
    st.write_stream(stream_text("Dans le cas contraire, vous pouvez emprunter le tunnel orienté à l'est, il vous suffit pour cela de contourner le puits ; rendez-vous au :"))
    st.page_link("tomes/tome4/page_156.py", label="156", icon="📄", disabled=has_kai("L'Orientation"))
    st.write_stream(stream_text('Si vous préférez prendre le tunnel orienté au sud, contournez également le puits et rendez-vous au :'))
    st.page_link("tomes/tome4/page_101.py", label="101", icon="📄", disabled=has_kai("L'Orientation"))

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
