import pandas as pd

# Load dataset
movies = pd.read_csv("movies.csv")

print("=" * 55)
print("      🎬 AI Movie Recommendation System")
print("=" * 55)

genres = movies["Genre"].unique()

print("\nAvailable Genres")

for i, g in enumerate(genres, start=1):
    print(f"{i}. {g}")

choice = input("\nEnter your favourite genre: ").strip()

recommend = movies[movies["Genre"].str.lower() == choice.lower()]

if len(recommend) > 0:

    print("\nRecommended Movies\n")

    for movie in recommend["Movie"]:
        print("⭐", movie)

else:
    print("\nSorry! No recommendations found.")
