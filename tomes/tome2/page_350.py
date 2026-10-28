import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=350, book=2)

fr_text = """
La ville de Holmgard a beaucoup souffert depuis votre départ. Le long
des quais, nombre de maisons et de boutiques ne sont plus que cendres
désormais. L'armée maléfique des Maîtres des Ténèbres encercle les
murailles et leurs effroyables machines de guerre maintiennent la cité
sous un déluge de feu qui déchire la nuit sans relâche. Les habitants
épuisés et affamés combattent du mieux qu'ils peuvent les incendies qui
se déclarent un peu partout dans la ville sous l'effet des projectiles
enflammés. Lorsqu'elle entre dans le port, la flotte durenoraise est tout
d'abord accueillie par des cris de désespoir; les assiégés ont cru en effet
qu'il s'agissait là de vaisseaux ennemis venus en renfort. Mais, lorsque
les premiers soldats descendent sur le quai en déployant l'étendard de
Durenor, la nouvelle a tôt fait de se répandre de l'arrivée des alliés. Les
cris de désespoir se changent alors en hurlements de joie. « Le Seigneur
Kaï est de retour ! » s'exclame-t-on bientôt dans toute la capitale.
Vous vous tenez debout au sommet d'une haute tour, qui défend la plus
grande porte de la ville lorsque les premières lueurs de l'aube naissent à
l'horizon. Des milliers et des milliers d'ennemis aux uniformes noirs
sont massés autour des murs de la cité, grouillant comme des cancrelats
le long des tranchées qui sillonnent la plaine. Au milieu de cette horde,
une tente rouge a été dressée qui porte l'emblème de Zagarna, Seigneur
de Kaag, l'un des Maîtres des Ténèbres, venu d'Helgedad. L'emblème
représente un crâne fracassé. Zagarna a pour ambition de détruire
Holmgard et il souhaite plus que tout conduire son armée à la victoire
sur la Maison d'Ulnar pour se proclamer ensuite roi du Sommerlund.
Mais la victoire ne sera pas pour aujourd'hui, car bientôt vous levez au-
dessus de votre tête le Glaive de Sommer : au même instant, un rayon
de soleil vient se refléter sur la pointe de l'épée d'or et un jaillissement
de flammes blanches et aveuglantes parcourt toute la longueur de sa
lame. La puissance du Glaive vous emplit d'une fantastique énergie.
Tout votre corps s'anime, vous vous sentez frémir de la tête au pied et
d'un geste ample vous abaissez l'Arme fantastique en pointant sa lame
sur la tente de Zagarna. Dans un formidable roulement de tonnerre, un
rayon blanc jaillit alors de l'épée magique et vient frapper la tente qui
explose dans une tempête de feu, un champignon enflammé s'élevant
jusqu'au ciel. Un épouvantable hurlement retentit aussitôt dont l'écho
semble déchirer les nuées: c'est Zagarna, le Maître des Ténèbres, qui
vient de succomber sous la vengeance du Glaive. Saisis de terreur, les
soldats aux uniformes noirs se lèvent des tranchées et se précipitent en
déroute loin des murs de Holmgard. L'impossible est survenu : leur
chef invincible a été terrassé. Le Glaive de Sommer est revenu chasser
l'envahisseur, et l'armée du Sommerlund aidée de ses alliés de Durenor
se lance sans attendre à la poursuite des ennemis défaits qui courent
aveuglément en direction des Monts Durncrag ; le triomphe est total :
Holmgard est libérée et vos frères Kaï vengés.
Votre vie d'aventures, cependant, ne fait que commencer, car un
nouveau défi vous attend, vous et le Glaive de Sommer, dans le
troisième volume de la série du Loup Solitaire :
LES GROTTES DE KALTE
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        st.balloons()
    st.success(
        "**Mission accomplie !** Grâce au Glaive de Sommer, Zagarna est terrassé et Holmgard est libérée. "
        "Le Loup Solitaire peut reprendre la route dans le tome 3, *Les Grottes de Kalte*."
    )
    st.page_link("tomes/tome3/debut.py", label="Continuer avec le tome 3", icon="📜")
    st.page_link("accueil.py", label="Retour à l'accueil", icon="🏠")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
