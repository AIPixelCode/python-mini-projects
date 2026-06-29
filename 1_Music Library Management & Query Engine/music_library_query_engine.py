def add_user(
    username: str,
    age: int,
    city: str,
    albums: list[str],
    all_users: dict,) -> None:
    """Add a new user to the user database."""
    all_users[username] = {
        "age": age,
        "city": city,
        "albums": albums,
    }


def add_album(
    name: str,
    artist: str,
    genre: str,
    tracks: int,
    all_albums: dict,) -> None:
    """Add a new album to the album database."""
    all_albums[name] = {
        "artist": artist,
        "genre": genre,
        "tracks": tracks,
    }


def count_tracks(
    albums: list[str],
    all_albums: dict,
    key: str,
    value: str,) -> int:
    """Count the total number of tracks that match a given album property."""
    total = 0
    for album in albums:
        if all_albums[album][key] == value:
            total += all_albums[album]["tracks"]
    return total


def filter_users(
    all_users: dict,
    key: str,
    value,) -> list[dict]:
    """Return users whose property matches the given value."""
    return [
        user
        for user in all_users.values()
        if user[key] == value
    ]


def query_user_artist(
    username: str,
    artist: str,
    all_users: dict,
    all_albums: dict,) -> int:
    """Return the number of purchased tracks by artist for a specific user."""
    return count_tracks(
        all_users[username]["albums"],
        all_albums,
        "artist",
        artist,
    )


def query_user_genre(
    username: str,
    genre: str,
    all_users: dict,
    all_albums: dict,) -> int:
    """Return the number of purchased tracks by genre for a specific user."""
    return count_tracks(
        all_users[username]["albums"],
        all_albums,
        "genre",
        genre,
    )


def query_age_artist(
    age: int,
    artist: str,
    all_users: dict,
    all_albums: dict,) -> int:
    """Return the total number of purchased tracks by artist for users of a given age."""
    total = 0

    for user in filter_users(all_users, "age", age):
        total += count_tracks(
            user["albums"],
            all_albums,
            "artist",
            artist,
        )
    return total


def query_age_genre(
    age: int,
    genre: str,
    all_users: dict,
    all_albums: dict,) -> int:
    """Return the total number of purchased tracks by genre for users of a given age."""
    total = 0
    for user in filter_users(all_users, "age", age):
        total += count_tracks(
            user["albums"],
            all_albums,
            "genre",
            genre,
        )
    return total


def query_city_artist(
    city: str,
    artist: str,
    all_users: dict,
    all_albums: dict,) -> int:
    """Return the total number of purchased tracks by artist for users in a city."""
    total = 0
    for user in filter_users(all_users, "city", city):
        total += count_tracks(
            user["albums"],
            all_albums,
            "artist",
            artist,
        )
    return total


def query_city_genre(
    city: str,
    genre: str,
    all_users: dict,
    all_albums: dict,) -> int:
    """Return the total number of purchased tracks by genre for users in a city."""
    total = 0
    for user in filter_users(all_users, "city", city):
        total += count_tracks(
            user["albums"],
            all_albums,
            "genre",
            genre,
        )
    return total