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

check_inventory(current_page_number=1, book=4)

fr_text = """
Pendant trois jours vous menez votre détachement de
patrouilleurs à travers les plaines fertiles situées au sud du
Sommerlund. C'est là la première étape de votre voyage. Les
champs qui vous entourent sont entièrement dépourvus d'arbres
et vous n'apercevez que de vastes surfaces de blé qui semblent
s'étendre à l'infini. Bien que vous soyez à cheval, les épis de blé
vous arrivent au-dessus du genou et vos montures paraissent
nager dans un immense océan d'un jaune éclatant où
apparaissent parfois un sentier ou un groupe de fermes isolées.
Les habitants de la région vous accueillent avec chaleur, mais
vous ne faites que de brèves haltes pour vous restaurer et vous
reposer. Vous ne voulez pas, en effet, abuser de l'hospitalité des
paysans ni les inquiéter en leur laissant deviner la nature de
votre mission. Le quatrième jour vers midi, vous atteignez la
passe de Moytura. Là, les plaines font place aux contreforts
déchiquetés des monts Durncrag. Bientôt vous arrivez sur une
grande route orientée au sud et dont la surface est creusée
d'ornières et de nids-de-poule. C'est la célèbre voie de Ruanon.
Au sud de la passe, la voie de Ruanon traverse sur 150 km
environ un territoire à découvert qu'on appelle la Contrée des
Pillards. Des bandes de brigands venues du Pays Sauvage et des
hordes de Gloks descendues des montagnes de l'ouest tendent
fréquemment des embuscades aux voyageurs qui empruntent la
grande route. A plusieurs reprises, les chargements d'or et de
pierres précieuses en provenance des mines de Ruanon ont ainsi
offert de riches butins à ces voleurs impitoyables. « Éclaireurs,
en position ! » C'est vous qui venez de donner cet ordre ; aussitôt
trois groupes de patrouilleurs s'écartent de la colonne et lancent
leurs chevaux au galop. Vous regardez avec fierté ces habiles
cavaliers prendre position pour reconnaître le terrain en avant et
sur les flancs de la troupe en marche. A la fin de l'après-midi, l'un
des éclaireurs revenant de l'ouest vient vous montrer une sorte
de cratère rocheux d'où s'élève un filet de fumée : de toute
évidence il y a là une maison dissimulée à l'abri des rocs en
surplomb.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez examiner cette maison, rendez-vous au :"))
    st.page_link("tomes/tome4/page_160.py", label="160", icon="📄")

    st.write_stream(stream_text("Si vous préférez ne pas y prêter attention et poursuivre votre chemin le long de la voie de Ruanon, rendez-vous au :"))
    st.page_link("tomes/tome4/page_273.py", label="273", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
