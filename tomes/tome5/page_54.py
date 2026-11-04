import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_flag,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=54, book=5)

fr_no_need = "Votre bras n'est pas paralysé : vous n'avez pas besoin de l'herbe d'Oede."

fr_text = """
Vous vous éloignez rapidement des Thermes et vous pénétrez
dans le Saddi-tas-Ouda : la Place des Morts, entièrement pavée
de grandes dalles noires. Au centre de chaque dalle est fixée une
longue pique en fer et, du haut des marches des Thermes, la
place donne l'illusion d'un gigantesque porc-épic. Mais lorsque
vous vous rapprochez, vous constatez que le Saddi-tas-Ouda est
en fait un bien plus sinistre lieu. Empalé sur chaque pointe se
trouve un crâne humain : c'est tout ce qui reste des pirates, des
assassins, des renégats et des voleurs qui ont été condamnés à
mort. Cette macabre exposition sert d'avertissement à tous ceux
qui seraient tentés de défier la loi du Zakhan. En traversant la
place, vous heurtez soudain l'une des piques. Votre manche
droite est maculée de sang frais qui laisse sur le tissu de votre
tunique une tache sombre et rougeâtre.
Tout en maudissant le sort qui a provoqué cet incident, vous
levez les yeux et vous restez médusé par le spectacle qui s'offre à
vous : sur les piques qui se dressent autour de vous sont
empalées la tête de l'envoyé de Vassagonie et celle de tous les
membres de l'équipage de la galère sur laquelle vous avez voyagé.
Sur leur front, on a badigeonné le mot TRAÎTRE. La peur monte
en vous et, tournant les talons pour ne plus voir ces horribles
faciès aux yeux morts, vous vous élancez en courant à travers les
rues animées du Mikarum, le quartier où sont réunis tous les
marchands d'herbes et d'épices de la ville. Au bout d'une ruelle
serpentante, vous atteignez un carrefour sur lequel donne une
échoppe portant comme enseigne : BIR DAR MASOUN -
HERBORISTE PATENTÉE.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous devez vous procurer l'herbe d'Oede, rendez-vous au :"))
    if has_flag("bras paralysé"):
        st.page_link("tomes/tome5/page_68.py", label="68", icon="📄")
    else:
        st.write_stream(stream_text(fr_no_need))
        st.page_link("tomes/tome5/page_68.py", label="68", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous n'avez pas besoin de cette herbe, mais si vous désirez quand même entrer dans le magasin, rendez-vous au :"))
    if has_flag("bras paralysé"):
        st.page_link("tomes/tome5/page_154.py", label="154", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome5/page_154.py", label="154", icon="📄")

    st.write_stream(stream_text("Enfin, si vous préférez continuer votre chemin par une autre allée, qui mène droit au Grand Palais, rendez-vous au :"))
    st.page_link("tomes/tome5/page_179.py", label="179", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
