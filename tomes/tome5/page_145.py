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

check_inventory(current_page_number=145, book=5)

fr_text = """
Vous avancez en pataugeant dans une eau épaissie par une
mousse sale et vous essayez de ne pas respirer par le nez. La
fange visqueuse est remplie d'immondices verdâtres et noirs et, à
chaque pas que vous faites, vous remuez toute cette boue qui
laisse échapper des gaz délétères. Vous placez votre manteau Kaï
sur la bouche mais, malgré cela, la puanteur épouvantable vous
suffoque et vous donne des haut-le-cœur. Un fort
éclaboussement vous avertit que les hommes de Maouk ne sont
plus très loin et vous pressez le pas. A intervalles réguliers, des
canalisations déversent leurs eaux sales qui tombent en cascade
du plafond. De nombreuses cascades sont colorées en jaune vif
ou en brun rougeâtre. Cette section du Baga-Darooz se trouve en
effet sous le quartier de la confection de Barrakeesh où la Guilde
des Tisseurs de Lin fait marcher ses nombreux ateliers de
foulons. Les teintures usées sont jetées directement dans l'égout,
colorant ainsi les eaux graisseuses du collecteur principal. Tout à
coup, vous apercevez à quelques mètres des remous qui
s'approchent de vous et vous comprenez, horrifié, qu'il s'agit du
sillage caractéristique d'une créature des égouts.
Instinctivement, vous vous collez au mur lorsque vous
commencez à sentir des remous tournoyer autour de votre taille.
Votre sang se fige et vous êtes incapable de faire le moindre
mouvement mais, au bout de quelques secondes qui vous
semblent une éternité, vous voyez avec un grand soulagement le
tourbillon s'éloigner. Un cri terrifiant éclate brusquement dans
les ténèbres : Maouk vient de perdre un de ses hommes. Le
hurlement affreux du Sharnazim vous fait frémir des pieds à la
tête, mais votre instinct vous dit de vous hâter tant que vous le
pouvez encore. Le tunnel arrive bientôt à un croisement d'où part
un autre tunnel vers l'ouest.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez suivre ce tunnel, rendez-vous au :"))
    st.page_link("tomes/tome5/page_108.py", label="108", icon="📄")

    st.write_stream(stream_text("Si vous préférez continuer vers le nord, rendez-vous au :"))
    st.page_link("tomes/tome5/page_70.py", label="70", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
