import pandas as pd
from pathlib import Path
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
import pickle  # Import pour sauvegarder le modèle

# Charger les données nettoyées
file_path = Path(__file__).parent / 'cleaned_dataset.csv'
df = pd.read_csv(file_path)

# Sélectionner les variables prédictives et la cible
X = df[['Age_Y', 'Weight_Kg', 'Height_cm', 'BMI', 'Gender', 'Jump_distance_cm']]
y = df['Speed_m/s']

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Définir les paramètres pour GridSearch
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 10],
    'learning_rate': [0.01, 0.1, 0.2]
}

# Initialisation du modèle
model = GradientBoostingRegressor(random_state=42)

# GridSearch pour optimiser les hyperparamètres
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, scoring='neg_mean_squared_error')
grid_search.fit(X_train, y_train)

# Meilleurs paramètres et modèle optimisé
best_model = grid_search.best_estimator_

# Évaluation du modèle optimisé
y_pred = best_model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")

# Sauvegarder le modèle optimisé dans un fichier .pkl
with open("model.pkl", "wb") as file:
    pickle.dump(best_model, file)

print("Modèle sauvegardé sous le nom 'model.pkl'")
import os
print("Fichier sauvegardé dans :", os.getcwd())

