import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=204, book=3)

fr_text = """
Les Bakanals sont des créatures féroces et dangereuses qui n'ont
peur que d'une chose : le feu. Saisissant alors une torche, vous
l'allumez et vous sortez de la tente. Le vent souffle beaucoup plus
fort qu'au moment où vous avez installé votre camp et la neige
poudreuse est soulevée en petits tourbillons qui vous picotent les
yeux. Une ombre mouvante à votre droite trahit la présence du
Bakanal qui s'avance vers vous à grands bonds. Mais au moment
où il s'apprête à vous sauter dessus, il aperçoit la flamme
vacillante de votre torche et pousse un hurlement de terreur.
Quelques secondes plus tard, il a disparu dans l'obscurité. Vous
constatez bientôt que tous les chiens Kanu sont sains et saufs,
bien qu'un peu nerveux, ce qui n'a rien d'étonnant. Pour être sûr
que le Bakanal n'attaquera plus, vous prenez des tours de garde
en tenant à portée de main armes et torches.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome3/page_134.py", label="134", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
