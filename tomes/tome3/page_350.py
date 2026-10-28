import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=350, book=3)

fr_text = """
La multitude de couleurs s'estompe et vous ressentez soudain
une soudaine chute de température. Vous vous trouvez à présent
sur la banquise de Liouk, à moins de 800 mètres de l'endroit où
le Cardonal est ancré. Loi-Kymar et Vonotar sont auprès de vous
et tous deux frissonnent dans la fraîcheur de l'air du matin.
Quelques minutes plus tard, l'homme de vigie du Cardonal vous
aperçoit et une chaloupe est immédiatement mise à la mer pour
venir vous chercher. Le capitaine vous accueille à bord du navire
en vous félicitant pour votre courage et votre habileté, tandis que
Vonotar le Traître est hissé sans ménagement sur le pont et
aussitôt enfermé à fond de cale. « Mais comment avez-vous fait
pour revenir si vite ? demande le capitaine incrédule, nous ne
vous attendions que dans dix jours. » « Disons, intervient Loi-
Kymar, que la sagesse d'un Seigneur Kaï et le savoir d'un
magicien de la Guilde peuvent parfois vaincre le temps lui-
même. » Une expression perplexe apparaît sur le visage du
capitaine, mais elle laisse place peu à peu à un sourire : il semble
qu'il ait compris à demi-mot ce que le magicien voulait dire.
Votre voyage de retour à Anskavern se déroule sans encombre,
mais vous êtes quelque peu attristé, cependant, par le souvenir
de vos guides courageux que vous avez dû laisser derrière vous.
Votre arrivée dans le port de la côte sommerlundaise est
attendue par une foule anxieuse de savoir ce qui s'est passé. On
craint en effet que votre retour si prompt ne soit un signe que
votre mission a échoué. Mais, lorsque la nouvelle se répand que
Vonotar le Traître a été capturé, il vous faut à nouveau montrer
tous vos talents de guerrier. Et cette fois, ironie du destin, c'est
Vonotar lui-même que vous devez défendre contre la foule
déchaînée qui monte à l'assaut de la prison d'Anskavern pour
lyncher l'infâme bossu. Vous parvenez malgré tout à protéger le
prisonnier et à l'amener à Toran où l'attend son procès. A l'aube
de la fête de Maesmarn, Vonotar le Traître est jugé par ses
anciens compagnons, rassemblés dans les sous-sols du temple
qui abrite la Guilde de l'Etoile de Cristal ; à l'issue des débats, il
est reconnu coupable de tous les terribles crimes qu'il a commis.
On le conduit alors en silence dans une salle du temple située
loin dans ses profondeurs et où se trouve l'Aveugloir : il s'agit
d'un point de passage vers d'infinies ténèbres, le seuil d'une
prison éternelle de laquelle il est impossible de s'échapper. Vous
êtes le vengeur de ses crimes et c'est à vous que revient la tâche
de précipiter le traître abject dans les limbes de l'Aveugloir. Votre
mission est désormais accomplie. Vous avez survécu aux Grottes
de Kalte et libéré le Sommerlund de la menace que Vonotar
faisait peser sur lui. Mais le feu des batailles et le défi d'une
nouvelle quête tout aussi désespérée vous attendent maintenant
dans le quatrième volume de la série du Loup Solitaire intitulé :
LE GOUFFRE MAUDIT
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        st.balloons()
    st.success(
        "**Mission accomplie !** Vonotar le Traître a été capturé et précipité dans l'Aveugloir : le Sommerlund "
        "est libéré de sa menace. L'aventure se poursuivra dans le tome 4, *Le Gouffre Maudit* (pas encore adapté)."
    )
    st.page_link("accueil.py", label="Retour à l'accueil", icon="🏠")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
