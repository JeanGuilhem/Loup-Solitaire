import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=380, book=5)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
Vous vous réveillez le lendemain peu après l'aube avec un violent
mal de tête. Parcourant la cabine des yeux, vous apercevez à
travers un brouillard les Nains entassés sur leurs couchettes qui
ronflent tranquillement. Le vrombissement grave et continu du
vaisseau augmente encore un peu plus votre migraine qui, tel un
démon, vous vrille les tempes. Vous devez serrer les dents pour
ne pas hurler de douleur au moindre mouvement de vos
membres raidis et endoloris. Cette atroce migraine vous fait
perdre 2 points d'ENDURANCE. Vous rassemblez péniblement
votre équipement et vous grimpez sur le pont. La Nef du ciel est
plongée dans l'obscurité la plus totale car le vaisseau est en train
de planer sous un gros rocher de grès qui jaillit en surplomb du
flanc de la montagne. Banedon est toujours debout à la barre
mais il n'est plus en transes. « Des Kraans ! » s'écrie-t-il, en
pointant un doigt vers la vallée en contrebas, écrasée de soleil
sous l'ombre immense prodiguée par le rocher. Vous regardez
cette vallée hostile d'où s'élèvent d'innombrables piliers formés
par l'amoncellement de blocs de pierre en équilibre précaire. Ces
colonnes sont si hautes qu'une avalanche de pierres semble
inévitable. Les Vassagoniens nomment cet endroit les Foos, c'est-à-dire les Aiguilles. Perchés sur deux de ces immenses colonnes
de pierre, se trouvent des Kraans avec, à leurs côtés, des
Drakkars qui scrutent la vallée à l'aide de longues-vues. Ils
restent ainsi une heure, puis disparaissent dans les airs sur leurs
montures. « Hisse la grand-voile, Nolrim ! ordonne Banedon,
d'une voix à peine audible dans le vrombissement de la Nef du
ciel. Nous avons une longue course à effectuer. »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)
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
