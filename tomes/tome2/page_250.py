import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=250, book=2)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
Le soldat vous regarde d'un air incrédule. « Où sont vos marchandises ?
s'étonne-t-il, où est votre cheval ? Et votre chariot ? Les marchands ne
viennent jamais à Port Bax à pied. Vous, un marchand ? Laissez-moi
rire ! J'ai plutôt l'impression que vous êtes un brigand qui essaie de fuir
les lieux de quelque inavouable forfait. Retournez donc d'où vous
venez, misérable canaille, nous n'avons pas besoin ici du genre de
commerce que vous pratiquez. » Si vous voulez passer vivant cette
frontière, il vous faudra trouver autre chose. Qu'allez-vous faire ?
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Repartir, faire un grand détour et pénétrer dans la forêt plus au sud ? Rendez-vous au :'))
    st.page_link("tomes/tome2/page_244.py", label="244", icon="📄")

    st.write_stream(stream_text('Essayer de corrompre le garde ? Il faudra vous rendre au :'))
    st.page_link("tomes/tome2/page_68.py", label="68", icon="📄")

    st.write_stream(stream_text("Montrer le Sceau d'Hammardal (en admettant qu'il soit toujours en votre possession) ? Rendez-vous dans ce cas au :"))
    if has_item("SCEAU D'HAMMARDAL"):
        st.page_link("tomes/tome2/page_223.py", label="223", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome2/page_223.py", label="223", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
