import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Program do konwersji formatów plików.')
    parser.add_argument('input_file', type=str, help='Ścieżka do pliku wejściowego.')
    parser.add_argument('output_file', type=str, help='Ścieżka do pliku wyjściowego.')

    args = parser.parse_args()
    return args

def main():
    args = parse_arguments()
    print('Plik wejściowy:', args.input_file)
    print('Plik wyjściowy:', args.output_file)

if __name__ == '__main__':
    main()
