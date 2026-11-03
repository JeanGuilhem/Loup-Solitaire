import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=225, book=4)

fr_text = """
Vous essayez de ne pas prêter attention aux douleurs que vous
ressentez dans les jambes, ni à la peur qui vous noue l'estomac,
et vous vous concentrez sur le drapeau du Sommerlund qui flotte
au loin comme un ultime symbole d'espoir. Votre visage ruisselle
de sueur et vous avez l'impression que vos poumons vont éclater.
Vous ne ralentissez pas l'allure cependant. La pensée des Chiens
de Guerre qui vous poursuivent pour vous dévorer suffit à vous
stimuler. Vous n'êtes plus qu'à 400 mètres de la barricade et de
la tour de guet. A cette distance, les visages que vous distinguez
ne semblent que de petits points roses qui se détachent contre les
murs. A 300 mètres de la barricade, le sol est jonché de cadavres
de brigands dont la plupart ont été tués par des flèches. Nombre
d'entre eux sont restés là pendant des semaines et une nuée de
corbeaux croassant s'envole à votre approche. Saisi de dégoût,
vous détournez la tête. Tout à coup, les échos de cris
enthousiastes retentissent dans la plaine. Les soldats assiégés
vous ont repéré et ont reconnu votre cape verte de Seigneur Kaï.
Il ne vous reste plus que 200 mètres à parcourir. Vous venez de
passer devant les ruines d'une maison incendiée lorsqu'une
douleur intense vous déchire soudain la jambe. Une flèche vient
de vous atteindre à la cuisse et vous tombez tête la première sur
le sol boueux recouvert de cendre. Tapi dans les ruines de la
maison, un brigand tend son arc et vise votre tête.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Utilisez la Table de Hasard pour obtenir un chiffre.'))
    roll = hazard_roll()
    if roll is not None:
        if roll == 0:
            st.write_stream(stream_text('Si vous tirez le 0, rendez-vous au :'))
            st.page_link("tomes/tome4/page_181.py", label="181", icon="📄")
        elif roll <= 5:
            st.write_stream(stream_text('Si vous tirez un chiffre de 1 à 5, rendez-vous au :'))
            st.page_link("tomes/tome4/page_20.py", label="20", icon="📄")
        else:
            st.write_stream(stream_text('De 6 à 9, rendez-vous au :'))
            st.page_link("tomes/tome4/page_300.py", label="300", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
