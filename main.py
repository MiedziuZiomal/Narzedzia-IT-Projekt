import yaml

def load_yaml_file(filepath):
    try:
        with open(filepath, 'r') as yaml_file:
            data = yaml.safe_load(yaml_file)
        print("Pomyślnie wczytano plik YAML.")
        return data
    except yaml.YAMLError as e:
        print(f"Błąd: plik YAML jest niepoprawny: {e}")
        return None
    except Exception as e:
        print(f"Błąd: {e}")
        return None
