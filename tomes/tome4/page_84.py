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

check_inventory(current_page_number=84, book=4)

fr_text = """
Dans la faible lumière qui règne à l'intérieur, vous apercevez un
vieil homme assis à une table. Seules les flammes vacillantes d'un
feu de bois éclairent ce taudis malodorant. Elles répandent
cependant suffisamment de clarté pour vous permettre de
distinguer les tas de parchemins et d'instruments étranges qui
encombrent les lieux. L'homme détache lentement son regard
d'une grande sphère de cristal et vous invite à vous asseoir en
face de lui. « Comment se fait-il que vous connaissiez mon nom ? »
lui demandez-vous avec méfiance. « Notre rencontre était
depuis longtemps écrite dans les étoiles, Loup Solitaire, réplique-t-il
en effleurant la sphère de ses mains ridées. Mais ne vous
alarmez pas, je ne souhaite que vous aider. » Il sort alors d'une
poche de sa toge un rouleau de parchemin qu'il vous tend. Sur ce
parchemin sont écrits ces quelques vers :
Au soir de pleine lune, en un temple profond,
Sacrifice viendra à jamais réveiller
Les légions d'un Seigneur trop longtemps oublié,
Quand mourra sur l'autel la vierge aux cheveux blonds,
Des gorges de Maaken les morts se lèveront
Pour exiger enfin la rançon des guerriers.
Vous demandez la signification de cette étrange strophe, mais le
vieil homme ne vous répond pas. Il semble être entré dans une
transe profonde. Vous vous penchez par-dessus la table
encombrée pour essayer de le réveiller et vous êtes alors stupéfait
de constater que votre main passe à travers son corps. Peu à peu,
son image s'estompe et, quelques secondes plus tard, il a
complètement disparu. Vous glissez le Parchemin dans votre
poche (inscrivez-le sur votre Feuille d'Aventure dans la case
Objets Spéciaux), puis vous vous hâtez de quitter la masure en
essuyant la sueur froide qui perle à votre front.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        add_to_inventory("ROULEAU DE PARCHEMIN")
    st.success("*Le Rouleau de Parchemin est ajouté à vos Objets Spéciaux.*")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_273.py", label="273", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
