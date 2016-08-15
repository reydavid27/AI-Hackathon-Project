import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename

#Initialize the Clafifai application
from clarifai import rest
client_id = "IaO7HzVoy7M1FgkiZ1mNl5KEX4_Z-W0zqmXywoZu"
client_secret = "D1SOC4MQ_UIoMQD1p3KuI-uduZWMQhSBQzAeeplP"
api = rest.ApiClient(client_id=client_id, client_secret=client_secret)

#api.predictConcepts([rest.Image(file_obj=open('upload/evil_robot.jpg'))])

#Initialize the Flask application
app = Flask(__name__)

# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = './upload/'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg'])

def upload_to_clarifai(filename):

    res = api.predictModel(model_id="b564f1f1d08b4bfbbd5aef4747950682",
        objs=[rest.Image(file_obj=open('upload/' + filename, "rb"))])

    for item in res["outputs"]:
        var = item["data"]["tags"][0]["concept"]["id"]
        if var == "funny" or var == "happy":
            return render_template('live.html')
        else:
            return render_template('die.html')


# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

# This route will show a form to perform an AJAX request
# jQuery is loaded to execute the request and update the
# value of the operation
@app.route('/')
def index():
    return render_template('index.html')


# Route that will process the file upload
@app.route('/upload', methods=['POST'])
def upload():
    # Get the name of the uploaded file
    file = request.files['file']
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(file.filename)
        var = upload_to_clarifai(filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        return var


# This route is expecting a parameter containing the name
# of a file. Then it will locate that file on the upload
# directory and show it on the browser, so if the user uploads
# an image, that image is going to be show after the upload
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("5000"),
        debug=True
    )