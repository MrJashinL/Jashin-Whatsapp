# MetaData Extractor
# Estrae metadati EXIF da immagini e video ricevuti su WhatsApp.
# Crediti: Jashin L.

from PIL import Image
from PIL.ExifTags import TAGS
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
from hachoir.core.tools import makePrintable

def extract_image_metadata(image_path):
    image = Image.open(image_path)
    exif_data = image._getexif()
    if exif_data:
        metadata = {}
        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag)
            metadata[tag_name] = value
        return metadata
    else:
        return "No EXIF metadata found."

def extract_video_metadata(video_path):
    parser = createParser(video_path)
    if not parser:
        return "Unable to parse video file."
    with parser:
        try:
            metadata = extractMetadata(parser)
        except Exception as err:
            return f"Metadata extraction error: {err}"
        if not metadata:
            return "No metadata found."
        return metadata.exportDictionary()

def main():
    file_path = input("Inserisci il percorso del file (immagine o video): ")
    if file_path.lower().endswith(('jpg', 'jpeg', 'png')):
        metadata = extract_image_metadata(file_path)
    elif file_path.lower().endswith(('mp4', 'avi', 'mov', 'mkv')):
        metadata = extract_video_metadata(file_path)
    else:
        print("Formato file non supportato.")
        return

    print("Metadati estratti:")
    print(metadata)

if __name__ == '__main__':
    main()