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

check_inventory(current_page_number=38, book=4)

fr_text = """
Il ne reste plus rien dans la carcasse calcinée du chariot. Le bois
est entièrement noirci et les garnitures de métal se sont
déformées sous l'effet de la chaleur. Ces débris, cependant,
confirment vos soupçons. C'est là ce qui reste d'un chariot de la
cavalerie du Sommerlund, l'un des trois qui ont quitté Ruanon il
y a plus d'un mois, escortés par les hommes du capitaine Gayal.
Tandis que vous vous trouvez devant le chariot, essuyant les
cendres de vos mains, l'un de vos patrouilleurs pousse soudain
un hurlement de douleur. Jetant un coup d'œil dans sa direction,
vous le voyez tomber de son cheval, un disque d'acier acéré
enfoncé dans la poitrine. « Une embuscade ! Tout le monde à
l'abri ! » Alors que vous donnez cet ordre, d'autres disques
mortels sont lancés des arbres, traversant l'air en sifflant. Les
chevaux, pris de panique, s'enfuient en tous sens, vos hommes
s'accrochant désespérément aux rênes. Vos agresseurs cachés
disparaissent aussi vite qu'ils sont venus, mais trois de vos
soldats ont été tués. Après avoir enterré les morts, il vous faut à
présent prendre une décision. Il ne reste en effet que quatre
hommes à vos côtés et l'ennemi peut revenir à tout moment pour
achever sa sinistre besogne.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez poursuivre votre chemin le long de la grand-route en galopant vers Ruanon, rendez-vous au :"))
    st.page_link("tomes/tome4/page_297.py", label="297", icon="📄")

    st.write_stream(stream_text("Si vous préférez éviter la route principale et continuer en empruntant le chemin orienté à l'est, rendez-vous au :"))
    st.page_link("tomes/tome4/page_15.py", label="15", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
