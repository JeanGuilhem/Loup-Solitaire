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

check_inventory(current_page_number=93, book=4)

fr_text = """
Quatre brigands au visage couvert de verrues sont assis autour
d'une table ronde sur laquelle est étalé un plan des mines de
Maaken. Votre attaque est si fulgurante qu'ils n'ont pas même le
temps de manifester une réaction de surprise. Trois d'entre eux
tombent morts avant même d'avoir pu dégainer leur arme. Le
quatrième s'écarte de ses compagnons et tire son épée. Il se
précipite alors sur vous, et vous pouvez lire dans son regard
brûlant une ardente soif de vengeance.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("GUERRIER PILLARD", 15, 26)])
    if outcome == "win":
        st.write_stream(stream_text("Si vous êtes vainqueur, rendez-vous au :"))
        st.page_link("tomes/tome4/page_2.py", label="2", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
