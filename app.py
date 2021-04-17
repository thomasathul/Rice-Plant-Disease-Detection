from flask import Flask
from flask import request
from flask import render_template
import keras
import os
import cv2
import numpy as np


app=Flask(__name__)
UPLOAD_FOLDER = "C:/Users/Dell/Documents/ricedisease/static"



def predict(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (224, 224) )
    img = img /255
    img=np.asarray([img])
    p = MODEL.predict(img)
    p2= MODEL2.predict(img)
    p3=MODEL3.predict(img)
    diseases = ["Healthy", "Bacterial Leaf Blight", "Brown Spot", "Leaf Smut"]
    #diseases = ["Leaf Smut", "Brown Spot", "Leaf Blast","Healthy", "Bacterial Leaf Blight"]
    accu1=np.max(p)
    accu2=np.max(p2)
    accu3=np.max(p3)
    if (accu1>accu2) and (accu1>accu3) :
        class_idx = np.argmax(p)
    elif (accu2 > accu1) and (accu2 > accu3):
        class_idx = np.argmax(p2)
    elif (accu3>accu1) and (accu3>accu1):
        class_idx=np.argmax(p3)    
    a = int(class_idx)
    return diseases[a],diseases[np.argmax(p)],diseases[np.argmax(p2)],diseases[np.argmax(p3)],accu1,accu2,accu3



@app.route("/",methods=["GET", "POST"])
def upload_predict():
    if request.method=="POST":
        image_file=request.files["image"]
        if image_file:
            image_location=os.path.join(
                UPLOAD_FOLDER, image_file.filename
                )
            image_file.save(image_location)
            predict_value,iv,mv,nv,accu1,accu2,accu3=predict(image_location)
            return render_template("index.html", prediction=predict_value, image_loc=image_file.filename,incepval=iv,mobilval=mv,nasval=nv,incecon=round(accu1*100,2),mobilcon=round(accu2*100,2),nascon=round(accu3*100,2))
    return render_template("index.html", prediction=" ", image_loc=None,incepval=None,mobilval=None,nasval=None,incepcon=None,mobilcon=None,nascon=None)

if __name__ == "__main__":
    MODEL = keras.models.load_model("C:/Users/Dell/Documents/ricedisease/savedmodel/ince_model.h5")
    MODEL2 = keras.models.load_model("C:/Users/Dell/Documents/ricedisease/savedmodel/mobile_model.h5")
    MODEL3 = keras.models.load_model("C:/Users/Dell/Documents/ricedisease/savedmodel/nasnet_model.h5")
    app.run(port=8080,debug=True)    
