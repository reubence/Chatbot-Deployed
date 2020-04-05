import chatgui
from flask import Flask, request


app = Flask(__name__)

@app.route("/analyze", methods=['POST'])
def analyze():
    some_json=request.get_json()
   
    text = some_json['text']  
    response = chatgui.chatbot_response(text)
    return str(response)

if __name__=='__main__':
    app.run(debug=True)