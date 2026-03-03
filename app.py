import streamlit as st
import pandas as pd
import pickle

# Charger le modèle entraîné
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Titre de l'application
st.title("Prédiction de la vitesse sportive")

# Formulaire pour saisir les données biométriques
st.header("Entrez les données biométriques")
age = st.number_input("Âge (années)", min_value=10, max_value=100)
weight = st.number_input("Poids (kg)", min_value=30.0, max_value=200.0)
height = st.number_input("Taille (cm)", min_value=100.0, max_value=250.0)
bmi = st.number_input("IMC (kg/m²)", min_value=10.0, max_value=50.0)
gender = st.selectbox("Genre", options=[0, 1], format_func=lambda x: "Femme" if x == 0 else "Homme")
jump_distance = st.number_input("Distance de saut (cm)", min_value=100.0, max_value=500.0)

# Bouton pour lancer la prédiction
if st.button("Prédire la vitesse"):
    # Créer un DataFrame avec les données saisies
    input_data = pd.DataFrame({
        'Age_Y': [age],
        'Weight_Kg': [weight],
        'Height_cm': [height],
        'BMI': [bmi],
        'Gender': [gender],
        'Jump_distance_cm': [jump_distance]
    })
    
    # Faire la prédiction
    prediction = model.predict(input_data)
    
    # Afficher le résultat
    st.success(f"La vitesse prédite est : {prediction[0]:.2f} m/s")