from flask import Flask, make_response, send_file



app = Flask(__name__)

@app.route('/', methods=['GET'])
def upload_pdf():
    response = make_response(send_file('/home/ubuntu/alan/python_related/create_pdf/phello.pdf'))
    response.headers["Content-Disposition"] = "attachment; filename=protocol.pdf"
    response.headers["Content-Type"] = "application/pdf"
    return response

if __name__ == '__main__':
    app.run(debug=True)