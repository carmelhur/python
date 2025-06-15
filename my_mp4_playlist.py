
def my_mp4_playlist(file_path, new_song):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    while len(lines) < 3:
        lines.append(";;0:00;
")

    parts = lines[2].strip().split(";")
    if len(parts) < 3:
        parts = ["", "Unknown", "0:00"]
    parts[0] = new_song
    lines[2] = ";".join(parts) + ";
"

    with open(file_path, 'w') as f:
        f.writelines(lines)

    with open(file_path, 'r') as f:
        print(f.read())
