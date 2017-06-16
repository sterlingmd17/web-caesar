from flask import Flask, request
from caesar import rotate_string

app= Flask(__name__)
app.config['DEBUG']=True
form="""
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form action='/' method='post' name='caesar'>
      <div>
        <label>Rotate by: 
        <input type='text' name='rot' value='0'/>
        </label>
    </div>
        <textarea name='text' value=>{0}
        </textarea>
        <input type='submit' value='submit'/>
      </form>
    </body>
</html
"""
@app.route("/", methods=['POST'])
def encrypt():
    rot= int(request.form['rot'])
    text= request.form['text']
    rotated= str(rotate_string(text,rot))
    return "<h1>"+ form.format(rotated)+ "</h1>"
    
    

@app.route("/")
def index():
    return form.format('')

app.run()