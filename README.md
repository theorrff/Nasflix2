import requests

# Votre clé API et recherche
api_key = "d89fa934fa20f9da82626ff5b6074e3e"
query = "Avatar"  # Remplacez par votre recherche
language = "fr-FR"
year = "2009"

# Construire l'URL
url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={query}&year={year}&language={language}"

# Faire la requête
response = requests.get(url)

# Vérifier la réponse
if response.status_code == 200:
    data = response.json()  # Récupérer les données en JSON
    # Afficher les films trouvés
    for movie in data.get("results", []):
        print(f"Titre : {movie['title']}")
        print(f"Date de sortie : {movie['release_date']}")
        print(f"Description : {movie['overview']}\n")
else:
    print(f"Erreur : {response.status_code}")
