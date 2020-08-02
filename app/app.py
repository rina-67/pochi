#Flaskとrender_template(htmlを表示させるための関数)をインポート
from flask import Flask,render_template,request

#Flaskオブジェクトの作成
app = Flask(__name__)


@app.route("/")

#「/index」にアクセスがあったときに、index.htmlを返す
@app.route("/index")
def index():
    name = request.args.get("name")
    return render_template("index.html",name=name)


@app.route('/index',methods=["post"])
def post():
    #formタグ内にあるinput要素のvalue値を取得、この場合はtype=nameの値を取得
    name = request.form["name"]
    return render_template("index.html",name=name)


if __name__ == "__main__":
    app.run(debug=True)
