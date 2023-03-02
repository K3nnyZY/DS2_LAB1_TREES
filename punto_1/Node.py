from Read import process_csv_files

csv_files = ["./csv/User_track_data.csv", "./csv/User_track_data_2.csv", "./csv/User_track_data_3.csv"]
user_ids_tree = process_csv_files(csv_files)

# Ejemplo: Buscar un usuario por ID (ASCII)
user_id_ascii = sum(ord(c) for c in "user123")
user_name = user_ids_tree.search(user_id_ascii)
print(f"User name: {user_name}")
