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

check_inventory(current_page_number=339, book=5)

fr_text = """
Deux Nains escaladent la plate-forme et se précipitent aux côtés
de leur jeune capitaine. L'un d'eux ouvre une sacoche en velours
accrochée en bandoulière autour de son torse musclé et en sort
un flacon de verre ainsi qu'un bandage de tissu propre. Avec
d'infinies précautions, les Nains soignent la blessure de Banedon.
Celui-ci reprend peu à peu ses forces, puis il vous écoute
attentivement raconter les circonstances terrifiantes qui ont
abouti à vos retrouvailles. Alors que vous arrivez à la conclusion
de cette triste histoire, Banedon prend soudain la parole avec une
ferme détermination. « L'avenir du Sommerlund est entre nos
mains, Loup Solitaire. Nous devons absolument empêcher le
Seigneur des Ténèbres Haakon de détruire le Livre du Magnakaï !
Les nomades de la Mer de la Sécheresse m'ont parlé du
Tombeau du Majhan. Ils disent que c'est un lieu terrifiant : un
endroit où règne la mort et où nul ne saurait survivre. Le site se
trouve au-delà du Dahir, à proximité de l'oasis de Bal-Loftan.
C'est tout ce que je sais, car le Tombeau du Majhan fut construit
dans le plus grand secret et les dernières traces qui en restaient
ont été depuis longtemps recouvertes par les sables mouvants de
la Mer de la Sécheresse. » A ces mots, vous ne pouvez cacher
votre déception, mais Banedon ne semble pas y accorder
d'attention et il reprend : « Cependant, tout espoir n'est pas
perdu. Il existe un homme, un seul, qui peut nous conduire
jusqu'au Tombeau du Majhan. Il s'appelle Tipasa Edarouk, c'est-
à-dire Tipasa le Vagabond. C'est lui que nous devrons trouver,
car c'est le seul homme ayant jamais pénétré dans le Tombeau du
Majhan qui soit encore vivant pour en parler. »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome5/page_302.py", label="302", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
