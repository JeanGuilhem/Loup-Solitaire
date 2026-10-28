import streamlit as st
from combat import combat, table_coups
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies, hazard_roll, ls_death

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=88, book=3)

fr_text = """
Tandis que le serpent à deux têtes rampe vers vous le long de la
corniche, vous le voyez ouvrir les mâchoires de sa seconde tête,
laissant apparaître deux crochets jaunes au bout desquels perle
une goutte de venin. Vous ôtez aussitôt votre épaisse tunique que
vous enroulez autour de votre bras. Vous pourrez ainsi vous
protéger contre l'une des têtes pendant que vous combattrez
l'autre. Il est à noter que cette créature est insensible à la
Discipline Kaï de la Puissance Psychique.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Si vous perdez des points d'ENDURANCE au cours de ce combat, ne les soustrayez pas de votre total. "
            "Utilisez d'abord la Table de Hasard pour obtenir un chiffre. Si vous tirez un chiffre de 0 à 8, "
            "le Javek aura enfoncé ses crochets dans la tunique qui protège votre bras et vous n'aurez alors "
            "perdu aucun point d'ENDURANCE. Si en revanche, vous tirez le 9, les crochets vous auront atteint. "
            "Or, le venin du Javek est le poison le plus puissant qui existe dans toutes les terres de "
            "Magnamund. Votre cœur s'arrêtera donc de battre quelques secondes plus tard et votre cadavre "
            "tombera dans le précipice. Dans cette hypothèse, il va sans dire que votre mission serait "
            "brutalement interrompue."
        )
    )
    st.info(
        "*Vous ne perdez aucun point d'ENDURANCE pendant ce combat. Après le combat, utilisez la Table de "
        "Hasard une fois pour chaque assaut où le Javek vous a touché.*"
    )
    outcome = combat([("JAVEK", 15, 15)], psychic_immune=True, ls_immune_rounds=999)
    if outcome == "win":
        # assauts où la Table des Coups Portés vous infligeait une perte (None = tué sur le coup)
        log = st.session_state["combat_combat"]["log"]
        bites = [entry for entry in log if table_coups(entry["quotient"], entry["dice"])[1] != 0]
        safe = True
        for number, entry in enumerate(bites, start=1):
            roll = hazard_roll(
                key=f"javek_{number}",
                label=f"Le Javek vous a touché à l'assaut {entry['round']} : utilisez la Table de Hasard.",
            )
            if roll is None:
                safe = False
                break
            if roll == 9:
                st.write_stream(
                    stream_text(
                        "Les crochets du Javek vous ont atteint. Votre cœur cesse de battre et votre cadavre "
                        "tombe dans le précipice. Votre mission s'achève ici."
                    )
                )
                show_illustrations()
                ls_death()
            st.write("*Les crochets se sont enfoncés dans la tunique qui protège votre bras.*")
        if safe:

            st.write_stream(stream_text('Si vous sortez vainqueur de ce combat, rendez-vous au :'))
            st.page_link("tomes/tome3/page_269.py", label="269", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
