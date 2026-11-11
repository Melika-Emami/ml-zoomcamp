import pickle

from flask import Flask, jsonify, request

app = Flask("predict")

input_file = "./models/model_C=1.0.bin"
with open(input_file, "rb") as f:
    (dv, model) = pickle.load(f)


@app.route("/predict", methods=["POST"])
def predict():
    customer = request.get_json()

    customer = dv.transform(customer)
    y_pred = model.predict_proba(customer)[:, -1]
    y_pred = float(y_pred[0])
    decision = y_pred >= 0.5

    result = {"conversion_prob": float(y_pred), "Converted": bool(decision)}
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)
