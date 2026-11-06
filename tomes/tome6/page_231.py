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

check_inventory(current_page_number=231, book=6)

fr_text = """
Vous aidez le Capitaine à transporter les deux grandes caisses en
bois qui contiennent ses achats. En sortant de la boutique de
l'apothicaire, il vous dit qu'il veut retourner au bateau le plus vite
possible car, explique-t-il, « mes hommes sont de bons soldats,
mais de piètres marins et, par ailleurs, je crains que, sans la
présence de leur chef, ils oublient leur tâche et qu'ils
commencent à s'endormir ». Ses craintes ne sont pas fondées et,
lorsque vous arrivez sur le quai, vous apercevez le Kazonara fin
prêt pour l'appareillage. « Larguez les amarres ! » crie le
Capitaine. La direction d'un bateau est pour lui quelque chose de
tout à fait nouveau qu'il semble beaucoup apprécier. « Nous
atteindrons Rhem à la nuit », dit-il joyeusement. Et en effet,
quelques heures plus tard, lorsque le soleil commence à décliner
à l'horizon, vous pénétrez dans le port de Rhem.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_124.py", label="124", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
