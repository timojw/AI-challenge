from flask import Flask, request, render_template
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get data from form
        age = float(request.form.get('age'))
        bodyweight = float(request.form.get('bodyweight'))
        # sex = request.form.get('sex') # You can include this if needed in your model

        # Dummy model (replace with your actual model)
        # Note: You need to load your trained model here instead of creating a new one
        poly_features = PolynomialFeatures(degree=2)
        model = LinearRegression()
        # Example input, replace with actual model input
        input_data = poly_features.fit_transform(np.array([[age, bodyweight]]))
        
        # Predict 1RM
        prediction = model.predict(input_data)[0]

        return render_template('index.html', prediction=prediction)
    
    return render_template('index.html', prediction=None)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
