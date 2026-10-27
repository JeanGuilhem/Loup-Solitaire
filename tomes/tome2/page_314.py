import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    remove_from_inventory,
    show_illustrations,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=314, book=2)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
L'aubergiste est un vieil homme maigre, sec et borgne. Il vous tend une
clé et vous désigne du doigt un escalier qui mène à une galerie. «
Chambre 2, c'est la porte rouge», dit-il. Les autres voyageurs paient
chacun leur Couronne, prennent la clé de leur chambre puis traversent
la salle bondée de la taverne en direction de l'escalier. « Il nous faut
établir un programme pour demain, dit alors Dorier. Je suggère que
nous nous retrouvions au bar dans une heure pour décider de ce qu'il
convient de faire. » Tous les autres approuvent d'un signe de tête.
Lorsque vous refermez la porte de votre chambre, les paroles du
capitaine Kelman vous reviennent soudain en mémoire : « Tout cela
sent la trahison, avait-il dit d'un air sombre, il est clair que l'ennemi a
déjà dressé des plans pour faire échouer votre mission. » Il s'est écoulé
presque une heure lorsque des coups frappés à la porte viennent
interrompre le fil de vos pensées. C'est l'aubergiste qui vous apporte un
repas chaud. « Avec les compliments d'un de vos amis», dit-il en
déposant un plateau devant vous. Puis il quitte la chambre avant que
vous ayez pu lui demander le nom de ce mystérieux ami. Le plat qu'il
vous a apporté est fort appétissant et d'ailleurs vous n'avez pas mangé
de la journée. Il est donc temps de prendre un Repas, sinon, vous
perdrez 3 points d'ENDURANCE.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez manger ce que l'aubergiste vous a apporté, rendez-vous au :"))
    st.page_link("tomes/tome2/page_36.py", label="36", icon="📄")
    st.write_stream(stream_text("Si vous ne voulez pas toucher à cette nourriture, rendez-vous au :"))
    st.caption("Il vous faudra alors prendre un Repas de votre Sac à Dos, sinon vous perdrez 3 points d'ENDURANCE.")
    if st.button("178", key="refuse_tray", icon="📄"):
        if not has_kai("La Chasse") and not remove_from_inventory("REPAS"):
            if remove_from_inventory("MOISSON DE LAUMSPUR"):
                change_endurance(3)
            else:
                change_endurance(-3)
        st.switch_page("tomes/tome2/page_178.py")
    st.write_stream(stream_text("Enfin, si vous maîtrisez la Discipline Kaï de la Chasse, rendez-vous au :"))
    if has_kai("La Chasse"):
        st.page_link("tomes/tome2/page_290.py", label="290", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome2/page_290.py", label="290", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
