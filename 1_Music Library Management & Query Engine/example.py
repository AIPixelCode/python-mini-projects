from music_library_query_engine import *

all_users = {}
all_albums = {}

# Add users
add_user("john_doe", 19, "London", ["hybrid_theory", "meteora", "minutes_to_midnight"], all_users)
add_user("emma_smith", 22, "New York", ["thriller", "meteora", "minutes_to_midnight"], all_users)
add_user("michael", 12, "Toronto", ["back_in_black", "parachutes"], all_users)

# Add albums
add_album("hybrid_theory", "Linkin Park", "Rock", 12, all_albums)
add_album("meteora", "Linkin Park", "Rock", 13, all_albums)
add_album("minutes_to_midnight", "Linkin Park", "Rock", 12, all_albums)
add_album("thriller", "Michael Jackson", "Pop", 9, all_albums)
add_album("back_in_black", "AC/DC", "Rock", 10, all_albums)
add_album("parachutes", "Coldplay", "Alternative", 10, all_albums)

print("=" * 60)
print("Music Library Management & Query Engine")
print("=" * 60)

print("\n--- Query by User and Artist ---")
print(
    f'Michael purchased '
    f'{query_user_artist("michael", "Coldplay", all_users, all_albums)} '
    f'track(s) by "Coldplay".')

print("\n--- Query by User and Genre ---")
print(
    f'Michael purchased '
    f'{query_user_genre("michael", "Rock", all_users, all_albums)} '
    f'rock track(s).')

print("\n--- Query by Age and Artist ---")
print(
    f'Users aged 12 purchased '
    f'{query_age_artist(12, "AC/DC", all_users, all_albums)} '
    f'track(s) by "AC/DC".')

print("\n--- Query by Age and Genre ---")
print(
    f'Users aged 19 purchased '
    f'{query_age_genre(19, "Rock", all_users, all_albums)} '
    f'rock track(s).')

print("\n--- Query by City and Artist ---")
print(
    f'Users from London purchased '
    f'{query_city_artist("London", "Linkin Park", all_users, all_albums)} '
    f'track(s) by "Linkin Park".')

print("\n--- Query by City and Genre ---")
print(
    f'Users from Toronto purchased '
    f'{query_city_genre("Toronto", "Alternative", all_users, all_albums)} '
    f'alternative track(s).')

print("\n" + "=" * 60)
print("End of demonstration.")
print("=" * 60)