from flask import Flask
from flask import request
from flask import render_template
import keras
import os
import cv2
import numpy as np

app=Flask(__name__)
UPLOAD_FOLDER = "C:/Users/Dell/Documents/ricedisease/static"
MODEL = keras.models.load_model("C:/Users/Dell/Documents/ricedisease/savedmodel/model.h5")


def predict(image_path):
    img = cv2.imread(os.path.join(image_path))
    img = cv2.resize(img, (224, 224))
    img = img / 255
    img=np.asarray([img])
    p = MODEL.predict(img)
    diseases = ["Healthy", "Bacterial Leaf Blight", "Brown Spot", "Leaf Smut"]
    class_idx = np.argmax(p)
    a = int(class_idx)
    return diseases[a]



@app.route("/",methods=["GET", "POST"])
def upload_predict():
    if request.method=="POST":
        image_file=request.files["image"]
        if image_file:
            image_location=os.path.join(
                UPLOAD_FOLDER, image_file.filename
                )
            image_file.save(image_location)
            predict_value=predict(image_location)
            return render_template("index.html", prediction=predict_value, image_loc=image_file.filename)
    return render_template("index.html", prediction=" ", image_loc=None)

if __name__ == "__main__":
    app.run(port=8080,debug=True)    
