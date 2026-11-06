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
from utils import called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=400, book=5)

fr_text = """
Vous regardez le sol à l'endroit où Haakon est tombé, mais il n'y
a plus aucune trace de son corps : il s'est littéralement volatilisé.
L'atmosphère est devenue étrangement calme et paisible, comme
si une ombre immense et malfaisante s'était dissipée. Vous
retournez vers le trône où Haakon vous attendait. Devant ce
trône se trouve un portail de pierre rouge sang où sont gravées
d'anciennes inscriptions. A travers les signes, vous distinguez
l'empreinte d'une main humaine sculptée dans la pierre.
Instinctivement, vous posez la main sur l'empreinte ; les deux
formes s'épousent parfaitement. Soudain, le portail coulisse
silencieusement, vous mettant en présence de l'objet qui va
changer votre destinée : le Livre du Magnakaï ! Le Livre, grand
ouvert, est posé sur un piédestal et offre ses secrets à vos yeux
émerveillés. Vous prenez le Livre dans vos mains et, soudain,
toute l'énergie retenue au sein des pages dorées se libère en un
flux de vibrations puissantes qui fait trembler les murs de la
pièce. Le cœur battant à tout rompre, vous refermez le Livre et
vous sortez du Tombeau en courant à perdre haleine. Une fois
dehors, vous partez en direction des contreforts de Koneshi.
Pendant ce temps, Banedon a, lui aussi, rempli sa mission avec
succès et il vous attend avec Tipasa. Lorsqu'ils vous voient tous
deux arriver avec le Livre du Magnakaï, ils ne peuvent retenir
leur joie : « Cette nuit triomphale fera naître une aube pleine
d'espoir pour le Sommerlund, dit Banedon avec jubilation. Le
Kaï est ressuscité ! » Votre quête est maintenant achevée. Vous
avez trouvé le Livre du Magnakaï et libéré le Magnamund de
l'ombre menaçante du Seigneur des Ténèbres Haakon. Mais,
pour vous, Loup Solitaire, l'aventure ne fait que commencer.
Votre destinée, à présent, est de suivre la voie glorieuse tracée
par les grands Maîtres Kaï. Pour apprendre leurs secrets et tenter
la première quête passionnante du Magnakaï, partez pour de
nouvelles aventures avec le sixième volume de la série Loup Solitaire.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        add_to_inventory("LIVRE DU MAGNAKAÏ")
        st.balloons()
    st.write("*Le Livre du Magnakaï a été ajouté à vos Objets Spéciaux.*")
    st.success(
        "**Mission accomplie !** Haakon s'est volatilisé et le Livre du Magnakaï est entre vos mains : "
        "le Kaï est ressuscité et le Magnamund est libéré de l'ombre du Seigneur des Ténèbres. "
        "L'aventure se poursuit dans le tome 6, *La Pierre de la Sagesse*, premier volume du cycle Magnakaï."
    )
    st.page_link("tomes/tome6/debut.py", label="Continuer avec le tome 6", icon="📜")
    st.page_link("accueil.py", label="Retour à l'accueil", icon="🏠")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
