from flask import Flask, redirect, url_for,request, render_template

app = Flask(__name__)

@app.route('/newmsg/<msg>')
def newmsg(msg):
    return '%s' % str(msg)

@app.route('/input', methods = ['POST', 'GET'])
def myfunc():
    if request.method == 'POST':
        uinput = request.form['uinput']
        global msg
        result =""

        for index, letter in enumerate(uinput):
            if index % 2 == 0:
                result += letter.lower()
            else:
                result += letter.upper()
        msg = result
        return redirect(url_for('newmsg',msg=result))

    else:
        return render_template('convert.html')

if __name__ == '__main__':
    app.run(debug= True, port=5000)