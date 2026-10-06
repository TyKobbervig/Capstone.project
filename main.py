import json


# Load game data from JSON file
def load_game_data(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        print("Error: game_data.json not found.")
        return []

    except json.JSONDecodeError as e:
        print("JSON Error:", e)
        return []


# Get user's search preferences
def get_user_preferences():

    valid_genres = [
        "rpg",
        "action",
        "adventure",
        "strategy",
        "sports"
    ]

    valid_platforms = [
        "pc",
        "playstation 4",
        "playstation 5",
        "xbox one",
        "xbox series x",
        "nintendo switch"
    ]

    print("\nAvailable Genres:")
    for genre in valid_genres:
        print("-", genre.title())

    while True:
        genre = input("\nChoose a genre: ").strip().lower()

        if genre in valid_genres:
            break

        print("Invalid genre. Please try again.")

    print("\nAvailable Platforms:")
    for platform in valid_platforms:
        print("-", platform.title())

    while True:
        platform = input("\nChoose a platform: ").strip().lower()

        if platform in valid_platforms:
            break

        print("Invalid platform. Please try again.")

    return genre, platform


# Find matching games
def find_recommendations(games, genre, platform):

    recommendations = []

    for game in games:

        if game["genre"].lower() == genre:

            for game_platform in game["platforms"]:

                if game_platform.lower() == platform:
                    recommendations.append(game)
                    break

    recommendations.sort(
        key=lambda game: game["rating"],
        reverse=True
    )

    return recommendations


# Display matching games
def display_recommendations(recommendations):

    if len(recommendations) == 0:
        print("\nNo games matched your search.")
        return

    print(f"\nFound {len(recommendations)} game(s)")
    print("=" * 50)

    for game in recommendations:

        print(f"\nTitle: {game['title']}")
        print(f"Genre: {game['genre'].title()}")
        print(f"Platforms: {', '.join(game['platforms'])}")
        print(f"Rating: {game['rating']}")

        print("-" * 50)


# Main Program
def main():

    print("=" * 50)
    print("      GAME RECOMMENDATION FINDER")
    print("=" * 50)

    games = load_game_data("game_data.json")

    if not games:
        return

    while True:

        genre, platform = get_user_preferences()

        recommendations = find_recommendations(
            games,
            genre,
            platform
        )

        display_recommendations(recommendations)

        again = input(
            "\nWould you like to search again? (yes/no): "
        ).strip().lower()

        if again != "yes":
            print("\nThank you for using Game Recommendation Finder!")
            break


main()