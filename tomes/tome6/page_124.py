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

# objet testé : BILLET DE BATEAU (acheté au 10)

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=124, book=6)

fr_text = """
La cité grouille littéralement de monde : des mercenaires venus
du nord ou de l'ouest, des marchands d'armes arrivés de l'est et
des centaines de réfugiés en haillons ayant fui le sud du pays
ravagé par la guerre. Le capitaine ordonne à ses hommes de
dormir à bord du Kazonara et de ne pas mettre pied à terre de
toute la nuit, car le prince Baloon de Rioma et sa troupe de
chevaliers-mercenaires ont établi leur camp à l'intérieur de la
ville. Une rivalité de longue date oppose les deux compagnies,
et le Capitaine, par un excès de prudence qui l'honore, tient à
éviter toute confrontation. Le bruit court qu'un certain nombre
de Princes des Pays de la Storn, parmi les plus puissants, se
sont réunis à Rhem pour fomenter un complot contre les Sloviens.
Cependant, le Capitaine estime, quant à lui, qu'il ne s'agit là
que d'une manœuvre de conspiration mutuelle, destinée à se
surveiller les uns les autres pour s'approprier chacun la plus
grande part des richesses de Tekaro. Le bateau lève l'ancre aux
premières lueurs du jour, saluant au passage les deux grandes
tours de la citadelle de Rhem qui projettent sur les quais leur
ombre démesurée. La Storn serpente vers le sud, au pied des
vignobles escarpés qui s'étendent à perte de vue sur les
coteaux, tel un océan de verdure. Il fait chaud et vous passez
la journée sur le pont, à regarder les cohortes de réfugiés qui
se traînent sur la grand-route pour gagner le nord, ainsi que le
spectacle offert par les Batrax, de gigantesques crapauds
utilisés dans cette région pour tirer bateaux et péniches à
contre-courant. A la fin de la journée, la ville d'Eula se
profile enfin dans le lointain. Vous sellez votre cheval et vous
préparez votre équipement tandis que le Kazonara jette l'ancre
près de l'embarcadère en bois.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # billet acheté à Soren (paragraphe 10), quelle que soit la destination
    has_ticket = any(has_item(f"BILLET POUR {city}") for city in ("LUYEN", "RHEM", "EULA"))

    st.write_stream(stream_text("Si vous avez acheté votre Billet de voyage en bateau à Soren, rendez-vous au :"))
    if has_ticket:
        st.page_link("tomes/tome6/page_59.py", label="59", icon="📄")
    else:
        st.page_link("tomes/tome6/page_59.py", label="59", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous n'avez pas de Billet, rendez-vous au :"))
    if not has_ticket:
        st.page_link("tomes/tome6/page_290.py", label="290", icon="📄")
    else:
        st.page_link("tomes/tome6/page_290.py", label="290", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
