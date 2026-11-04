import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=90, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Vous pénétrez dans un grand vestibule en marbre rose et blanc.
Un homme vêtu d'une longue tunique blanche est assis près
d'une porte au fond de la pièce ; il est en train de lire un
parchemin qu'il tient tout près de ses yeux. Il ne vous a pas vu
entrer dans les Bains, mais il décèle pourtant rapidement votre
présence. « Par le Majhan ! s'écrie-t-il en se pinçant le nez, vous
sentez encore plus mauvais qu'un Baknar ! » Puis il vous tend
une serviette et vous dit en désignant la porte : « Suivez mon
conseil : baignez-vous tout habillé car vos vêtements ont eux
aussi besoin d'un bon nettoyage ! » Vous craignez que l'homme
ne s'aperçoive que vous n'êtes pas Vassagonien, mais il se
contente de reprendre sa lecture en plissant ses yeux myopes.
Vous réalisez alors avec soulagement que l'homme n'a pas une
assez bonne vue pour découvrir que vous êtes étranger. Au-delà
de la porte se trouve une grande entrée donnant accès à plusieurs
salons ouverts qui comportent chacun un bassin encastré dans le
sol. Un courant d'eau parfumée alimente en permanence les
bassins, puis s'écoule directement dans le Baga-Darooz. Suivant
le conseil du gardien des Thermes, vous décidez de vous plonger,
tout habillé, dans l'eau fraîche. Sur le rebord du bassin, vous
remarquez une jarre en terre remplie à ras bord d'une huile
violette et translucide.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï de la Guérison, rendez-vous au :"))
    if has_kai("La Guérison"):
        st.page_link("tomes/tome5/page_6.py", label="6", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_6.py", label="6", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous désirez goûter un peu cette huile violette, rendez-vous au :"))
    st.page_link("tomes/tome5/page_41.py", label="41", icon="📄")

    st.write_stream(stream_text("Si vous préférez au contraire vous enduire la peau de cette huile, rendez-vous au :"))
    st.page_link("tomes/tome5/page_103.py", label="103", icon="📄")

    st.write_stream(stream_text("Si enfin vous ne voulez pas toucher à l'huile, rendez-vous au :"))
    st.page_link("tomes/tome5/page_71.py", label="71", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
