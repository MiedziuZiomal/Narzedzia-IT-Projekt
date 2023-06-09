import argparse
import json
import yaml


def parse_arguments():
    parser = argparse.ArgumentParser(description='Program do konwersji formatów plików.')
    parser.add_argument('input_file', type=str, help='Ścieżka do pliku wejściowego.')
    parser.add_argument('output_file', type=str, help='Ścieżka do pliku wyjściowego.')

    args = parser.parse_args()

    # Rozpoznawanie formatu pliku wejściowego
    input_file_extension = args.input_file.split('.')[-1]
    args.input_file_extension = input_file_extension

    return args

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

def write_to_json_file(filepath, data):
    try:
        with open(filepath, 'w') as json_file:
            json.dump(data, json_file)
        print(f"Pomyślnie zapisano dane do pliku JSON: {filepath}")
    except Exception as e:
        print(f"Błąd podczas zapisywania do pliku JSON: {e}")

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

def write_to_yaml_file(filepath, data):
    try:
        with open(filepath, 'w') as yaml_file:
            yaml.dump(data, yaml_file)
        print(f"Pomyślnie zapisano dane do pliku YAML: {filepath}")
    except Exception as e:
        print(f"Błąd podczas zapisywania do pliku YAML: {e}")

def main():
    args = parse_arguments()
    print('Plik wejściowy:', args.input_file)
    print('Plik wyjściowy:', args.output_file)

    # Wczytywanie pliku JSON
    if args.input_file_extension == 'json':
        data = load_json_file(args.input_file)
        print(data)  # Wydrukowanie wczytanych danych
    elif args.input_file_extension == 'yaml' or args.input_file_extension == 'yml':
        data = load_yaml_file(args.input_file)
        print(data)  # Wydrukowanie wczytanych danych

    # Zapisywanie danych do pliku JSON
    output_file_extension = args.output_file.split
