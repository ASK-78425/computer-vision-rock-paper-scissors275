#%% 
# Imports
import cv2
from keras.models import load_model
import numpy as np
import time
import math

#%%
# Create countdown function
# Set parameters:
def countdown_from_three():
   '''Sets a countdown from 3 seconds'''
   start_time = time.time()
   counter_cft = 0
   while True:
      if math.floor(time.time()) - math.floor(start_time) == 1 and counter_cft == 0:
         print("3")
         counter_cft += 1
      elif math.floor(time.time()) - math.floor(start_time) == 2 and counter_cft == 1:
         print("2")
         counter_cft +=1
      elif math.floor(time.time()) - math.floor(start_time) == 3 and counter_cft == 2:
         print("1")
         counter_cft += 1
      elif math.floor(time.time()) - math.floor(start_time) == 4 and counter_cft == 3:
         print("Show choice!")
         counter_cft += 1
      else:
         if counter_cft == 4:
            break

# %%
# create function get_prediction
def get_prediction():
  model = load_model('keras_model.h5')
  cap = cv2.VideoCapture(0)
  data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
  counter = 0
  while counter < 1:
    countdown_from_three()
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    counter += 1

  # After the loop release the cap object
  cap.release()
  # Destroy all the windows
  cv2.destroyAllWindows()
  prediction_list = prediction.tolist()
  prediction_list_values = prediction_list[0]
  highest_conf_prediction = max(prediction_list_values)
  key_index = prediction_list_values.index(highest_conf_prediction)
  if key_index == 0:
     print("You chose Rock")
  elif key_index == 1:
     print("You chose Paper")
  elif key_index == 2:
     print("You chose Scissors")
  else:
     print("Nothing, try again!")
     get_prediction()
  return key_index

# %%
