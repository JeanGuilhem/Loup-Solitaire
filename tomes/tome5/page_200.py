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

check_inventory(current_page_number=200, book=5)

fr_text = """
L'empereur de Vassagonie, le Zakhan Kimah, trône sur une
estrade recouverte de fourrure écarlate. Il est vêtu d'un habit
brodé d'or mais dépourvu de tout ornement. Il tient dans la main
un objet de métal noir et ses yeux froids et cruels vous glacent le
sang. Le Zakhan est un homme à la prestance impressionnante,
mais il fait pâle figure à côté de son compagnon qui est la
véritable cause de votre terreur. Celui-ci se tient devant le
Zakhan ; un heaume noir comme la mort dissimule son visage
mais une odeur de décomposition et une horrible voix sépulcrale
trahissent son identité. « Amenez-moi Loup Solitaire ! » hurle la
voix cruelle, que vous connaissez bien : celle d'un Seigneur des
Ténèbres d'Helgedad, vos ennemis mortels. Le Zakhan se lève et,
en observant attentivement son visage, vous décelez une lueur de
doute - ou peut-être de crainte - dans ses yeux durs, mais ils
reprennent vite leur expression normale. « Il vous sera amené,
au coucher du soleil, en échange de l'Orbe de la Mort, comme
convenu », dit le Zakhan. « Mais vous l'avez cet Orbe ! rétorque
la terrible voix, amenez-moi ce blanc-bec de Loup Solitaire ! » Le
Zakhan parvient à dissimuler sa peur mais le temps joue contre
lui. La partie de bluff qu'il a engagée est très dangereuse.
Cependant, il n'a pas encore été percé à jour et c'est une preuve
de la force de la volonté car le Seigneur des Ténèbres fait de
grands efforts pour essayer de connaître le fond de sa pensée. « Vous aurez votre Homme du Nord, Seigneur Haakon, répond
sèchement le Zakhan, mais puisque vous prétendez n'avoir aucun
besoin d'or ni de bijoux, alors pourquoi vos hommes ont-ils pillé
les tombes de nos ancêtres et profané la sépulture du Majhan ? »
Un silence de mort règne dans la salle, troublé seulement par le
sifflement de la respiration du Seigneur des Ténèbres. « Ce pays,
dit-il, cet insignifiant lopin de sable recèle deux échardes
enfoncées douloureusement dans notre chair et nous voulons
nous en débarrasser une bonne fois pour toutes. Loup Solitaire
est l'une d'elles ; à cause de lui, nous n'avons aucun pouvoir au
Sommerlund. La tombe du Majhan cache l'autre épine qui nous
menace : ce maudit Livre du Magnakaï. » Votre cœur bat à tout
rompre lorsque ces mots résonnent à vos oreilles : le Livre du
Magnakaï ! La raison pour laquelle vous avez été entraîné dans
ce piège mortel devient alors claire et la sinistre vérité vous
apparaît subitement. Le Livre du Magnakaï est un recueil des
plus vieilles légendes du Sommerlund. L'Aigle du Soleil, le
premier Grand Maître Kaï, a pu, grâce à la sagesse et au savoir
qu'enseigne le Magnakaï, instruire les guerriers de la maison
d'Ulnar. Votre roi est issu de cette lignée de guerriers qui avaient
pour mission de défendre votre pays contre les attaques et les
dévastations perpétrées par les Seigneurs des Ténèbres. Le Livre
du Magnakaï a été perdu il y a des centaines d'années, mais sa
sagesse est parvenue vivante jusqu'à maintenant, transmise
oralement de génération en génération par les guerriers du
Sommerlund. C'est ainsi qu'ils ont pu faire face et résister à leurs
ennemis de toujours : les Seigneurs des Ténèbres d'Helgedad. Si
ces derniers découvrent le Livre de Magnakaï, ils le détruiront ;
ses secrets seront perdus à jamais et, à votre mort, le Kaï
s'éteindra. En revanche, si vous trouvez le Livre avant les
Seigneurs des Ténèbres, toute la sagesse du Magnakaï vous sera
révélée et, grâce à ce savoir, vous deviendrez fort, suffisamment
fort pour arriver à la consécration pour un guerrier du
Sommerlund : devenir Grand Maître Kaï. Cette glorieuse quête et
ses grands périls vous font oublier que des dangers plus
immédiats vous menacent.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.success("**Fin de la première partie.** La quête du Livre du Magnakaï commence.")
    st.write_stream(stream_text('Pour connaître ces dangers et commencer la quête du Livre du Magnakaï, rendez-vous dans la deuxième partie du Tyran du Désert. Commencez votre nouvelle aventure au :'))
    st.page_link("tomes/tome5/page_201.py", label="201", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
