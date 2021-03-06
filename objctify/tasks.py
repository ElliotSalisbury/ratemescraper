from __future__ import absolute_import

from celery import shared_task

import cv2
import base64
import numpy as np
from PIL import Image
from objctify.models import UploadedImage
from processing.beautify import beautify_image

def base64_to_image(imageb64):
    raw = base64.b64decode(imageb64.split(',')[1].encode('utf-8'))
    image = np.frombuffer(raw, dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image

def upload_to_image(upload):
    image = np.array(Image.open(upload))
    return cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

def ensureImageLessThanMax(im, maxsize=512):
    height, width, depth = im.shape
    if height > maxsize or width > maxsize:
        if width > height:
            ratio = maxsize / float(width)
            width = maxsize
            height = int(height * ratio)
        else:
            ratio = maxsize / float(height)
            height = maxsize
            width = int(width * ratio)
        im = cv2.resize(im,(width,height))
    return im

def image_to_base64(image):
    jpgdata = cv2.imencode('.jpg',image)[1]
    b64 = "data:image/jpeg;base64,"+base64.b64encode(jpgdata).decode('utf-8')
    return b64

@shared_task
def faceBeautificationTask(uploadedIds, gender):
    reply = {}
    reply["images"] = []
    for id in uploadedIds:
        uploadedImage = UploadedImage.objects.get(pk=id)
        image = upload_to_image(uploadedImage.image)
        image = ensureImageLessThanMax(image)
        results, image = beautify_image(image, gender)

        results["processed_image"] = image_to_base64(image)

        reply["images"].append({"name":uploadedImage.filename, "results":results})
    return reply