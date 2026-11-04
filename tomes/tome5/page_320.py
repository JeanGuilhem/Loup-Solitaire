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

check_inventory(current_page_number=320, book=5)

fr_text = """
Le jour se lève derrière une colline basse semée d'arbustes
touffus. La Nef du ciel a fait route rapidement à travers les
ténèbres de la nuit et vous vous trouvez à présent dans les
contreforts des monts Koneshi, dont les replis rocheux pourront
dérober le vaisseau de l'espace aux regards indiscrets. A 25 km
au nord, au-delà d'une étendue de pierrailles et de broussailles
desséchées, se dresse le Tombeau du Majhan. Banedon et vous
vous remettez en route, soucieux de ne pas perdre de temps tant
que vous pouvez bénéficier de la protection de la nuit. A présent,
tandis que le disque rougeoyant du soleil s'élève lentement à
l'horizon, vous découvrez enfin le but de votre voyage. De
gigantesques fouilles ont mis à nu le cœur de cette terre aride en
creusant les alentours des tombeaux ancestraux. Des milliers de
Giaks, les serviteurs malveillants et rusés des Seigneurs des
Ténèbres, travaillent sans relâche sous les ordres des Drakkars
pour dégager de cette énorme carrière des tonnes de pierres et de
sable, portant péniblement leur lourd fardeau sur le dos jusqu'au
sommet du cratère. Non loin du bord de la carrière, un
campement de tentes noires entoure un grand dais voûté. A côté
de cet édifice se trouve une énorme créature ailée : un Zlan
impérial. Sa présence révèle clairement que le Seigneur des
Ténèbres Haakon est déjà sur les lieux. A cette pensée, un frisson
vous parcourt l'échine, mais vous reprenez courage en observant
les esclaves : le fait que ceux-ci continuent à travailler prouve que
leur mission n'est pas encore accomplie. En d'autres termes, le
Livre du Magnakaï n'a sûrement pas encore été découvert ! Il est
cependant impossible d'approcher des fouilles sans être vu. Vous
devrez attendre que la nuit soit tombée pour tenter de pénétrer
dans le Tombeau. Pendant ces longues heures d'attente, il a été
convenu que Banedon, de son côté, essaiera de trouver Tipasa. Il
est fort probable, en effet, que ce dernier est retenu prisonnier à
l'intérieur du campement, car les Seigneurs des Ténèbres ne le
tueront certainement pas avant d'avoir découvert le trésor qu'ils
cherchent avec tant d'acharnement. Au cours de cette journée,
vous devrez obligatoirement prendre un Repas, sans quoi vous
perdrez 3 points d'ENDURANCE.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    handle_repas(hunting=False)

    st.write_stream(stream_text('Rendez-vous ensuite au :'))
    st.page_link("tomes/tome5/page_286.py", label="286", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
