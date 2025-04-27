import streamlit as st
import openai
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random

# Chargement des secrets
openai.api_key = st.secrets["openai"]["api_key"]

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=st.secrets["spotify"]["client_id"],
    client_secret=st.secrets["spotify"]["client_secret"]
))

# Interface Streamlit
st.set_page_config(page_title="TIWAS - Tell It With A Song", page_icon="🎵", layout="centered")

st.title("🎶 TIWAS - Tell It With A Song")
st.subheader("Décris ton émotion, TIWAS te propose une bande son !")

with st.form(key="formulaire_tiwas"):
    texte = st.text_area("✍️ Dépose ton message (max 500 caractères)", max_chars=500)
    sexe_expediteur = st.selectbox("Sexe de l'expéditeur", ["Masculin", "Féminin", "Non genré"])
    sexe_destinataire = st.selectbox("Sexe du destinataire", ["Masculin", "Féminin", "Non genré"])
    age_expediteur = st.number_input("Âge de l'expéditeur", min_value=1, max_value=120, step=1)
    age_destinataire = st.number_input("Âge du destinataire", min_value=1, max_value=120, step=1)
    theme = st.selectbox("Thème du message", [
        "Déclaration d’amour", "Désir", "Déclaration d’amitié", 
        "Annonce de rupture / Séparation", "Annonce de naissance", 
        "Annonce de mariage", "Décès"
    ])
    submit_button = st.form_submit_button(label="🎶 Générer la chanson !")

if submit_button:
    if texte.strip() == "":
        st.error("Merci d'écrire un texte avant de générer.")
    else:
        with st.spinner('Analyse du message...'):

            # Envoyer le texte à OpenAI pour extraire 3 mots-clés
            prompt = f"""
            Analyse le message suivant et propose 3 mots-clés musicaux associés. 
            Message : "{texte}"
            Réponds uniquement avec les mots-clés séparés par une virgule.
            """
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=50
            )
            mots_cles = response['choices'][0]['message']['content']
            mots_cles_list = [mot.strip() for mot in mots_cles.split(",")]

        st.success(f"Mots-clés détectés : {', '.join(mots_cles_list)}")

        # Recherche de morceaux Spotify
        st.subheader("🎵 Résultat :")

        morceaux = []
        for mot in mots_cles_list:
            resultats = sp.search(q=mot, type="track", limit=5)
            morceaux_trouves = resultats['tracks']['items']
            morceaux.extend(morceaux_trouves)

        if morceaux:
            morceaux_random = random.sample(morceaux, min(5, len(morceaux)))
            for track in morceaux_random:
                st.markdown(f"**{track['name']}** par *{track['artists'][0]['name']}*")
                st.audio(track['preview_url']) if track['preview_url'] else st.write("(Pas d'extrait disponible)")
        else:
            st.error("Aucun morceau trouvé. Essaie avec un texte différent.")

