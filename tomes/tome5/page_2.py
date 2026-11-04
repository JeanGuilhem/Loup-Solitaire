import streamlit as st
from inventory import (
    check_inventory,
    clear_flag,
    display_inventory,
    end_page,
    has_flag,
    is_new_page,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=2, book=5)

fr_text = """
Le souffle coupé par l'effort et fatigué par le combat que vous
venez de mener, vous vous écartez de l'Elix au moment où celui-ci s'effondre en poussant un dernier soupir. Ses yeux verts
deviennent peu à peu vitreux et finissent par prendre l'aspect dur
et froid du jade. Autour du cou ensanglanté de la créature pend
une Clé accrochée à une chaîne en or. A l'aide de cette Clé, vous
ouvrez la porte blindée de la chambre forte qui se trouve au fond
de l'Herboristerie. A l'intérieur, sur une étagère placée en
hauteur, vous découvrez une petite boîte qui renferme ce que
vous cherchiez : l'herbe d'Oede. Quelques secondes après avoir
appliqué les merveilleuses feuilles dorées sur la blessure de votre
épaule, un picotement envahit tout votre bras. Puis l'engourdissement disparaît et votre épaule se trouve enfin
libérée des redoutables microbes paralysants. Dans la boîte, il
reste suffisamment d'herbe d'Oede pour une application. Cette
substance puissante peut être utilisée pour guérir de nombreuses
maladies mortelles, mais elle pourra également vous faire gagner
10 points d'ENDURANCE si vous en mangez à la suite d'un
combat. Si vous désirez garder cette herbe, inscrivez-la sur votre
Feuille d'Aventure dans la case des Objets Spéciaux. Par ailleurs,
n'oubliez pas de rajouter à votre total d'HABILETÉ les points que
vous aviez temporairement perdus à cause de la Paralysie des
Membres. Après avoir traîné le cadavre de l'Elix dans la chambre
forte, vous verrouillez la porte blindée de l'intérieur et vous
remarquez alors que deux portes donnent accès à la pièce : celle
par laquelle vous êtes entré et une autre, plus petite, située à
l'opposé. La Clé d'Or ouvre également la nouvelle porte, qui
donne sur un escalier étroit, faiblement éclairé par des torches
fixées au mur. L'ascension est difficile car l'escalier est abrupt.
Vous supposez que ces marches font partie d'un passage secret
menant à la pièce d'où vous venez, et votre impression se trouve
confirmée lorsque vous parvenez à ce qui semble être une
impasse. Après avoir mieux examiné l'endroit, vous remarquez
une étroite porte en bronze encastrée dans le mur. A première
vue, il ne paraît pas y avoir de serrure, mais vous finissez par
apercevoir un minuscule trou, au ras du sol. Lorsque vous y
enfoncez la Clé d'Or, vous êtes sûr que la porte de bronze va
s'ouvrir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # l'herbe d'Oede guérit la Paralysie des Membres : on rend les 3 points d'HABILETÉ perdus
    if is_new_page() and has_flag("bras paralysé"):
        st.session_state.hability += 3
        clear_flag("bras paralysé")
        st.success("Votre bras est guéri : vous retrouvez les 3 points d'HABILETÉ perdus.")

    pickup_button("HERBE D'OEDE", key="oede", label="Garder l'herbe d'Oede")

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome5/page_67.py", label="67", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
