from flask import Flask,render_template
app = Flask(__name__,template_folder='templates')
@app.route('/dad')
def showdad():
    return render_template('dad.html')
@app.route('/mom')
def showmom():
    return render_template('mom.html') 
@app.route('/ilyas')
def showilyas():
    return render_template('ilyas.html')       

@app.route('/ehan')
def showehan():
    return render_template('ehan.html')
@app.route('/yusuf')
def showyusuf():
    return render_template('yusuf.html')           
app.run(debug=True)
