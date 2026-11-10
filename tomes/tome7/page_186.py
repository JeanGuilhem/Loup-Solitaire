import streamlit as st
from inventory import (
    add_to_inventory,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=186, book=7)

fr_text = """
Vous portez le coup de grâce à votre ennemi qui hurle de douleur
avant de s'effondrer à vos pieds en se matérialisant. Vous pensez
de prime abord qu'il s'agit d'un être humain, mais en observant
plus attentivement le corps sans vie, vous comprenez qu'il n'en
est rien. Ses yeux, maintenant vitreux, ressemblent à ceux d'un
chat ; ses doigts courts sont pourvus de griffes, et sa mâchoire
inférieure dépasse largement sa mâchoire supérieure. Sa peau est
marquée de profondes cicatrices, dues à l'évidence non pas à des
blessures de guerre, mais à des opérations chirurgicales
sommaires. Il n'y a plus trace du fouet avec lequel il vous a
frappé, mais il porte une lance en bandoulière et, autour de son
cou ensanglanté, un Sifflet d'Argent accroché à une chaîne.
(Inscrivez cette dernière trouvaille sur votre Feuille d'Aventure,
dans la case Objets Spéciaux.) Instinctivement, vous portez le
Sifflet à vos lèvres et vous soufflez, mais aucun son n'en sort.
Intrigué, vous tournez la tête en tout sens, et vous sursautez en
apercevant une solide poutre en métal bleu qui enjambe
maintenant le gouffre !
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        add_to_inventory("SIFFLET D'ARGENT")
    st.caption("Le Sifflet d'Argent est inscrit dans vos Objets Spéciaux.")

    st.write_stream(stream_text("Si vous désirez traverser le gouffre, rendez-vous au :"))
    st.page_link("tomes/tome7/page_6.py", label="6", icon="📄")

    st.write_stream(stream_text("Si vous préférez revenir sur vos pas le long du couloir, rendez-vous au :"))
    st.page_link("tomes/tome7/page_64.py", label="64", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
