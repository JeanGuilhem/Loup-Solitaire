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

check_inventory(current_page_number=244, book=4)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Vous passez derrière les Gardes et vous pénétrez dans le tunnel
sans avoir été repéré. Le souterrain est large et éclairé par des
Torches fixées le long des murs. Leurs flammes penchées
vacillent en crépitant avec bruit. Vous arrivez bientôt à un
croisement où le tunnel se rétrécit avant de se séparer en deux.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï du Sixième Sens ou celle de l'Orientation, rendez-vous au :"))
    if has_kai("Le Sixième Sens") or has_kai("L'Orientation"):
        st.page_link("tomes/tome4/page_250.py", label="250", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome4/page_250.py", label="250", icon="📄", disabled=True)

    st.write_stream(stream_text('Dans le cas contraire, vous pouvez prendre le passage de gauche en vous rendant au :'))
    st.page_link("tomes/tome4/page_335.py", label="335", icon="📄", disabled=(has_kai("Le Sixième Sens") or has_kai("L'Orientation")))

    st.write_stream(stream_text('Si vous préférez emprunter le passage de droite, rendez-vous au :'))
    st.page_link("tomes/tome4/page_11.py", label="11", icon="📄", disabled=(has_kai("Le Sixième Sens") or has_kai("L'Orientation")))

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
