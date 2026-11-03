import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, handle_repas, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=139, book=4)

fr_text = """
Vous envoyez trois de vos hommes dans la vallée avec ordre de
reconnaître la grand-route et d'inspecter la forêt qui la borde
pour y découvrir la présence d'éventuels brigands. Vous donnez
pour consigne à vos éclaireurs de revenir faire leur rapport dans
deux heures. Vous avez faim à présent et il vous faut prendre un
Repas, sinon vous perdrez 3 points d'ENDURANCE. En dépit de
la fatigue, vos patrouilleurs, tous leurs sens en alerte, sont prêts à
l'action. En effet, il y a maintenant plus de trois heures que vos
éclaireurs sont partis et aucun d'entre eux n'a encore donné signe
de vie.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    handle_repas()

    st.write_stream(stream_text('Si vous souhaitez envoyer trois autres éclaireurs dans la vallée, rendez-vous au :'))
    st.page_link("tomes/tome4/page_206.py", label="206", icon="📄")

    st.write_stream(stream_text("Si vous préférez attendre l'aube pour partir à leur recherche, rendez-vous au :"))
    st.page_link("tomes/tome4/page_330.py", label="330", icon="📄")

    st.write_stream(stream_text("Enfin, si vous estimez qu'il est beaucoup trop dangereux de rester ici, vous pouvez repartir vers l'est en direction de la ville d'Eshnar. Rendez-vous pour cela au :"))
    st.page_link("tomes/tome4/page_92.py", label="92", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
