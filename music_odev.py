# Music Playlist Analysis System

# Toplam süre
def get_total_duration(songs):
    return sum(s["sure"] for s in songs)

# En çok dinlenen
def get_most_played_song(songs):
    return max(songs, key=lambda x: x["dinlenme"])

# Ortalama süre
def get_average_duration(songs):
    return get_total_duration(songs) / len(songs)

# Playlist yazdır
def print_playlist(songs):
    print("\n--- PLAYLIST ---")
    for s in songs:
        print(s["ad"], "-", s["sanatci"], "| Süre:", s["sure"], "| Dinlenme:", s["dinlenme"])

# Bonus: en uzun şarkı
def get_longest_song(songs):
    return max(songs, key=lambda x: x["sure"])

# Bonus: filtreleme
def filter_by_artist(songs, artist):
    return [s for s in songs if s["sanatci"].lower() == artist.lower()]

# Bonus: sıralama
def sort_by_play_count(songs):
    return sorted(songs, key=lambda x: x["dinlenme"], reverse=True)

# main
def main():
    songs = [
        {"ad": "Blinding Lights", "sanatci": "The Weeknd", "sure": 3.5, "dinlenme": 1500},
        {"ad": "Shape of You", "sanatci": "Ed Sheeran", "sure": 4.2, "dinlenme": 2000},
        {"ad": "Levitating", "sanatci": "Dua Lipa", "sure": 3.8, "dinlenme": 1800},
        {"ad": "Peaches", "sanatci": "Justin Bieber", "sure": 3.3, "dinlenme": 1200},
        {"ad": "Senorita", "sanatci": "Shawn Mendes", "sure": 3.9, "dinlenme": 1600}
    ]

    print_playlist(songs)

    print("\nToplam süre:", get_total_duration(songs))
    print("Ortalama süre:", get_average_duration(songs))
    print("En çok dinlenen:", get_most_played_song(songs)["ad"])
    print("En uzun şarkı:", get_longest_song(songs)["ad"])

    print("\nSıralı liste:")
    print_playlist(sort_by_play_count(songs))

    print("\nThe Weeknd şarkıları:")
    print_playlist(filter_by_artist(songs, "The Weeknd"))

main()