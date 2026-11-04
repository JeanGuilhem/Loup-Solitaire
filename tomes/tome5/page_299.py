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

check_inventory(current_page_number=299, book=5)

fr_text = """
Le Vordak retire ses doigts osseux, dégoulinants de sang, du dos
de l'Itikar puis il saisit la masse d'armes de métal noir accrochée
à sa ceinture. Il lève l'arme au-dessus de sa tête, prêt à vous
l'écraser violemment sur le crâne. Vous ne pouvez éviter son
attaque et vous devez combattre la créature jusqu'à ce que mort
s'ensuive.
A moins que vous ne maîtrisiez la Discipline du Bouclier
Psychique, réduisez de 2 points votre total d'HABILETÉ, car le
Vordak est en train d'utiliser son pouvoir psychique. En
revanche, il est insensible à la puissance psychique dont vous
pourriez vous servir contre lui.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("VORDAK", 17, 25)], psychic_attack=True, psychic_immune=True)
    if outcome == "win":
        st.write_stream(stream_text("Si vous gagnez le combat, rendez-vous au :"))
        st.page_link("tomes/tome5/page_203.py", label="203", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
