import io, os
from numpy import random
from google.cloud import vision
from pillow_utility import draw_borders, Image
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"abc.json"
client = vision.ImageAnnotatorClient()

import cv2
from PIL import Image

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types



def detect_text(path):
    """Detects text in the file."""
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)
    response = client.object_localization(image=image)
    text = response.localized_object_annotations
    string = ''

    #for texts in text:
        #string+=' ' + texts.name
    return text




cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    file = 'live.png'
    cv2.imwrite( file,frame)

    # print OCR text
    print(detect_text(file))

    # Display the resulting frame
    cv2.imshow('frame',frame)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


pillow_image = Image.open(image_path)
df = pd.DataFrame(columns=['name', 'score'])
for obj in text:
    df = df.append(
        dict(
            name=obj.name,
            score=obj.score
        ),
        ignore_index=True)

    r, g, b = 0, 0, 0

    draw_borders(pillow_image, obj.bounding_poly, (r, g, b),
                 pillow_image.size, obj.name, obj.score)

print(df)
pillow_image.save("abcd.jpg")