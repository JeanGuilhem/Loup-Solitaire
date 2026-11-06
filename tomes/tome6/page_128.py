import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, ls_death

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=128, book=6)

fr_text = """
Votre cœur bat la chamade tandis que le Yamsark approche en
pataugeant bruyamment dans la boue immonde qui recouvre le sol.
Des glapissements odieux vous parviennent en écho de toute part,
se mêlant les uns aux autres en un crescendo assourdissant. Et,
subitement, vous prenez conscience de l'horrible réalité : il
n'y a pas un Yamsark, mais deux ! vous avez, par mégarde,
pénétré dans leur repaire, et vous voilà maintenant pris au
piège. Vous vous battez vaillamment mais, dans l'atmosphère
sombre et confinée de cet antre, les Yamsarks ne tardent pas à
l'emporter et à vous mettre en pièces. Votre aventure et votre
vie s'achèvent, hélas ! ici.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    show_illustrations()
    ls_death()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
