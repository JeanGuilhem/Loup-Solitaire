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

check_inventory(current_page_number=230, book=6)

fr_text = """
« Portons un toast à notre vaillant ami ! » crie le soldat au visage
grêlé. « Honneur dans la bataille ! » s'écrie l'homme aux cheveux
roux à votre gauche. « Et une bourse bien remplie pour le
vainqueur ! » dit le troisième soldat. Ils éclatent de rire puis
lèvent joyeusement leurs chopes. Le visage entièrement caché
derrière leurs chopes, ils commencent à boire avidement. Au
bout d'une minute, ils reposent bruyamment leurs chopes vides
sur la table. La forte bière dissipe bientôt leurs dernières réserves
à votre égard et ils deviennent intarissables sur eux-mêmes. Vous
en profitez pour leur demander ce qu'ils savent au sujet de la
Pierre de la Sagesse. « Légende ! » s'écrie l'homme roux entre
deux hoquets. « Légende ? Pas du tout ! interrompt le grêlé. Elle
existe bel et bien, mais elle a été perdue il y a de nombreuses
années. Elle détient un pouvoir extraordinaire qui peut faire de
n'importe quel homme un roi. » A ces mots, les deux autres
soldats se mettent à ricaner doucement mais le grêlé poursuit
sans leur prêter attention : « La Pierre de la Sagesse était
autrefois incrustée dans le trône de Lyris qui se trouvait à Varetta
dans la Tour du Roi. Mais, au cours de la Guerre de la Pierre de
la Sagesse qui eut lieu il y a des centaines d'années, elle fut volée
par un prince salonien appelé Kaskor. Il fixa la Pierre sur un
sceptre en or qu'il utilisait au cours des combats pour encourager
ses hommes. Il croyait être devenu invulnérable, mais il n'en
était rien. Il fut tué à Rhem lors d'une bataille à bord de son
bateau royal. En mourant, il lâcha le sceptre qui disparut avec la
Pierre dans les eaux profondes de la rivière Storn. Mais l'histoire
ne s'arrête pas là. Aussitôt après, le bruit courut que l'on avait
enfin retrouvé la Pierre, mais cela se révéla dénué de tout
fondement. Quoi qu'il en soit, la légende raconte que quiconque
brandit la Pierre de la Sagesse devient aussitôt le chef incontesté
de tous les Pays de Storn. C'est pour cette raison que la Pierre de
la Sagesse est recherchée par de nombreux hommes ambitieux et
sans scrupules qui rêvent de parvenir au pouvoir. Si vous
souhaitez en savoir plus long, vous devriez vous rendre à Varetta.
Là-bas, beaucoup d'hommes très érudits ont consacré leur vie à
l'étude de la Pierre de la Sagesse : les savants et sages de la rue
des Chaudronniers. Ils pourront vous apporter une aide
précieuse. » Vous remerciez le soldat pour ces renseignements
puis vous prenez congé du petit groupe.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez à présent commander quelque plat, rendez-vous au :"))
    st.page_link("tomes/tome6/page_172.py", label="172", icon="📄")

    st.write_stream(stream_text("Si vous préférez vous diriger directement vers le comptoir pour vous enquérir d'une chambre pour la nuit, rendez-vous au :"))
    st.page_link("tomes/tome6/page_232.py", label="232", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
