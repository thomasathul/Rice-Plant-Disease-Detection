# Rice-Plant-Disease-Detection

Detecting diseases in rice plants and classifying them according to it.

Trained Classes:- Bacterial leaf blight, Leaf smut, Brown Spot, Healthy



| Model  | Training Accuracy | Validation Accuracy | 
| ------------- | ------------- | ------------|
| Inception V3 model  |  accuracy: 0.9905  |   accuracy : 0.8198     | 
| MobileNetV2 |   accuracy: 0.9500    | accuracy: 0.8125   |
| NasNetMobile | accuracy : 0.9320        | accuracy: 0.8044     |
| SVM Technique |     accuracy : 0.85            |       |
| K Nearest Neighbors |  accuracy: 0.62      |        |
| Decision Tree |     accuracy :  0.54         |          |







## Observations:
 
Decision  Tree and KNN needs to be improved

While running the API, you may have to wait for a few seconds at first to load all the models. 





## Steps to run the program:

```
1. Download / Clone this repository
```
```
2. Make sure you have installed the necessary libraries given in requirements.txt
```

```
3. Open your terminal and change your directory to the cloned repository
   > cd Documents/GitHub/Rice-Plant-Disease-Detection
```

```
4. Run the app.py in your command terminal
   > python app.py
```

```
5. Open the app locally in your web broswer
```





## Possible Errors

* (OSError: SavedModel not found at ".....)

  Please check your savedmodel file and check whether ince_model.h5 is a pointer file ( i.e 1kb file). If yes, please go to the savedmodel file in my github repo and manually download the ince_model.h5 (108mb file)
  
* Please do check whether the file path's in the app.py file is changed to your local paths. Else it would throw an error.

* Install the necessary libraries required to run the app to avoid any other possible errors.
