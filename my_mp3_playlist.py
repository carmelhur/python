
def my_mp3_playlist(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    max_duration = 0
    longest_song = ""
    artist_count = {}
    song_count = 0

    for line in lines:
        parts = line.strip().split(";")
        if len(parts) < 3:
            continue
        song_name, artist, duration = parts[0], parts[1], parts[2]
        song_count += 1

        # בדיקת שיר הארוך ביותר
        minutes, seconds = map(int, duration.split(":"))
        total_seconds = minutes * 60 + seconds
        if total_seconds > max_duration:
            max_duration = total_seconds
            longest_song = song_name

        # ספירת המבצעים
        artist_count[artist] = artist_count.get(artist, 0) + 1

    # מציאת המבצע המופיע הכי הרבה פעמים
    most_common_artist = max(artist_count, key=artist_count.get)

    return (longest_song, song_count, most_common_artist)
