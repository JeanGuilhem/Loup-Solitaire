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

check_inventory(current_page_number=142, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Vous plongez, puis vous nagez sous l'eau jusqu'à ce que la
pression dans vos poumons devienne insupportable et vous
contraigne à refaire surface. Les Sharnazims courent dans toutes
les directions, essayant de cerner le quai afin de prévenir toute
tentative de fuite de votre part. Vous aspirez une grande bouffée
d'air, puis vous plongez à nouveau et vous nagez immergé vers
une flottille de petits bateaux situés à moins de 50 mètres. A
travers l'eau bleue et limpide, vous voyez clairement les débris et
autres détritus qui jonchent le lit du port. Ce sont les
témoignages des nombreux navires marchands qui ont mouillé le
long de ces quais par le passé. Tout à coup, vous apercevez,
accrochée à une vieille ancre, une étrange masse gélatineuse d'où
sort une multitude de petits tubes et dont la partie inférieure est
prolongée par un rostre en forme d'hameçon. Sans que rien ne le
laisse présager, la créature se précipite vers vous, propulsée par
ses innombrables tubes respiratoires. Vous comprenez avec
effroi qu'il s'agit d'une Sangsue géante affamée qui a besoin de
votre sang !
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï de la Communication Animale, rendez-vous au :"))
    if has_kai("Communication Animale"):
        st.page_link("tomes/tome5/page_134.py", label="134", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_134.py", label="134", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous désirez vous battre avec la créature, rendez-vous au :"))
    st.page_link("tomes/tome5/page_12.py", label="12", icon="📄")

    st.write_stream(stream_text("Si vous préférez la fuir au plus vite, rendez-vous au :"))
    st.page_link("tomes/tome5/page_95.py", label="95", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
