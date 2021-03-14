# Rice-Plant-Disease-Detection
Detecting diseases in rice plants and classifying them acoording to it.

## Observations:
  #### Inception V3 model
            Somewhat accurate, healhty correct result, others not accurate
         1).loss: 2.6493 - accuracy: 0.6750, val_loss: 4.2833 - val_accuracy: 0.5081
         2) loss: 2.2479 - accuracy: 0.6431 - val_loss: 3.4463 - val_accuracy: 0.5696       (Increasing datasets and labelled test samples)
         3) loss: 2.7192 - accuracy: 0.6596 - val_loss: 2.2923 - val_accuracy: 0.7119
         4) loss: 1.9514 - accuracy: 0.7247 - val_loss: 4.4615 - val_accuracy: 0.5163       (Epoch increased by 10, Learning rate defined)
         5) loss: 1.6486 - accuracy: 0.7814 - val_loss: 4.9798 - val_accuracy: 0.5346       (Epoch-30,regulizers introduced)
         6) loss: 2.0126 - accuracy: 0.7337 - val_loss: 3.9157 - val_accuracy: 0.5774
         7) loss: 0.0476 - accuracy: 0.9911 - val_loss: 1.8791 - val_accuracy: 0.8250       (Healthy predicted correctly, overfitting)
  #### Resnet50 Model
            Not accurate, wrong results.
         1).loss: 1.4497 - accuracy: 0.4122,val_loss 1.9753 - val_accuracy: 0.2581
         
  #### SVM Technique
           Accurate, correct results.
         1).Prediction score= 0.875
