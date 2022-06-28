import csv 

allarticles = []
likedarticles = []
notlikedarticles = []

with open("articles.csv",encoding = "utf-8") as a:
    reader = csv.reader(a)
    data = list(reader)
    allarticles= data[1:]

from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route("/getarticle")
def getarticle():
    
    return jsonify({
        "data":allarticles[0],
        "status":"success"
    })

@app.route("/likedarticle",methods = ["POST"])
def likedarticle():
    movie = allarticles[0]
    likedarticles.append(movie)
    allarticles.pop(0)
    return jsonify({
        "status":"success"
    }),201

@app.route("/unlikedarticle",methods = ["POST"])
def unlikedarticle():
    movie = allarticles[0]
    notlikedarticles.append(movie)
    allarticles.pop(0)
    return jsonify({
        "status":"success"
    }),201


if __name__=="__main__":
    app.run()