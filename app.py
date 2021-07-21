from flask import Flask
import numpy as np
import pickle
from flask import request, render_template


app = Flask(__name__)
model = pickle.load(open('GBR.pkl', 'rb'))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/y_predict', methods=['POST'])
def y_predict():
    cement = request.form["a"]
    slag = request.form["b"]
    ash = request.form["c"]
    water = request.form["d"]
    superplastic = request.form["e"]
    coarseagg = request.form["f"]
    fineagg = request.form["g"]
    age = request.form["h"]

    Input = np.array(
        [[cement, slag, ash, water, superplastic, coarseagg, fineagg, age]])
    output = model.predict(Input)
    return render_template("index.html",  Predcited_Output=f'The Compressive Strength of Concrete is :{output}')


if __name__ == "__main__":
    app.run(debug=True)
