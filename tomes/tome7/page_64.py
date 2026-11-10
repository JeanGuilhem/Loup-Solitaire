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

check_inventory(current_page_number=64, book=7)

fr_text = """
A peine avez-vous fait quelques pas le long du couloir que vous
recevez un coup d'une rare violence en pleine poitrine. Vous
perdez l'équilibre. Lorsque vous relevez péniblement la tête, vous
apercevez une silhouette indistincte et fantomatique qui plane
au-dessus de vous : c'est un Guerrier-Squelette qui tient dans sa
main décharnée une lance ensanglantée. Il vient de vous infliger
une blessure mortelle. Votre vision se trouble et l'apparition
disparaît tandis que la vie vous échappe en même temps que
s'écoule votre sang. Votre aventure est, hélas ! terminée.
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
