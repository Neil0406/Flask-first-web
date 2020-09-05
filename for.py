from flask import Flask, render_template

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():
   dataList = ["最近真忙","不過終於國慶連假了","希望天氣好"]
   return render_template('for.html',data=dataList) #將dataList傳給data屬性
 
if __name__== "__main__":
    app.run(debug=True)