import csv

def process_csv_files(csv_files):
    user_ids = {}

    # Leer y procesar cada archivo CSV
    for filename in csv_files:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                user_id_ascii = sum(ord(c) for c in row['User_ID'])
                user_ids[user_id_ascii] = row['User_name']

    # Imprimir los IDs de usuario convertidos a ASCII
    for user_id_ascii, user_name in user_ids.items():
        print(f"User name: {user_name}, User ID (ASCII): {user_id_ascii}")


csv_files = ["./csv/User_track_data.csv", "./csv/User_track_data_2.csv", "./csv/User_track_data_3.csv"]
process_csv_files(csv_files)
