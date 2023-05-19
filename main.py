from flask import Flask , make_response ,jsonify , url_for ,request
import urllib.request

app = Flask(__name__)
# Setting up static file
@app.post("/checkimages")
def index():
    try:
        requestData=request.json
        imgUrl = "httsssps://yt3.googleusercontent.com/6WbGn3t5KILO2FaA6fmhNVBH1PRqL1jTbsNmftSl5GAGM6yX0iSTGbuAU8wRtZuERCF-LRhFLQ=s900-c-k-c0x00ffffff-no-rj"
        urllib.request.urlretrieve(imgUrl, "targetiamge.jpg")
        return make_response({"message":"successfully saved image","url":"url"} ,200)
    except Exception as e:
        print(e)
        return make_response({"message":"failed to save image" } ,500)
# Some Simple Work
# 1.saves images through the given link name=user_id
if __name__ == "__main__":
    app.run(debug=True)