import os
from flask import Flask , render_template , request

UPLOAD_FOLDER = "./images"


app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER



@app.route('/',methods=['GET']) 
def hello_world():
    return render_template('main.html')
    #return 'Hello, World!'

@app.route('/',methods=['POST'])
def predict():
    imagefile= request.files['imagefile']
    image_path = os.path.join(app.config["UPLOAD_FOLDER"],imagefile.filename)
    imagefile.save(image_path)

    
    return render_template('main.html') 




if __name__ == "__main__":
     app.run(debug=True) 

