import streamlit as st
from combat import combat
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

check_inventory(current_page_number=14, book=4)

fr_text = """
Vos patrouilleurs se déploient et avancent sans bruit à l'abri de
gros rochers. Lorsque vous êtes arrivé à proximité de l'ennemi,
vous lancez un sifflement perçant : c'est le signal de l'attaque !
Immédiatement vos soldats se précipitent sur les brigands. Deux
de ces derniers meurent sur le coup, le crâne fracassé par les
épées des patrouilleurs. Un troisième fait volte-face pour
s'enfuir, mais il est tué à son tour et précipité dans l'eau
parsemée d'écume. Votre propre adversaire est un redoutable
Guerrier: d'énormes bracelets d'acier lui protègent les poignets et
les avant-bras, et un sinistre collier composé de têtes réduites
orne sa poitrine. Vous portez le premier coup, mais ses réflexes
sont vifs comme l'éclair. Il esquive en effet et contre-attaque à
l'aide de sa lance.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Vous pouvez prendre la fuite à tout moment en plongeant dans la rivière Xane."))
    outcome = combat([("GUERRIER PILLARD", 17, 28)], flee_after=0)
    if outcome == "fled":
        st.write_stream(stream_text("Vous plongez dans la rivière Xane, rendez-vous au :"))
        st.page_link("tomes/tome4/page_31.py", label="31", icon="📄")

    elif outcome == "win":
        st.write_stream(stream_text("Si vous combattez et sortez vainqueur, rendez-vous au :"))
        st.page_link("tomes/tome4/page_146.py", label="146", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
