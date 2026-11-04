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

check_inventory(current_page_number=1, book=5)

fr_text = """
Durant 25 jours, la galère vassagonienne à bord de laquelle vous
êtes parti de Holmgard fait route vers Barrakeesh, son port
d'attache. Seule une courte escale à Port-Bax, dans le pays de
Durenor, est venue rompre la monotonie du voyage, et vous
mettez à profit vos longs moments de loisirs pour apprendre, au
contact des membres de l'équipage, la langue du pays où vous
vous rendez. Les marins ne sont que trop heureux de vous
enseigner le vassagonien, et ils ne vous demandent en échange
que de leur raconter les aventures qui vous sont arrivées dans les
Fins de Terre. Pour nombre d'entre eux, ce sont les récits les plus
passionnants qu'ils aient jamais entendus ! Avant même que
vous ayez atteint Barrakeesh, vous parlez couramment la langue
que vous ont enseignée les marins vassagoniens et vous avez, de
plus, gagné leur estime.
Dans l'après-midi du vingt-cinquième jour, les remparts de la
capitale du désert apparaissent enfin à l'horizon. Vous vous
frayez un chemin parmi les membres enthousiastes de l'équipage
pour rejoindre l'envoyé de Vassagonie à la proue du navire.
Celui-ci, le visage rayonnant de fierté, vous tend une longue-vue
et vous invite à regarder le pays qui l'a vu naître. La vue qui
s'offre à vos yeux est effectivement époustouflante. Vous
découvrez, fasciné, les coupoles dorées, les nombreux minarets,
les toits de tuile verte qui scintillent sous le soleil du désert, et
vous vous émerveillez de la splendeur du Grand Palais qui
domine cette ville magnifique. Soudain, vous remarquez qu'à
chaque tourelle du Palais flotte un long drapeau noir. Lorsque
vous demandez à l'envoyé la signification de ces étendards, vous
voyez une expression d'horreur se peindre sur son visage. D'un
geste vif, il s'empare de la longue-vue et s'écrie : « Par l'esprit du
Majhan ! Il est mort... le Zakhan est mort ! » Sur le bateau, la
triste nouvelle se répand comme une traînée de poudre et vous
priez pour que le traité de paix soit tout de même signé et
respecté par le successeur du Zakhan. Mais à ce propos, l'envoyé
se montre plus que pessimiste. Lorsque vous mettez pied à terre,
vous constatez que le port de Barrakeesh est désert, exception
faite d'une poignée de citoyens portant le deuil. Seul le tintement
des cloches sonnant le glas vous accueille en ce jour funèbre.
Soudain, une voiture tirée par des chevaux et escortée par la
cavalerie de la Garde du Palais débouche sur la place du port et
un homme sévère, vêtu d'une tunique turquoise, vient à votre
rencontre : « Soyez le bienvenu, Loup Solitaire. Je suis Maouk, et
j'ai été chargé de vous accueillir en notre ville au nom de mon
maître, Son Altesse Sérénissime, le Zakhan Kimah. » En
entendant le nom du nouveau Zakhan, l'envoyé ne peut retenir
un hoquet de surprise ; il se tourne vers vous, les yeux agrandis
par la peur, et vous dit : « C'est un piège ! Vous devez vv... »
A ce moment, Maouk lui porte un violent coup de poignard et
l'envoyé ne peut achever sa phrase. Une vingtaine de guerriers
vêtus de noir émergent soudain de l'ombre: ce sont les
Sharnazims, l'élite de la garde vassagonienne. Ils s'approchent de
vous et vous encerclent. Vous devez agir rapidement si vous
voulez échapper à ce piège mortel.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez affronter ces hommes, bien qu'ils vous surpassent en nombre, rendez-vous au :"))
    st.page_link("tomes/tome5/page_36.py", label="36", icon="📄")
    st.write_stream(stream_text('Si vous préférez vous rendre et vous soumettre à Maouk et ses guerriers, rendez-vous au :'))
    st.page_link("tomes/tome5/page_176.py", label="176", icon="📄")
    st.write_stream(stream_text('Si vous voulez, en revanche, retourner en courant vers la galère sur laquelle vous êtes arrivé, rendez-vous au :'))
    st.page_link("tomes/tome5/page_104.py", label="104", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
