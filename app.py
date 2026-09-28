from flask import Flask, render_template, request
import joblib
import os

# ================= FLASK APP =================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

# ================= LOAD MODEL =================

model_path = os.path.join(BASE_DIR, "crop_model.pkl")
model = joblib.load(model_path)

accuracy = 99.55


# ================= NORMALIZE GRAPH VALUES =================

def graph_percentage(value, maximum):

    percentage = (value / maximum) * 100

    # Keep graph between 0 and 100
    percentage = max(0, min(100, percentage))

    return round(percentage, 2)


# ================= HOME / PREDICTION =================

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    input_values = None
    graph_values = None

    if request.method == "POST":

        # Get values from HTML form
        N = float(request.form["N"])
        P = float(request.form["P"])
        K = float(request.form["K"])
        temperature = float(request.form["temperature"])
        humidity = float(request.form["humidity"])
        ph = float(request.form["ph"])
        rainfall = float(request.form["rainfall"])

        # Prepare input for ML model
        input_data = [[
            N,
            P,
            K,
            temperature,
            humidity,
            ph,
            rainfall
        ]]

        # Predict crop
        prediction = model.predict(input_data)[0]
        prediction = prediction.capitalize()

        # Actual values
        input_values = {
            "Nitrogen": N,
            "Phosphorus": P,
            "Potassium": K,
            "Temperature": temperature,
            "Humidity": humidity,
            "Soil pH": ph,
            "Rainfall": rainfall
        }

        # Normalized values for graph
        graph_values = {
            "Nitrogen": graph_percentage(N, 140),
            "Phosphorus": graph_percentage(P, 145),
            "Potassium": graph_percentage(K, 205),
            "Temperature": graph_percentage(temperature, 45),
            "Humidity": graph_percentage(humidity, 100),
            "Soil pH": graph_percentage(ph, 10),
            "Rainfall": graph_percentage(rainfall, 300)
        }

    return render_template(
        "index.html",
        prediction=prediction,
        accuracy=accuracy,
        input_values=input_values,
        graph_values=graph_values
    )


# ================= RUN APPLICATION =================

if __name__ == "__main__":
    app.run(debug=True)