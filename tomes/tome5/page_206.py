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

check_inventory(current_page_number=206, book=5)

fr_text = """
Vous frappez mais vous n'obtenez aucune réponse. Vous vous
apprêtez à frapper une nouvelle fois, lorsque la porte s'entrouvre
de quelques centimètres. Vous apercevez les yeux rougeoyants
d'une vieille femme qui brillent dans les ténèbres.
« Banedon ! s'écrit-elle, d'une voix chevrotante et enrouée. Grâce
à Dieu, c'est vous. » Elle vous introduit tous deux dans la maison
et verrouille la porte. La pièce est presque vide et les quelques
meubles qui s'y trouvent sont cassés ou en mauvais état. « Ils
l'ont pris, Banedon. Les hommes au visage de mort ont pris mon
mari. Il y a dix jours... Ils sont venus comme des ombres dans la
nuit. » Tout à coup, elle s'effondre, son corps maigre secoué par
les sanglots. Banedon la réconforte du mieux qu'il peut, mais
vous sentez qu'il partage également sa douleur. Les Drakkars se
sont emparés de Tipasa, il n'y a pas de doute et, à l'heure
actuelle, ils ont déjà dû lui faire dire tout ce qu'il savait au sujet
du Tombeau du Majhan. « Nous le trouverons, je vous le promets,
dit Banedon en essuyant les larmes qui ruissellent sur le visage
de la vieille femme. Mais vous devez essayer de nous aider si
vous le pouvez. Nous savons que Tipasa gardait toujours un
journal de ses voyages. Est-il toujours en votre possession ? »
Une étincelle d'espoir se met à luire dans les yeux de la vieille
femme. « Oui, il est ici. Il m'a dit de le cacher quand ces brutes
sont venues le chercher. » Elle s'agenouille devant la cheminée,
déloge une brique descellée dans l'âtre, puis en retire un livre
relié de cuir. Elle le tend à Banedon qui en étudie très
attentivement les pages jaunies. En regardant par-dessus son
épaule, vous remarquez que le livre est rempli de symboles
secrets, de chiffres et de mystérieux pictogrammes. « Toutes ces
figures représentent les différentes positions des étoiles, dit
Banedon en suivant du doigt les lignes de la carte astronomique.
Je suis sûr qu'elles recèlent le secret que nous cherchons, mais
sans ma carte du ciel, nous ne réussirons pas à trouver le
Tombeau du Majhan. Dès les premières lueurs de l'aube, nous
retournerons à la Nef du ciel. Une fois à bord, je devrais pouvoir
comprendre l'énigme de ce livre. »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_331.py", label="331", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
