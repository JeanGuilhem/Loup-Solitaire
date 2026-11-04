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

check_inventory(current_page_number=343, book=5)

fr_text = """
L'Itikar quitte son perchoir et vous êtes violemment rejeté en
arrière de la selle. Le grand oiseau noir pousse des croassements
aigus en battant des ailes dans un bruit de tonnerre. Au moment
où il prend son envol depuis la tour, vous apercevez, tout en bas,
quelques Drakkars éparpillés, pas plus grands que des poupées.
Soudain, vous voyez en un éclair un guerrier Drakkar, dont le
masque à tête de mort a été coupé en deux par les serres
tranchantes de l'oiseau, tomber de la plate-forme vers une mort
certaine dans les jardins du Palais en contrebas. Les dômes dorés
du Grand Palais deviennent de plus en plus petits au fur et à
mesure que l'Itikar prend de l'altitude. Vous passez rapidement
au-dessus des murailles de la ville et vous vous dirigez vers la
grande plaine salée du lac Inrahim. A l'ouest, le soleil qui se
couche derrière les montagnes du Dahir baigne le paysage d'une
belle lumière orangée. Le cœur plein d'allégresse, vous rejetez la
tête en arrière en poussant un cri de triomphe que le vent frais
du soir emporte au loin. Mais comme en réponse à votre cri, un
chœur de croassements stridents retentit dans le ciel. La peur
s'empare de vous à nouveau lorsque vous apercevez une
formation de Kraans, ces affreux oiseaux aux ailes dures comme
du cuir, qui transportent chacun un guerrier Drakkar sur le dos.
Ils sont à plus d'un kilomètre de vous pour l'instant, mais ils se
rapprochent à vive allure. Dans une heure, la nuit sera tombée et
si vous pouvez continuer à voler jusqu'à ce que l'obscurité soit
totale, vous parviendrez à les semer. Vous êtes à présent juste au-
dessus du centre du lac et vous devez choisir une direction. Avant
de prendre une décision, consultez la carte qui figure au début de
ce livre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous désirez voler vers le sud, en empruntant le passage du Dahir, rendez-vous au :'))
    st.page_link("tomes/tome5/page_264.py", label="264", icon="📄")

    st.write_stream(stream_text("Si vous préférez aller vers l'est, vers la ville de Chula, rendez-vous au :"))
    st.page_link("tomes/tome5/page_244.py", label="244", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
