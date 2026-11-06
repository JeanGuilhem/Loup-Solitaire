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

check_inventory(current_page_number=119, book=6)

fr_text = """
Les yeux de Cyrilus s'écarquillent de stupeur : « Loup Solitaire
! chuchote-t-il, presque incrédule. J'aurais dû m'en douter...
Veuillez accepter toutes mes excuses, mon Seigneur, je croyais
que vous recherchiez la Pierre de la Sagesse pour de bien moins
honorables raisons ! » Cyrilus se met alors à vous raconter,
avec une extrême lenteur, la légende de la Pierre de la Sagesse.
Vous apprenez qu'après la quête d'Aigle du Soleil la Pierre est
longtemps restée à Varetta, où elle fut scellée sur le trône de
Lyris, qui lui-même se trouvait dans la Tour des Rois. Par la
suite, durant la guerre qu'elle déclencha - il y a de cela
plusieurs centaines d'années -, la Pierre de la Sagesse fut
volée par Kaskor, un prince de Salonie. Ce dernier la fit sertir
sur un sceptre en or, qu'il emporta avec lui dans les batailles
afin d'exhorter les fanatiques à le suivre et à écraser ses
ennemis. Grâce à elle, il pensait être invulnérable. Mais il
n'en était rien : Kaskor fut tué, comme le plus commun des
mortels, sur son vaisseau royal, au cours de la bataille de
Rhem. Le sceptre lui échappa des mains et la Pierre de la
Sagesse disparut dans les eaux profondes de la Storn. A partir
de là, on a raconté maintes et maintes histoires au sujet de la
redécouverte de la Pierre, mais la plupart étaient sans
fondement, pour ne pas dire franchement extravagantes. On dit
que celui qui la retrouverait deviendrait maître de tous les
pays de la Storn. Cela suffit à appâter de nombreux Seigneurs de
la Guerre, tous plus avides les uns que les autres de se
l'approprier à des fins peu avouables. Cependant, personne ne
réussit à retrouver la pierre légendaire. Cyrilus, quant à lui,
ignore également où elle se trouve, mais il connaît un homme qui
prétend savoir exactement son emplacement. « Laissez-moi vous
accompagner jusqu'à Varetta, vous demande-t-il. Et, en échange
de cet immense privilège, je vous conduirai à cet homme. » Votre
instinct de Maître Kaï vous incite à penser que la proposition
du vieil homme est sincère. Vous hochez la tête en guise
d'acquiescement, puis vous convenez avec lui de vous retrouver,
le lendemain matin, dans la cour de l'auberge, au lever du jour.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("A présent, rendez-vous au :"))
    st.page_link("tomes/tome6/page_5.py", label="5", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
