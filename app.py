import pickle
from flask import Flask, request, render_template
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        age = float(request.form.get('age'))
        bodyweight = float(request.form.get('bodyweight'))
        sex = float(request.form.get('sex'))  # Assuming sex is provided as 0 or 1

        # Prepare input data
        poly_features = PolynomialFeatures(degree=2)
        input_data = poly_features.fit_transform(np.array([[age, bodyweight, sex]]))

        # Load models and make predictions
        with open('model_deadlift.pkl', 'rb') as f:
            model_deadlift = pickle.load(f)
        prediction_deadlift = round(model_deadlift.predict(input_data)[0])

        with open('model_squat.pkl', 'rb') as f:
            model_squat = pickle.load(f)
        prediction_squat = round(model_squat.predict(input_data)[0])

        with open('model_bench.pkl', 'rb') as f:
            model_bench = pickle.load(f)
        prediction_bench = round(model_bench.predict(input_data)[0])


        # Return predictions to the template
        return render_template('index.html', prediction_deadlift=prediction_deadlift, 
                               prediction_squat=prediction_squat, prediction_bench=prediction_bench)

    return render_template('index.html', prediction_deadlift=None, prediction_squat=None, prediction_bench=None)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
