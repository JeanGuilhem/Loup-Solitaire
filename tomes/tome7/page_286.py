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

check_inventory(current_page_number=286, book=7)

fr_text = """
Une escorte de gardes en armure vous emmène de force le long
d'un couloir en acier, entre deux rangées de serviteurs de Zahda
qui vous crachent dessus et vous martèlent le visage à coups de
poing au passage. Vous avancez sous les huées et les
malédictions jusqu'à une immense porte en fer. Les gardes
débarrassent vos poignets sanglants et meurtris des chaînes qui
les liaient tout en prévenant toute tentative de fuite en vous
entourant de leurs lances. Soudain, la porte s'ouvre et vous êtes
jeté dans une fosse puante sous les acclamations de la foule.
« Bienvenue dans le labyrinthe ! » ricane Zahda d'une voix cruelle
quelque part au-dessus de votre tête. Vous vous remettez
péniblement debout et vous levez la tête. Vous apercevez un voile
de brouillard tourbillonnant où brille une faible lueur. Le
brouillard se condense, et la lueur prend graduellement la forme
d'un crâne humain. Des yeux verts dans des orbites osseuses
vous fixent d'un air menaçant, et le crâne décharné est coiffé
d'une perruque poudrée ressemblant à celle que portent les juges
de haute cour. « Vous êtes venu ici pour tuer, mais vos plans ont
été déjoués, et vous devez maintenant en assumer les
conséquences, retentit la voix du crâne. Vous avez été condamné
à entrer dans le labyrinthe de Zahda. Si vous parvenez à vous en
échapper, vous aurez la vie sauve, mais si vous échouez, vous
mourrez sûrement ; une fin normale pour celui qui est venu ici
semer la mort. » Le crâne disparaît ensuite dans le brouillard, et
un silence de mort règne dans la fosse. Une ombre semi-circulaire
se forme sur le mur, devant vous ; l'ombre grandit et
devient de plus en plus sombre. Elle ressemble maintenant à
l'entrée d'une grotte ou d'un tunnel. Soudain, une rafale d'air
froid venant des ténèbres s'engouffre dans la fosse, et vous
comprenez que vous vous trouvez devant l'entrée du labyrinthe.
« Entrez ! ordonne la voix. Entrez ou mourez sur place ! » Ce
n'est pas une vaine menace : un carreau d'arbalète s'enfonce dans
le sable, à quelques centimètres de votre pied, et un cliquetis
métallique vous avertit qu'un autre carreau va suivre si vous
n'obéissez pas. A contrecœur, vous pénétrez dans le labyrinthe de
Zahda.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_111.py", label="111", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
