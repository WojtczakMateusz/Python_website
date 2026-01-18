from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
from PIL import Image

app = Flask(__name__)

model_simple = tf.keras.models.load_model("models/simple_cnn.h5")
model_advanced = tf.keras.models.load_model("models/advanced_cnn.h5")

def prepare_image(image):
    image = image.convert("L").resize((28,28))
    img = np.array(image) / 255.0
    img = img.reshape(1,28,28,1)
    return img

@app.route("/", methods=["GET", "POST"])
def index():
    result_simple = None
    result_advanced = None

    if request.method == "POST":
        file = request.files["image"]
        image = Image.open(file)

        img = prepare_image(image)

        pred1 = model_simple.predict(img)
        pred2 = model_advanced.predict(img)

        result_simple = np.argmax(pred1)
        result_advanced = np.argmax(pred2)

    return render_template(
        "index.html",
        simple=result_simple,
        advanced=result_advanced
    )

if __name__ == "__main__":
    app.run(debug=True)