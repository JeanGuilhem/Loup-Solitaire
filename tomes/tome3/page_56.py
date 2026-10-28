import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=56, book=3)

fr_text = """
« Par ma foi ! Un Seigneur Kaï ! s'exclame-t-il, les yeux ronds de
stupeur. J'ai tant désiré retrouver ma liberté, tant attendu qu'on
vienne me délivrer de cette infernale prison ! Mais, bien que
l'espoir ne m'ait jamais quitté, je n'aurais pu penser que mon
sauveur serait un personnage aussi illustre ! » Au plus fort de son
exaltation, le vieil homme est soudain pris d'une quinte de toux ;
lorsqu'enfin il peut reprendre son souffle, il est pâle, épuisé, et ne
peut à nouveau parler que quelques minutes plus tard. « Je
m'appelle Loi-Kymar, dit-il, je suis l'un des Anciens de la Guilde
des Magiciens de Toran. » Il vous montre alors, sous sa toge en
lambeaux, un pendentif en Étoile de Cristal, le symbole de la
guilde. La guilde est connue sous le nom de la Confrérie de
l'Étoile de Cristal et le magicien vous donne ainsi la preuve
tangible de son identité. Vous lui demandez ensuite comment il
se fait qu'il soit emprisonné ici, à Ikaya, à plusieurs centaines de
kilomètres de sa ville natale de Toran. « C'est Vonotar, ce traître
abject qui est responsable de mon tourment. Avant l'invasion du
Sommerlund par les Maîtres des Ténèbres, il a trahi les Maîtres
Kaï pour gagner de nouveaux pouvoirs, les sombres pouvoirs de
la mort et de l'obscurité. Il ne parvint pas, cependant, à remplir
le rôle qui lui avait été attribué dans la stratégie guerrière de ses
maîtres maléfiques. Or, les Maîtres des Ténèbres ne peuvent
tolérer une telle faiblesse, leur esprit monstrueux ignore la pitié.
Dans l'amertume de la défaite, ils ont cherché à tuer Vonotar
pour le punir du crime d'avoir échoué. Vonotar, quant à lui,
savait que le moyen d'échapper à leur vengeance se trouvait en
ma possession : ma Crosse de la Guilde a en effet le pouvoir de
transporter instantanément d'un lieu à un autre une personne ou
un objet. Il essaya donc de me la voler pour s'enfuir ainsi à Ikaya
où il serait en sûreté. Il apprit bien vite, cependant, que les
pouvoirs de la Crosse magique ne sont pas à la portée du premier
venu ; je suis le seul, en effet, à connaître son secret. Furieux, il
menaça de tuer toute ma famille si je refusais de l'amener
jusqu'ici à l'aide de la Crosse. Je n'avais donc pas d'autre choix
que d'accepter. Depuis ce temps, je suis resté prisonnier dans
cette cellule. Mais, en dépit des tortures physiques et mentales
que Vonotar m'a fait subir, je ne lui ai jamais révélé le secret de la
Crosse de la Guilde qu'il conserve, je le sais, dans la salle du
Trône du Brumalmarc. Si je lui disais ce secret, ma vie ne
vaudrait plus très cher. » Vous expliquez alors à Loi-Kymar la
nature de votre mission et vous lui racontez la suite
d'événements qui vous a amené à le rencontrer. Il vous propose
aussitôt de vous montrer le chemin qui mène à la salle du Trône
du Brumalmarc, où Vonotar exerce ses pouvoirs de chef
suprême. Et si vous parvenez à retrouver la Crosse de la Guilde, il
vous promet de vous transporter instantanément jusqu'au point
de la côte où se trouve ancré le Cardonal. Vous pourrez ainsi
rejoindre le navire à temps. Pour la première fois depuis que
vous êtes tombé dans les Grottes de Kalte, vous avez le sentiment
que votre mission est sur la voie du succès.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_192.py", label="192", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
