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

check_inventory(current_page_number=68, book=5)

fr_text = """
Vous écartez le rideau de perles qui voile la porte et vous
pénétrez dans une pièce agréable et fraîche. Votre bras inerte,
qui pend mollement le long de votre corps, a pris une teinte
violacée. La peur vous étreint à nouveau: il faut absolument que
vous trouviez l'herbe d'Oede qui pourra vous guérir, sans quoi
vous perdrez votre bras... et sans doute la vie également. Dans la
pénombre du magasin surgit soudain une femme derrière le
comptoir. Elle a des yeux verts perçants et sa chevelure
flamboyante est relevée en un haut chignon retenu par des
épingles de jade. « Soyez le bienvenu, Homme du Nord, dit-elle
d'une voix douce et claire. En quoi puis-je vous être utile ? »
Vous hésitez un instant avant de lui répondre, puis vous
murmurez : « Oede... » La femme plisse alors les yeux en
examinant votre bras blessé et reprend : «Je ne peux
malheureusement pas vous aider, car l'Oede est devenue une
denrée très rare et très précieuse. Il me faudrait vendre mon
magasin ainsi que tous mes autres biens pour m'en procurer un
tout petit sac ! A Barrakeesh, il n'existe qu'un seul homme assez
riche pour posséder cette herbe : le Zakhan. » A ces mots, la
sueur commence à perler à votre front tandis qu'elle continue : «
Le peu d'herbe d'Oede qui soit disponible actuellement se trouve
sévèrement gardé sous clé au Grand Palais. » Vous demandez à
la femme s'il existe une autre herbe capable de guérir votre bras,
mais elle secoue la tête en signe de dénégation et vous répond : «
Seule l'herbe d'Oede peut neutraliser la Paralysie des Membres,
et vous n'en trouverez qu'à l'Herboristerie Impériale ». Puis elle
se penche sous le comptoir et vous présente trois flacons de verre
contenant chacun un liquide coloré. « Ceci ne vous guérira pas,
dit-elle, mais atténuera la douleur des derniers instants... »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez examiner ces potions, rendez-vous au :"))
    st.page_link("tomes/tome5/page_27.py", label="27", icon="📄")

    st.write_stream(stream_text("Si vous préférez sortir du magasin sans vous soucier des flacons et reprendre votre chemin le long de l'allée, rendez-vous au :"))
    st.page_link("tomes/tome5/page_160.py", label="160", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
