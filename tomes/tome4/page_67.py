import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    has_kai,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=67, book=4)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
Vos hommes sont affamés et épuisés, mais leur confiance dans
l'infaillibilité de votre intuition de Seigneur Kaï reste
inébranlable. Vous donnez donc le signal du départ. Lorsque
vous arrivez à la sortie de la ville, cependant, vous entendez un
sifflement. Un patrouilleur à côté de vous pousse alors un
hurlement de douleur : un disque d'acier aux bords acérés vient
de s'enfoncer dans sa poitrine. Plusieurs autres disques sont
aussitôt lancés depuis les toits. L'un d'eux vous écorche le dos de
la main avant de se loger dans l'encolure de votre cheval. Vous
êtes projeté à terre et vous perdez 1 point d'ENDURANCE. Vous
vous relevez et vous vous mettez à courir en direction d'un
chariot pour vous y abriter. Deux de vos hommes sont étendus
sur le sol, tués par les disques d'acier, mais les autres ont pu fuir
l'embuscade et s'éloignent de la ville au galop, cachés par des
nuages de poussière. Soudain, vous apercevez un Guerrier Pillard
qui se tient debout sur un balcon proche. Il a la peau sombre, des
cheveux et une barbe d'un noir huileux. A cet instant, il fait un
geste de la main et un disque mortel jaillit dans votre direction.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-1)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-1)

    st.write_stream(stream_text("Si vous possédez le Glaive de Sommer, rendez-vous au :"))
    if has_item("GLAIVE DE SOMMER"):
        st.page_link("tomes/tome4/page_292.py", label="292", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome4/page_292.py", label="292", icon="📄", disabled=True)

    if not has_item("GLAIVE DE SOMMER"):
        st.write_stream(stream_text("Sinon, utilisez la Table de Hasard pour obtenir un chiffre. Si vous possédez la Discipline Kaï de la Chasse ou celle de la Maîtrise Psychique de la Matière, ajoutez 2 au chiffre que vous aurez tiré."))
        roll = hazard_roll()
        if roll is not None:
            bonus = 2 if has_kai("La Chasse") or has_kai("Maîtrise Psychique de la Matière") else 0
            total = roll + bonus
            if bonus:
                st.write(f"*Bonus de Discipline Kaï : +2, soit un total de {total}.*")
            if total <= 4:
                st.write_stream(stream_text("Si le total obtenu est de 0 à 4, rendez-vous au :"))
                st.page_link("tomes/tome4/page_242.py", label="242", icon="📄")
            elif total <= 8:
                st.write_stream(stream_text("De 5 à 8, rendez-vous au :"))
                st.page_link("tomes/tome4/page_263.py", label="263", icon="📄")
            else:
                st.write_stream(stream_text("De 9 à 11, rendez-vous au :"))
                st.page_link("tomes/tome4/page_278.py", label="278", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
