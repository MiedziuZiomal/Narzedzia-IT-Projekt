import argparse
import json

def parse_arguments():
    parser = argparse.ArgumentParser(description='Program do konwersji formatów plików.')
    parser.add_argument('input_file', type=str, help='Ścieżka do pliku wejściowego.')
    parser.add_argument('output_file', type=str, help='Ścieżka do pliku wyjściowego.')

    args = parser.parse_args()

    # Rozpoznawanie formatu pliku wejściowego
    input_file_extension = args.input_file.split('.')[-1]
    args.input_file_extension = input_file_extension

    return args


def main():
    args = parse_arguments()
    print('Plik wejściowy:', args.input_file)
    print('Plik wyjściowy:', args.output_file)

    # Wczytywanie pliku JSON
    if args.input_file_extension == 'json':
        data = load_json_file(args.input_file)
        print(data)  # Wydrukowanie wczytanych danych

if __name__ == '__main__':
    main()

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
