import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    kai_rank,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=113, book=4)

fr_text = """
Vous pénétrez dans la forêt et vous descendez le flanc de la
colline en direction de la rivière Xane. Au bout de quelques
mètres, la végétation devient trop dense pour que vous puissiez
continuer à cheval. A contrecœur, vous faites donc signe à vos
hommes de descendre de selle pour poursuivre votre chemin à
pied. Vous parvenez bientôt au bord de la rivière dont vous
remontez le courant parsemé d'écume. Vous escaladez ainsi
plusieurs terrasses rocheuses dont la surface a été rendue
parfaitement lisse par la force du torrent. Vous parvenez ensuite
à un endroit où de petits cours d'eau se jettent dans la rivière.
Vous apercevez alors six brigands qui donnent des coups de
lance dans l'eau bouillonnante le long de la berge. Sur la rive
opposée, des poissons gris sont entassés à côté d'un chariot
attelé. Vous reconnaissez aussitôt ce chariot : il appartient à la
cavalerie du Sommerlund.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous avez atteint le rang Kaï de Guerrier, rendez-vous au :'))
    if kai_rank() >= 8:
        st.page_link("tomes/tome4/page_166.py", label="166", icon="📄")
    else:
        st.write_stream(stream_text("Vous n'avez pas atteint le rang Kaï de Guerrier."))
        st.page_link("tomes/tome4/page_166.py", label="166", icon="📄", disabled=True)

    st.write_stream(stream_text('Sinon, vous pouvez lancez une attaque surprise contre les bandits en vous rendant au :'))
    st.page_link("tomes/tome4/page_14.py", label="14", icon="📄", disabled=kai_rank() >= 8)

    st.write_stream(stream_text("Si vous préférez essayer de traverser la rivière à l'abri des rochers, rendez-vous au :"))
    st.page_link("tomes/tome4/page_316.py", label="316", icon="📄")

    st.write_stream(stream_text("Enfin, si vous pensez qu'il serait imprudent de traverser à cet endroit, vous pouvez rebrousser chemin en vous rendant au :"))
    st.page_link("tomes/tome4/page_232.py", label="232", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
