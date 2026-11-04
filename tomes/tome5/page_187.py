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

check_inventory(current_page_number=187, book=5)

fr_text = """
Vous reconnaissez la créature : il s'agit d'un Kwaraz. Ce sont de
gigantesques reptiles originaires des marais de Maaken situés à
des centaines de kilomètres à l'ouest de la Vassagonie. Les
Kwaraz peuvent vivre dans n'importe quel environnement
pourvu qu'il y fasse chaud et que l'air soit humide et fétide. Vous
comprenez tout à coup que le Baga-Darooz réunit toutes les
conditions permettant à ces dangereuses créatures de proliférer.
Le Kwaraz se déplace au plafond en s'agrippant à la pierre à
l'aide de ses longues griffes recourbées, ses yeux globuleux de
plus en plus écarquillés... Les Kwaraz sont très sensibles au
pouvoir psychique. En utilisant votre Discipline Kaï de la
Communication Animale, vous le persuadez que votre chair n'est
pas aussi tendre qu'elle en a l'air et, bientôt, vous n'offrez plus
aucun intérêt à ses yeux. Vous le regardez disparaître le long du
tunnel avec un sentiment de crainte mêlé de fascination.
Soudain, un cri terrifiant retentit dans les ténèbres : Maouk vient
de perdre un de ses hommes. Un frisson glacial vous parcourt
l'échine mais votre instinct vous dit de continuer d'avancer
rapidement pendant qu'il en est encore temps.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome5/page_17.py", label="17", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
