
# For creating the web application.
import flask as fl
# For generating random numbers.
import numpy as np
import base64
import keras as kr
# PIL Python Image Library
from PIL import Image, ImageOps
#conda install opencv (OpenCV is a library of programming functions mainly aimed at real-time computer vision)
import cv2
# Create the web application.

# Loading the nueral network
model = kr.models.load_model('my_model.h5')
#https://github.com/keras-team/keras/issues/6462
model._make_predict_function()


app = fl.Flask(__name__)

# Add a route for the web page.
@app.route('/')
def home():
  return app.send_static_file('canvashtml.html')
  
#Good source used https://machinelearningmastery.com/how-to-develop-a-convolutional-neural-network-from-scratch-for-mnist-handwritten-digit-classification/
# Add a route for predicting the drawing using POST data.
@app.route('/predict', methods=['GET', 'POST'])
def predictionFunct():
  theimage = fl.request.values.get("theimage", "")
  print(theimage)
  #decode the image data in to base64 and then generate image using base 64
  imgdata = base64.b64decode(theimage[22:])
  with open('theimage.png', 'wb') as f:
    f.write(imgdata)
  #open image
  drawnImage = Image.open("theimage.png")
  #generate a resised image
  size = 28, 28
  resizedImage = ImageOps.fit(drawnImage, size, Image.ANTIALIAS)
  resizedImage.save("resized.png")
  # Convert to greyscale
  cv2Image = cv2.imread("resized.png")
  grayScaleImage = cv2.cvtColor(cv2Image, cv2.COLOR_BGR2GRAY)
  grayScaleArray = np.array(grayScaleImage, dtype=np.float32).reshape(1, 784)
  grayScaleArray = grayScaleArray / 255
  #predict
  prediction = model.predict(grayScaleArray)
  predictedNumber = np.array(prediction[0])
  
  print(predictedNumber)

  return predictedNumber

