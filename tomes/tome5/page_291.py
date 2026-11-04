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

check_inventory(current_page_number=291, book=5)

fr_text = """
Vous apprenez que les Nains formaient jadis l'équipage d'un
vaisseau beaucoup plus conventionnel appartenant à un riche
armateur dont les bateaux sillonnaient les Tentarias, du sud du
Magnamund. Les Tentarias regroupent des milliers de lacs et
d'archipels qui forment une sorte de canal étendu sur plusieurs
milliers de kilomètres. Ils furent formés, ainsi que le Rymerift de
Durenor, par un gigantesque glissement de terrain. Il y a trois
ans, le précédent capitaine des Nains, un Nain appelé Quan,
perdit son bateau, son chargement et son équipage en jouant aux
cartes. Il semble que l'infortuné capitaine n'ait été au courant de
la véritable profession de Banedon que bien trop tard ! C'est ainsi
que Banedon devint le capitaine des Nains, et depuis ils ont vécu
ensemble de nombreuses aventures sous les cieux du sud du
Magnamund. La Nef du ciel, quant à elle, fut donnée à Banedon
par les magiciens de Dessi en récompense de son aide précieuse
qui contribua largement à la défaite du Gagadoth, une créature
monstrueuse qui terrorisait leur pays et que leur propre
sorcellerie ne parvenait pas à maîtriser. La Nef du ciel faisait
route de Dessi à Barrakeesh lorsque vous fîtes votre apparition.
Les Nains n'ont pas perdu un mot de votre conversation avec
Banedon et ils sont tout excités à l'idée d'une nouvelle aventure,
apparemment inconscients des dangers qui les attendent.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_359.py", label="359", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
