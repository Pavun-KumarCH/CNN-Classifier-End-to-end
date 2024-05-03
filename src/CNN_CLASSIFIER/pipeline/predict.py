import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class DogCat:
    def __init__(self, filename):
        self.filename = filename

    def predictiondogcat(self):
        #load model
        #model = load_model(os.path.join("model","model_vgg16.h5"))
        model = load_model(os.path.join("artifacts","training","model.h5"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224,224))
        #test_image = image.load_img(imagename, target_size = (64,64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = np.argmax(model.predict(test_image), axis = 1)
        print(result)

        #training_set.class_indices
        if result[0] == 1:
            prediction = 'dog'
            return[{"Image": prediction}]
        else:
            prediction = 'cat'
        return [{"Image": prediction}]