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

check_inventory(current_page_number=204, book=6)

fr_text = """
Le Capitaine assiste au conseil de guerre que tient le Prince
Ewewin. Une heure plus tard, il est de retour dans sa compagnie
et rend compte de la conférence à ses hommes qui, fatigués de
courir les routes, accueillent ses propos avec une certaine
froideur. « Nous livrerons bataille cette nuit, dit-il d'une voix
ferme et claire. Nous attaquerons par le pont de Tekaro pour
essayer de forcer les portes de la ville qui sont à moitié détruites.
Nous devons saisir notre chance ce soir car les travaux de
réparation vont commencer dès demain. » Bien que la plupart de
ses hommes soient de vieux briscards ayant à leur actif un
nombre incalculable de campagnes, ils craignent que cette
attaque soit suicidaire. Ils savent, en effet, que les portes sont
défendues par de nombreux archers et qu'elles ne pourront être
franchies qu'au prix de lourdes pertes. « Chaque homme recevra
1 000 couronnes », poursuit le Capitaine en espérant que l'appât
du gain les fasse changer d'avis. Mais cette forte récompense ne
semble pas les intéresser. A quoi leur servira cet or s'ils doivent
perdre la vie au cours de la bataille ? « Que ceux qui veulent se
battre me suivent, poursuit le Capitaine en durcissant la voix, ses
yeux bleu-acier brillants de colère. Les autres peuvent partir tout
de suite. »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez rester avec le Capitaine pour prendre d'assaut les portes de la ville, rendez-vous au :"))
    st.page_link("tomes/tome6/page_126.py", label="126", icon="📄")

    st.write_stream(stream_text("Si vous préférez partir, rendez-vous au :"))
    st.page_link("tomes/tome6/page_280.py", label="280", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
