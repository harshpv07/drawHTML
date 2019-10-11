from flask import Flask,render_template
from modules.html_reader import html_ext
from modules.streamer import capture
from modules.render import render_html

app = Flask(__name__)

@app.route('/json')
def getjson():
    arr = []
    filler_initial = ["<html>","<head>","<title>Sample_program</title>","</head>","<body>"] #initial HTML code
    filler_final  = ["</body>","</html>"]
    j = html_ext() #complete json
    for i in range(0,len(j)):
        arr.append(render_html(j[i]["detectionString"],j[i]["box"][0],j[i]["box"][1],j[i]["box"][2],j[i]["box"][3]))
    return render_template('./hello.html',aray_sent = arr,ini = filler_initial,final = filler_final)


if __name__ == "__main__":
    app.debug = True
    app.run()
    app.run(debug = True)