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

check_inventory(current_page_number=142, book=4)

fr_text = """
L'aube arrive, sinistre et pluvieuse. Un voile de bruine enveloppe
la cité fantôme et les gémissements lugubres des vents qui
soufflent au fond des gorges de Maaken vous mettent mal à
l'aise. Vous contemplez longuement les ruines, votre cape de
Seigneur Kaï serrée autour de vos épaules pour vous protéger du
froid et de l'humidité. C'est ici même, au temps de la lune noire,
que le roi Ulnar du Sommerlund tua le Seigneur Vashna, le plus
puissant des Maîtres des Ténèbres. A l'issue d'un mortel combat
livré au bord même de cet abîme, le redoutable Maître des
Ténèbres fut tué par le Glaive de Sommer. On dit que son cri de
mort, lorsqu'il tomba dans le gouffre, résonnera dans ces
profondeurs jusqu'au jour où Vashna se relèvera pour mener sa
vengeance contre le Sommerlund et la maison d'Ulnar. Vous
sentez votre estomac se contracter à la pensée que ce jour est
peut-être venu. Cinq heures durant, vous observez la ville morte
en notant le moindre détail. Le premier vers de l'étrange
prophétie tourne sans cesse dans votre tête : « Au soir de pleine
lune, en un temple profond... » Ce temple, de toute évidence, se
trouve quelque part sous terre et il doit exister un moyen d'y
accéder. Mais par où peut-on y entrer ? Vous étudiez chaque
fissure du terrain accidenté et vous arrivez à la conclusion que
seuls deux chemins peuvent y mener. Il faut soit franchir la porte
d'une crypte, gardée par deux Guerriers vassagoniens, soit
descendre un escalier de marbre qui s'enfonce sous terre entre
deux colonnes en ruines.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez essayer de pénétrer dans le temple par la porte de la crypte que surveillent les Gardes, rendez-vous au :'))
    st.page_link("tomes/tome4/page_183.py", label="183", icon="📄")

    st.write_stream(stream_text("Si vous préférez descendre l'escalier de marbre qui, lui, n'est pas gardé, rendez-vous au :"))
    st.page_link("tomes/tome4/page_270.py", label="270", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
