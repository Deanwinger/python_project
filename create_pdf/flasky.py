from io import BytesIO
from flask import Flask, make_response, send_file
import base64


app = Flask(__name__)

@app.route('/', methods=['GET'])
def upload_pdf():
    response = make_response(send_file('D:\python-related\create_pdf\phello.pdf'))
    response.headers["Content-Disposition"] = "attachment; filename=alan.pdf"
    response.headers["Content-Type"] = "application/pdf"
    return response

if __name__ == '__main__':
    app.run(debug=True)