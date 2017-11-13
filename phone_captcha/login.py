# 基于 flask + LeanCloud 的短信验证
from flask import *
from func import sms

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def do_login():
    error_msg = None
    if request.method == "GET":
        phone_numbers = request.args.get("mobile_phone_number")
        if phone_numbers is not None:
            if sms.send_message(phone_numbers):
                return render_template('login.html')
            else:
                error_msg = 'Failed to get the verification code!'
    elif request.method == "POST":
        phone_numbers = request.form["phone"]
        code = request.form["code"]
        if code == '':
            error_msg = 'Please input the verification code!'
        elif sms.verify(phone_numbers, code):
            return redirect(url_for("success"))
        else:
            error_msg = 'Your code is wrong, please check again!'
    return render_template('login.html', error_msg=error_msg)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
