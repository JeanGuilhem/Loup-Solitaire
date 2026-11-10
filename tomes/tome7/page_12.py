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

check_inventory(current_page_number=12, book=7)

fr_text = """
« Nous sommes des hommes morts si nous restons ici, dit le
guerrier avec l'accent fort prononcé des lointaines provinces de la
Storn. Suivez-moi, je crois qu'il vaut mieux trouver un tunnel où
nous serons en sécurité, avant qu'ils ne lâchent un Trakka à nos
trousses. Si ce monstre arrivait à déceler notre odeur, nous
aurions immédiatement toute la horde des créatures de Zahda
sur les talons ! » Vous suivez l'homme à travers un labyrinthe
inextricable de tunnels et de salles descendant toujours plus bas,
d'escalier en escalier et de galerie en galerie, dans les
profondeurs de ce monde souterrain. Vous n'échangez pas un
mot jusqu'à ce que vous fassiez halte dans une petite pièce où
règne une forte odeur de moisi, et dont l'entrée est partiellement
dissimulée par un gros bloc de pierre rouge. « Depuis combien
de temps errez-vous dans ce dédale ? » vous demande votre
compagnon. Lorsque vous lui apprenez que cela ne fait que
quelques heures, vous voyez une expression de surprise et de
déception se peindre sur son visage. « Quel dommage ! J'aurais
affronté et combattu les Dhax si j'avais su que nous étions si près
de la surface ! » dit-il en hochant la tête d'un air triste. L'homme
se présente alors à vous : il s'appelle Tavig et vient de Suentina,
une cité de l'ouest de la Slovie. Il y a un an, sa sœur fut capturée
par Sadzar, un esclavagiste de Gzor. Le bateau à bord duquel elle
s'était embarquée fut en effet attaqué au large de l'île de Lipo par
des pirates à la solde de cet homme cruel. Sadzar fixa le prix de
sa rançon à 1 000 Pièces d'Or, et Tavig jura de rassembler cette
somme afin de sauver sa sœur, dût-il en mourir. C'est ainsi qu'au
mépris de toutes les mises en garde, il partit pour offrir ses
services aux Anciens Mages de Dessi. Il leur proposa de les
débarrasser du fléau de Kazan-Oud contre 1 000 Pièces d'Or. Les
Anciens Mages acceptèrent le marché et lui firent traverser
l'écran magique. Cela se passait il y a un an... « Il est absolument
impossible pour un homme seul d'anéantir Zahda, celui qui
règne sur cette sinistre forteresse, car ses pouvoirs sont encore
plus grands que les Anciens le soupçonnent. J'ai essayé, mais j'ai
échoué. J'ai été capturé deux fois, par deux fois j'ai pu
m'échapper de ce dédale ; maintenant, mon seul souhait est de
quitter à jamais cet endroit de cauchemars. Je suis devenu un
coureur de fond souterrain, un survivant, un fugitif au royaume
des ténèbres de Zahda, mais je crois que je suis arrivé au bout de
mes forces. » Sur ces mots, Tavig dégaine son épée en marchant
vers l'entrée. Après avoir scruté le couloir, il vous dit : « A
présent, chacun de son côté, étranger ! » Puis il part en courant.
Vous lui criez de vous attendre, mais l'homme disparaît au
détour du tunnel sans que vous puissiez en apprendre plus long
sur Kazan-Oud et ses mystères.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous voulez vous lancer à la poursuite de Tavig, rendez-vous au :'))
    st.page_link("tomes/tome7/page_119.py", label="119", icon="📄")

    st.write_stream(stream_text('Si vous préférez continuer à faire route tout seul, rendez-vous au :'))
    st.page_link("tomes/tome7/page_308.py", label="308", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
