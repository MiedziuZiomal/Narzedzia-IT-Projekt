import json
def write_to_json_file(filepath, data):
    try:
        with open(filepath, 'w') as json_file:
            json.dump(data, json_file)
        print(f"Pomyślnie zapisano dane do pliku JSON: {filepath}")
    except Exception as e:
        print(f"Błąd podczas zapisywania do pliku JSON: {e}")
