
# For creating the web application.
import flask as fl
# For generating random numbers.
import numpy as np

# Create the web application.
app = fl.Flask(__name__)

# Add a route for the web page.
@app.route('/')
def home():
  return app.send_static_file('canvashtml.html')