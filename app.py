import streamlit as st

st.set_page_config(
    page_title="TIWAS - Tell It With A Song",
    page_icon="🎵",
    layout="centered",
)

st.title("🎵 TIWAS - Tell It With A Song")
st.write("Dépose ton texte et je le transforme en chanson !")

# Texte à analyser
texte_utilisateur = st.text_area("Ton message (500 caractères max)", max_chars=500)

# Menus déroulants
sexe_expediteur = st.selectbox("Sexe de l'expéditeur :", ["M", "F", "NG"])
sexe_destinataire = st.selectbox("Sexe du destinataire :", ["M", "F", "NG"])
age_expediteur = st.selectbox("Âge de l'expéditeur :", list(range(10, 101)))
age_destinataire = st.selectbox("Âge du destinataire :", list(range(10, 101)))
langues = st.multiselect("Choix de langue(s) :", ["Français", "Anglais", "Espagnol", "Allemand", "Italien"])
artiste_prefere = st.text_input("Artiste ou groupe préféré :")

style_musical = st.selectbox("Style musical :", [
    "Pop", "Rock", "Hip-hop", "Jazz", "Classique", "Electro", "Reggae", "Blues", "Country", "Metal", "Funk", "Soul"
])

periode = st.selectbox("Période :", [
    "1960s", "1970s", "1980s", "1990s", "2000s", "2010s", "2020s"
])

duree_extraits = st.slider("Durée des extraits musicaux (en secondes) :", 2, 8, 4)
transition = st.selectbox("Type de transition :", [
    "Aléatoire", "Scratch de DJ", "Bang Bang", "Hurlement de loup", "Battements de cœur", "Riff de guitare"
])

theme_message = st.selectbox("Thème du message :", [
    "Déclaration d’amour", "Désir", "Déclaration d’amitié", "Annonce de rupture", "Annonce de naissance",
    "Annonce de mariage", "Décès"
])

if st.button("🎶 Générer la chanson !"):
    st.success("La génération commencera ici. (WIP)")
