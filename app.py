from flask import Flask, render_template, request, send_file
from main import resize_image
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/resize', methods=['POST'])
def resize():
    uploaded_file = request.files['Image']
    percentage = int(request.form['percentage'])
    ext = uploaded_file.filename.split(".")[-1]
    resized_image = resize_image(uploaded_file, percentage, ext)
    return send_file(
            resized_image,
            as_attachment=True,
            mimetype=f"image/{ext}"
    )
if __name__ == '__main__':
    app.run(debug=True)