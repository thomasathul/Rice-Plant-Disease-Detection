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
    img = cv2.resize(img, (224, 224),  interpolation=cv2.INTER_AREA)
    img = img /255
    img=np.asarray([img])
    p = MODEL.predict(img)
    p2= MODEL2.predict(img)
    p3=MODEL3.predict(img)
    diseases = ["Healthy", "Bacterial Leaf Blight", "Brown Spot", "Leaf Smut"]
    accu1=round(np.max(p)*100,2)
    accu2=round(np.max(p2)*100,2)
    accu3=round(np.max(p3)*100,2)
    totaccu=accu1+accu2+accu3
    healthaccu=0
    blightaccu=0
    brownaccu=0
    smutaccu=0
    list=[p,p2,p3]
    for i in list:
        if diseases[np.argmax(i)] =="Healthy":
            healthaccu += round(np.max(i)*100, 2)
        elif diseases[np.argmax(i)] == "Bacterial Leaf Blight":
            blightaccu += round(np.max(i)*100, 2)
        elif diseases[np.argmax(i)] == "Brown Spot":
            brownaccu += round(np.max(i)*100, 2)
        elif diseases[np.argmax(i)] == "Leaf Smut":
            smutaccu += round(np.max(i)*100, 2) 
    healthaccu=round((healthaccu/totaccu)*100,2)
    blightaccu = round((blightaccu/totaccu)*100,2)
    brownaccu =round((brownaccu/totaccu)*100,2)
    smutaccu = round((smutaccu/totaccu)*100,2)
    if healthaccu>blightaccu and healthaccu>brownaccu and healthaccu>smutaccu:
        class_idx=0  
    elif blightaccu > healthaccu and blightaccu > brownaccu and blightaccu > smutaccu:
        class_idx=1
    elif brownaccu > healthaccu and brownaccu > blightaccu and brownaccu > smutaccu:
        class_idx = 2
    elif smutaccu > healthaccu and smutaccu > blightaccu and smutaccu > brownaccu:
        class_idx = 3   
    a = int(class_idx)
    return diseases[a], healthaccu, blightaccu, brownaccu, smutaccu



@app.route("/",methods=["GET", "POST"])
def upload_predict():
    if request.method=="POST":
        image_file=request.files["image"]
        if image_file:
            image_location=os.path.join(
                UPLOAD_FOLDER, image_file.filename
                )
            image_file.save(image_location)
            predict_value, accu1, accu2, accu3,accu4 = predict(image_location)
         
            return render_template("index.html", prediction=predict_value, image_loc=image_file.filename, health=accu1, blight=accu2, spot=accu3, smut=accu4)
    return render_template("index.html", prediction=" ", image_loc=None, health=None,blight=None,spot=None,smut=None)

 

if __name__ == "__main__":
    MODEL = keras.models.load_model("C:/Users/Dell/Documents/ricedisease/savedmodel/ince_model.h5")
    MODEL2 = keras.models.load_model("C:/Users/Dell/Documents/ricedisease/savedmodel/mobile_model.h5")
    MODEL3 = keras.models.load_model("C:/Users/Dell/Documents/ricedisease/savedmodel/nasnet_model.h5")
    app.run(port=8080,debug=True)    

