import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=165, book=7)

fr_text = """
En vous réveillant, la vision qui s'offre à vos yeux est tellement
stupéfiante que vous avez l'impression d'être en plein rêve.
Devant vous s'étend une salle démesurée, toute dallée de marbre
poli, qui s'étage en gradins comme un gigantesque amphithéâtre.
Au centre de la pièce s'enfonce un grand puits surmonté d'une
estrade en fer noir que viennent lécher les flammes qui jaillissent
des profondeurs du puits en grondant. Des centaines de
silhouettes sombres sont assises sur les gradins. Sous les
capuchons qui enveloppent leur tête, vous sentez des regards
froids et cruels vous regarder fixement comme autant d'épingles
chauffées à blanc. Un murmure rauque parcourt l'assistance, et
vous éprouvez une sinistre prémonition. Soudain, le son grave
d'un gong retentit, et une incantation gémissante s'élève des
gradins. Vous êtes pris d'une irrésistible envie de fuir au plus vite
cet endroit infernal, mais vos poignets sont solidement liés et
attachés à un gros anneau de bronze fixé dans le mur, au-dessus
de votre tête. « Que le jugement commence ! » ordonne une voix
puissante. A ces mots, la foule se répand en clameurs hostiles, et
les spectateurs encapuchonnés se lèvent comme un seul homme.
C'est alors qu'un faisceau de lumière vient inonder l'estrade. Un
homme décharné, aux cheveux blancs, est assis sur un grand
trône en or massif étincelant. Deux cristaux sont suspendus en
l'air, au-dessus de sa tête : l'un est aussi pur et transparent qu'un
diamant, l'autre aussi noir qu'une tombe. Les deux pierres sont
reliées par un arc électrique qui court de l'une à l'autre en
grésillant. La lueur vive et bleutée qui s'en dégage projette une
ombre fantomatique sur le seigneur assis sur le trône. « Intrus,
commence ce dernier d'une voix douce et glaciale à la fois, tu es
venu à Kazan-Oud dans le dessein de tuer. Je suppose que ces
couards d'Elzian t'ont promis une récompense en échange de ma
mort, n'est-ce pas ? » A ces mots, un murmure de réprobation
parcourt la foule, étouffant la réponse que vous auriez pu donner
pour votre défense. Le seigneur se lève alors lentement de son
trône, puis il se tourne vers ses sujets, les bras tendus, comme
pour recevoir le témoignage de leur adoration. Tandis que la
rumeur d'hostilité va en s'amplifiant de gradin en gradin, votre
regard est soudain attiré par le cristal clair qui plane au-dessus
du trône : un éclat doré brille à présent en son centre. Vous
reconnaissez alors l'objet de votre quête : vous avez sous les yeux,
à quelques mètres de vous, la Pierre de la Sagesse de Herdos !
Mais la voix du Seigneur, maintenant rauque et cruelle, vient
vous tirer de vos pensées : « Quel est votre verdict, mes chers
sujets ? » « Coupable, Seigneur Zahda ! » répond à l'unisson la
foule hargneuse. « Et la sentence ? » reprend le maître. « Le
Labyrinthe ! Le Labyrinthe ! » hurle-t-on en retour.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    sommerswerd = has_item("GLAIVE DE SOMMER")
    st.write_stream(stream_text("Si vous possédez le Glaive de Sommer, rendez-vous au :"))
    st.page_link("tomes/tome7/page_335.py", label="335", icon="📄", disabled=not sommerswerd)

    st.write_stream(stream_text("Si vous ne possédez pas cet Objet Spécial, rendez-vous au :"))
    st.page_link("tomes/tome7/page_264.py", label="264", icon="📄", disabled=sommerswerd)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
