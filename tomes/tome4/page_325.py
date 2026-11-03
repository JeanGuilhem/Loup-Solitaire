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

check_inventory(current_page_number=325, book=4)

fr_text = """
Lorsque vous dégainez le Glaive de Sommer, la plainte du vent
retentit avec plus de force, comme animée d'une soudaine fureur.
En voyant étinceler la lame d'or qui tua Vashna, Maître des
Ténèbres, Barraka a un bref mouvement de recul. Il se reprend
aussitôt, mais la menace de l'arme magique a quelque peu
ébranlé la puissance de sa volonté et il ne pourra pas utiliser
contre vous sa redoutable force mentale au cours du combat. Il
reste cependant invulnérable à la Discipline Kaï de la Puissance
Psychique. Il vous faut à présent affronter l'aristocrate renégat,
armé de son cimeterre, en un combat sans merci qui ne
s'achèvera que par la mort de l'un de vous deux.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("BARRAKA", 25, 29)], psychic_immune=True)
    if outcome == "win":
        st.write_stream(stream_text("Si vous êtes vainqueur, rendez-vous au :"))
        st.page_link("tomes/tome4/page_350.py", label="350", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
