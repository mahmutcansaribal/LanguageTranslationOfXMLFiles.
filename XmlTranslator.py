import xml.etree.ElementTree as ET
from deep_translator import GoogleTranslator


translator = GoogleTranslator(source='en', target='tr')

# XML files read
tree = ET.parse('strings.xml')
root = tree.getroot()


MAX_CHUNK_SIZE = 5000

def translate_text(text):

    chunks = [text[i:i+MAX_CHUNK_SIZE] for i in range(0, len(text), MAX_CHUNK_SIZE)]
    translated_chunks = []
    
    for chunk in chunks:
        try:
            translated_chunk = translator.translate(text=chunk)
            if translated_chunk is not None:
                translated_chunks.append(translated_chunk)
            else:
                translated_chunks.append(chunk)
        except Exception as e:
            print(f"Error: {e}")


    # Çevirilen parçaları birleştirme
    return ''.join(translated_chunks)

# Translate data within tags
for string in root.findall('string'):
    original_text = string.text
    if original_text == None:
        pass  
    else:
        translated_text = translate_text(original_text)
        string.text = translated_text
        print(f"CEVİRİ : {string.text}")

# Saving changes
tree.write('strings_tr.xml', encoding='utf-8', xml_declaration=True)

print("Translation completed and saved in the file 'strings_en.xml' ")
