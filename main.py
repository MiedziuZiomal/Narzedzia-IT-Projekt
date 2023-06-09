import yaml

def write_to_yaml_file(filepath, data):
    try:
        with open(filepath, 'w') as yaml_file:
            yaml.dump(data, yaml_file)
        print(f"Pomyślnie zapisano dane do pliku YAML: {filepath}")
    except Exception as e:
        print(f"Błąd podczas zapisywania do pliku YAML: {e}")
