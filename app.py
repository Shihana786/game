from flask import Flask,request,render_template
import random
app=Flask(__name__)
choices=["Stone!","Paper!","Scrissor!"]
@app.route("/",methods=["POST","GET"])
def index():
    if request.method=="POST": 
        my_choices=request.form.get("choice")
        computer_choices=random.choice(choices)
        if my_choices==computer_choices:
            result="It is tie"
        elif (my_choices=="Stone!"and computer_choices=="Scrissor!")or\
             (my_choices=="Paper!" and computer_choices=="Stone!")or\
             (my_choices=="Scrissor!" and computer_choices=="Paper!"):
            result="you won"
        else:
           result="computer won"
        return render_template("home.html",my_choices=my_choices,computer_choices=computer_choices,result=result)
    return render_template("home.html",my_choices=None, computer_choices=None, result=None)
if __name__=="__main__":
    app.run(debug=True)

    
     
