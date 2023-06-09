def write_to_xml_file(filepath, data):
    try:
        tree = ET.ElementTree(data)
        with open(filepath, 'wb') as xml_file:
            tree.write(xml_file)
        print(f"Pomyślnie zapisano dane do pliku XML: {filepath}")
    except Exception as e:
        print(f"Błąd podczas zapisywania do pliku XML: {e}")
