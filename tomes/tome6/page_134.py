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

check_inventory(current_page_number=134, book=6)

fr_text = """
Au-delà de la Vallée de Taunor, la grand-route part en
serpentant à travers des collines boisées, plongeant de temps à
autre au fond de vallées encaissées où des cours d'eau
tumultueux, regorgeant de truites, coulent vers le sud pour
aller se jeter dans la Quarle. La route est bordée de fleurs
odorantes entourées de nuées de papillons multicolores, et le
chant incessant des oiseaux vient ajouter à la sérénité
bucolique de ce magnifique paysage. « Je suis heureux de voir
qu'il existe encore au Lyris un endroit que la guerre a épargné,
dit Cyrilus en tirant nonchalamment sur sa longue pipe en terre
cuite. Hélas ! combien cette paix est rare de nos jours ! » Peu
après, la route passe devant un monastère en ruine, avant de
redescendre en pente raide vers des cabanes en bois regroupées
en demi-cercle près d'un pont de pierre. Une grande porte,
flanquée de deux tourelles, commande l'accès du pont. « Voici la
Porte de Denka, explique Cyrilus. Le droit de passage pour
traverser le pont est de 3 Pièces d'Or, à moins, bien entendu,
que le gardien de la Porte ne soit votre frère ! » Sur ces mots
Cyrilus fait un petit clin d'œil et sourit. « Cela nous prendra
sans doute un bon moment, poursuit-il, car je n'ai pas vu mon
frère Esmond depuis plus d'un mois, et il voudra sûrement que je
lui raconte les derniers potins de Quarle avant de nous laisser
repartir ! » Cyrilus désigne ensuite du doigt deux cabanes où
l'on a gravé dans le bois, au-dessus de la porte, la forme d'un
tonnelet de bière et d'une miche de pain. « Vous trouverez là la
meilleure bière et le pain le plus succulent de tout le Lyris.
Allez-y de ma part, vous serez traité comme un roi ! » Votre
longue chevauchée vous a donné grand faim et soif, aussi la
perspective d'une collation est-elle bien alléchante...
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez entrer dans la cabane où l'on sert la bière, rendez-vous au :"))
    st.page_link("tomes/tome6/page_185.py", label="185", icon="📄")

    st.write_stream(stream_text("Si vous préférez aller droit vers la cabane où l'on vous donnera ce fameux pain, rendez-vous au :"))
    st.page_link("tomes/tome6/page_287.py", label="287", icon="📄")

    st.write_stream(stream_text("Si vous jugez plus sage de rester avec Cyrilus et de l'accompagner à la Porte de Denka, rendez-vous au :"))
    st.page_link("tomes/tome6/page_89.py", label="89", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
