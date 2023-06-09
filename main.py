import json

def load_json_file(filepath):
    try:
        with open(filepath, 'r') as json_file:
            data = json.load(json_file)
        print("Pomyślnie wczytano plik JSON.")
        return data
    except json.JSONDecodeError:
        print("Błąd: plik JSON jest niepoprawny.")
        return None
    except Exception as e:
        print(f"Błąd: {e}")
        return None
