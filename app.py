from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")

@app.route("/")
def home():
    return render_template("index.html", prediction=None, error=None)

@app.route("/predict_web", methods=["POST"])
def predict_web():
    try:
        throughput = float(request.form["throughput"])

        prediction = model.predict([[throughput]])

        # Works for both (1,1) and (1,) shaped outputs
        result = round(float(np.array(prediction).flat[0]), 3)
        result = max(0.0, result)   # clamp to non-negative

        return render_template("index.html", prediction=result)
    except Exception as e:
        return render_template("index.html", prediction=None, error=str(e))

if __name__ == "__main__":
    app.run(debug=True, port=5001)