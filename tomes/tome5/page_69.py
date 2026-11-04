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

check_inventory(current_page_number=69, book=5)

fr_text = """
Vous reprenez lentement connaissance, le corps meurtri par de multiples contusions et les muscles engourdis par de
douloureuses courbatures. Vous ouvrez péniblement les yeux et
vous découvrez avec horreur l'endroit où vous vous trouvez !
Vous gisez à même le sol dur et froid d'une cellule de prison ! La
pièce est nue, excepté une paillasse crasseuse située sous une
étroite fenêtre à barreaux. Des cafards, dont certains atteignent
la taille d'une souris, grouillent le long d'un caniveau nauséabond
qui coule sous une grille encastrée dans le sol. On ne vous a pas
lié les mains et vous pouvez par conséquent vous redresser pour
vous adosser contre la porte de la cellule. Seul un léger courant
d'air venant du couloir de la prison vient renouveler l'air moite et
malsain que vous respirez. Soudain, vous percevez des bruits de
pas se rapprochant peu à peu, puis un tintement de clés et enfin
le grincement d'une porte tournant sur ses gonds. La porte se
referme avec un bruit sourd et vous entendez à nouveau des pas :
quelqu'un s'arrête devant la porte de votre cellule et s'exclame
d'une voix forte : « Alors, Sefrou, on dort pendant le service ? Un
jour, tu te retrouveras de l'autre côté de cette porte, si le
Capitaine te surprend ! » Vous entendez une chaise racler le sol
et une voix indignée s'écrier : « Maudit sois-tu Hadj ! Le Zakhan
ne veut pas qu'on conduise l'Homme du Nord à la grande salle
avant le crépuscule ; j'aurais pu dormir encore deux heures ! » «
Tais-toi, Sefrou ! grogne la première voix, et écoute-moi bien :
plusieurs objets intéressants ont été trouvés sur l'Homme du
Nord. Il y en a sans doute pour cher, d'après ce que je sais. Ce
serait dommage de les laisser perdre, pas vrai ?... ! » Les geôliers
partent tous deux d'un rire complice et se mettent à imaginer la
belle vie qu'ils pourront mener en ville après qu'ils auront vendu
votre équipement. « Je vais aller jeter un coup d'œil sur notre
pensionnaire, dit l'un des hommes. J'espère qu'il apprécie notre
hospitalité ! » Le volet du judas s'ouvre au-dessus de vous et vous
entendez l'homme pousser un cri de surprise : « Il n'est plus là !
Il s'est enfui ! Par le Majhan, nos têtes vont y passer ! » Soudain,
vous réalisez qu'on ne peut pas vous voir de l'extérieur, puisque
vous êtes collé à la porte. « Laisse-moi voir », souffle le second
Garde, impatient de s'en assurer par lui-même. Soudain, la clé
tourne dans la serrure. Voilà peut-être votre seule chance de vous
échapper.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez attaquer les Gardes dès que la porte s'ouvrira, rendez-vous au :"))
    st.page_link("tomes/tome5/page_138.py", label="138", icon="📄")

    st.write_stream(stream_text("Si vous préférez vous éloigner de la porte et attendre, debout, au centre de la cellule, rendez-vous au :"))
    st.page_link("tomes/tome5/page_85.py", label="85", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
