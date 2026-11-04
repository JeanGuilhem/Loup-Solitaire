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

check_inventory(current_page_number=331, book=5)

fr_text = """
Vous n'arrivez pas à trouver le sommeil tellement vous êtes
préoccupé par l'issue prochaine de votre expédition et vous êtes
hanté par la pensée que les Seigneurs des Ténèbres ont peut-être
déjà trouvé le Livre du Magnakaï. Vous vous levez avant l'aube et
vous prenez un petit déjeuner frugal, composé d'une galette de
farine et de lait de brebis. Puis Banedon et vous vous remettez en
route après avoir salué et remercié la femme de Tipasa. Le
voyage de retour vers la Nef du ciel se passe sans incident et, à
midi, vous atteignez la faille rocheuse où le vaisseau est ancré.
Nolrim est le premier à vous accueillir, mais il ne peut cacher sa
déception en constatant que vous revenez seuls. « Ne t'inquiète
donc pas, la réponse se trouve là, dit Banedon en lui montrant le
journal de Tipasa. Prépare-toi à hisser les voiles ! » Tandis que la
Nef du ciel s'élève lentement dans le ciel azuré, Banedon passe la
barre à Nolrim et vous demande de le suivre dans sa cabine, à la
proue du vaisseau. Trois heures durant, il examine attentivement
ses cartes, faisant de nombreux calculs et vérifiant les cotes
données par ses instruments de mesure afin de trouver la
situation exacte du Tombeau du Majhan. « Cela ne sert à rien,
finit-il par dire, exténué et découragé. Je n'arrive pas à sonder le
mystère de tous ces chiffres. » Alors que vous feuilletez à votre
tour les pages du journal de Tipasa, vous comprenez subitement
que celui-ci est rédigé en code. Ce que Banedon a supposé être la
position des étoiles est en réalité un message codé à trois chiffres
qui donne une localisation extrêmement précise du Tombeau.
Consultez la carte qui figure au début du livre pour vous aider à
découvrir le Tombeau du Majhan d'après les indications
suivantes : le premier des trois chiffres est égal au nombre
d'oasis qui se trouvent entre Ikaresh et Bir Adalou. Le deuxième
de ces chiffres représente le nombre des cités de Vassagonie. Le
troisième chiffre, quant à lui, est égal au nombre d'îles qui se
trouvent au large des côtes de Cap Kabar.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Lorsque vous aurez déchiffré le code, inscrivez les trois chiffres dans l'ordre donné. Vous obtiendrez alors le numéro du paragraphe où vous devez vous rendre à présent."))
    code = st.number_input("Numéro du paragraphe (les trois chiffres du code)", min_value=1, max_value=400, value=None, step=1, key="code_331")
    if code == 373:
        st.page_link("tomes/tome5/page_373.py", label="373", icon="📄")
    elif code is not None:
        st.write("*Banedon secoue la tête : ces chiffres ne correspondent à rien sur sa carte du ciel. Consultez à nouveau la carte.*")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
