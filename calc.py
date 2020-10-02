from flask import Flask, render_template, request

app = Flask(__name__)
# app.config.from_object(__name__)

@app.route('/')
def welcome():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def result():
    var_1 = request.form.get("var_1", type=int, default=0)
    var_2 = request.form.get("var_2", type=int, default=0)
    operation = request.form.get("operation")
    if(operation == 'Addition'):
        result = var_1 + var_2
    elif(operation == 'Subtraction'):
        result = var_1 - var_2
    elif(operation == 'Multiplication'):
        result = var_1 * var_2
    elif(operation == 'Division'):
    	if(var_1==0 and var_2==0):
    		result = 0
    	else:
        	result = var_1 / var_2
    else:
        result = 0
    entry = result
    return render_template('form.html', entry=entry)

if __name__ == '__main__':
    app.run(debug=True)
