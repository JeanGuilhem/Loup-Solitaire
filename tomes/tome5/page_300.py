import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=300, book=5)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
Vous êtes réveillé peu après le lever du soleil par les ronflements
des Nains et le bourdonnement grave qu'émet la Nef du ciel.
Vous rassemblez votre équipement, puis vous grimpez sur le
pont. Tout est plongé dans l'obscurité car la Nef du ciel est en
train de planer juste en dessous d'un énorme rocher de grès qui
s'avance en saillie du flanc de la montagne, à des centaines de
mètres au-dessus de la vallée. Banedon est toujours à la barre,
mais il n'est plus en transes. « Des Kraans ! crie-t-il tout à coup,
en pointant l'index vers la vallée écrasée de soleil, par-delà
l'ombre projetée par le rocher. Ils arrivent avec l'aube. » Vous
contemplez cet étrange paysage, un plateau montagneux
fantastique, profondément encaissé, d'où s'élèvent d'énormes
rochers qui forment de véritables colonnes rocheuses dont
l'équilibre semble très précaire. Les Vassagoniens appellent cet
endroit les Foos, c'est-à-dire les Aiguilles. Ces colonnes de pierre
s'élancent si haut que vous avez l'impression qu'elles vont
s'écrouler d'une minute à l'autre. Perchés sur ces cheminées de
pierre, vous apercevez des Kraans et, debout à côté d'eux, des
Drakkars qui scrutent la vallée avec des longues-vues. Ils restent
ainsi plus d'une heure, puis ils s'envolent dans les airs et
disparaissent. « Hissez la grand-voile ! » ordonne Banedon d'une
voix tout juste audible dans le vacarme assourdissant que fait la
Nef du ciel en vrombissant. « Nous devons fuir rapidement et
une longue course nous attend. »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez un Cube de Cristal noir, rendez-vous au :"))
    if has_item("CUBE DE CRISTAL NOIR"):
        st.page_link("tomes/tome5/page_229.py", label="229", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome5/page_229.py", label="229", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne possédez pas cet Objet Spécial, rendez-vous au :"))
    if has_item("CUBE DE CRISTAL NOIR"):
        st.page_link("tomes/tome5/page_247.py", label="247", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome5/page_247.py", label="247", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
