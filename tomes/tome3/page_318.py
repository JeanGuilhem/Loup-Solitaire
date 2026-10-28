import streamlit as st
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

check_inventory(current_page_number=318, book=3)

fr_text = """
Vous devinez que le Bakanal cherche désespérément quelque
chose à manger. Votre Discipline Kaï, cependant, ne vous sera
d'aucune utilité : en effet, à présent qu'il a senti l'odeur des
chiens Kanu, il vous sera impossible de lui ordonner de quitter le
campement. Vous n'ignorez pas que les Bakanals sont de
courageux chasseurs qui n'ont peur de rien, ou plutôt, qui n'ont
peur que d'une seule chose : le feu. Vous saisissez alors une
torche, vous l'allumez et vous vous précipitez hors de la tente. Il
fait nuit noire et il tombe une neige épaisse, mais un mouvement
à votre droite trahit la présence du Bakanal qui s'avance vers
vous. Au moment où il s'apprête à bondir, il aperçoit la flamme
de la torche et pousse aussitôt un hurlement de terreur. Une
seconde plus tard, il a fait volte-face et il disparaît dans la nuit.
Les chiens Kanu sont sains et saufs, mais pour être sûr que les
Bakanals ne reviendront pas, vous décidez, cette nuit-là, de
prendre des tours de garde en conservant une torche et une arme
à portée de main.
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
