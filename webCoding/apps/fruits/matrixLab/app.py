from flask import Flask, render_template, request
import numpy as np
from matrixMath.qi.bytes.qubit.gate import isUnitary
from matrixMath.qi.bytes.qubit.qubity import eigens2
app = Flask(__name__)

#######################################


# define the architecture
@app.route("/")
def home():
    return render_template("home.html")

########################################

#calc

@app.route("/calc", methods=['POST'])
# define send message
def calc():

    if request.method == 'POST':
        num1 = request.form['num1']
        # separate and convert numbers to floats
        num1 = [float(i) for i in num1.split()]
        array1 = np.array([num1])
        array1 = array1.reshape(2, 2)
        operation = request.form['operation']
        if operation == 'unitarity':
            unitary = isUnitary(array1)
            print(unitary)
            return render_template('home.html', sum=unitary)
        elif operation == 'eigenvalue':
            eigen = eigens2(array1)
            print(eigen)
            return render_template('home.html', sum=eigen)


###################################################

@app.route("/adinkra")
# test channel
def adinkra():
    return render_template('adinkra.html')



######################################

if __name__ == "__main__":
    app.run(debug=True)