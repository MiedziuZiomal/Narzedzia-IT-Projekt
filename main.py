import xml.etree.ElementTree as ET

def load_xml_file(filepath):
    try:
        tree = ET.parse(filepath)
        root = tree.getroot()
        print("Pomyślnie wczytano plik XML.")
        return root
    except ET.ParseError:
        print("Błąd: plik XML jest niepoprawny.")
        return None
    except Exception as e:
        print(f"Błąd: {e}")
        return None
