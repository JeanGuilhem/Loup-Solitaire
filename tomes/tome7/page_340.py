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

check_inventory(current_page_number=340, book=7)

fr_text = """
Vous lui faites part de votre quête et de l'aide des Anciens Mages
qui vous ont permis de pénétrer dans Kazan-Oud. Vous lui
racontez ensuite votre voyage à travers les airs jusqu'à Herdos, à
bord du vaisseau spatial du Seigneur Paido, et vous remarquez
de grosses larmes qui coulent de ses yeux aveugles. « Mon nom
est Kasin, dit-il tristement. Le Seigneur Paido est mon frère. »
Vous vous apitoyez sur le sort de ce malheureux guerrier, car
vous savez qu'il est condamné à mourir : la cécité est le dernier
stade du Takadea, la maladie qui ravage son corps. « On ne peut
plus me sauver maintenant, dit-il, le visage déformé par la
douleur. Mais je vous aiderai dans votre quête, Seigneur Kaï.
Écoutez-moi attentivement : au bout du couloir, un escalier
descend vers la salle du trône de Zahda. Au-dessus du trône se
trouve la Pierre de Sagesse que vous cherchez ; mais attention !
la puissance de Zahda est associée à une pierre maudite dont il
tire tout son pouvoir. Cette gemme provient du royaume de
Naaros, et vous devrez la détruire d'abord, sinon vous périrez
sûrement. Malheureusement, je ne peux pas vous aider à fuir de
Kazan-Oud car j'ai moi-même été capturé bien avant d'atteindre
la surface. Si vous parvenez quand même à regagner la plage,
allez jusqu'à la vieille jetée : vous y trouverez mon bateau,
dissimulé sous les marches. » Il vous prend la main
amicalement, le visage maintenant calme et paisible. « Lorsque
vous retournerez à Elzian, dites à mon frère que je ne suis pas
mort en vain. Que les dieux vous protègent, Loup Solitaire. »
Vous entendez les gardes qui s'approchent et vous devez quitter
la cellule. Avant de laisser votre compagnon, vous lui promettez
que sa bravoure sera immortalisée dans les légendes des
Vakeros, ses compagnons d'armes.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_142.py", label="142", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
