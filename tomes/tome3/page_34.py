import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=34, book=3)

fr_text = """
Vous vous souvenez tout à coup que vous possédez une Effigie de
cette hideuse créature. Vous la sortez aussitôt de votre poche et
vous la tenez devant vous. Elle se met alors à diffuser une étrange
lueur qui semble hypnotiser le monstre. Vonotar n'a plus le
contrôle de la créature qui, désormais, vous obéit. Le mage, se
rendant compte qu'il a perdu, s'éloigne du fossé. Loi-Kymar vous
rejoint peu après. Il essaie de vous dire quelque chose, mais il est
hors d'haleine. « Servez-vous de lui, Loup Solitaire... Envoyez-le...
contre Vonotar ! » Vous ordonnez au monstre de s'emparer de
Vonotar et de l'immobiliser, et il vous obéit aussitôt. Le traître
hurle de terreur et s'évanouit lorsque les tentacules gluants se
referment autour de lui. Vous remarquez que, pendant ce temps,
Loi-Kymar a jeté une poignée d'herbes pilées dans le fossé.
Quelques secondes plus tard, des vignes vierges et toutes sortes
de plantes grimpantes se mettent à pousser, formant un pont qui
vous permet de franchir le fossé pour atteindre le Trône du
Brumalmarc. Dès que vous êtes parvenu de l'autre côté, vous
ordonnez à la créature de relâcher Vonotar et de retourner dans
le fossé. Obéissante, elle se glisse dans l'obscurité et les blocs de
cristal s'élèvent lentement pour se remettre en place. « Ligotez-le,
Loup Solitaire ! crie Loi-Kymar tandis qu'il cherche la Crosse
de la Guilde, et prenez soin de lui ôter ses bagues et ses
amulettes. C'est un maître en matière de fourberie et il ne
faudrait surtout pas qu'il manque la petite fête que le
Sommerlund lui réserve pour son retour. » Vous suivez les
recommandations de Loi-Kymar et vous vous assurez que
Vonotar est bien attaché. « Ah ! la voici », s'écrie enfin le
magicien d'un ton triomphal. Il vient de découvrir la Crosse de la
Guilde parmi les feuilles de vignes vierges enchevêtrées au pied
du Trône. Il a hâte de s'en aller et vous le remerciez de son aide
en lui donnant votre carte de Kalte sur laquelle vous lui montrez
la position exacte du Cardonal. « Je n'en aurai pas besoin,
assure-t-il, les cartes sont toujours fausses et je préfère m'en
remettre à mon propre sens de l'orientation. » Loi-Kymar lève
alors sa Crosse de la Guilde et un rayon de lumière aveuglante
jaillit aussitôt de son extrémité. Le magicien décrit trois larges
cercles dans les airs, tenant la Crosse à bout de bras, et la salle du
Trône du Brumalmarc se transforme instantanément en un
kaléidoscope multicolore.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_350.py", label="350", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
