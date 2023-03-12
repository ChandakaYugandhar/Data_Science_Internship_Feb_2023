# Step 1- Import Flask
from flask import Flask,request

# Step 2 - Create a Object with Parameter __name__
yuggu = Flask(__name__)

# Step 3 - Create an END POINT usingroutes and bind then with a Functionally
@yuggu.route('/')
def home_page():
    return "Welcome to the Home Page"


@yuggu.route('/mul')
def multiplication():
    a=request.args.get('a')
    b=request.args.get('b')
    return "multiplication of "+a+" + "+b+" : "+str(int(a)*int(b))


@yuggu.route('/upper')
def upper_case():
    user_name = request.args.get('user_name')
    return "Upper Case of "+user_name+" : "+user_name.upper()


@yuggu.route('/lower')
def lower_case():
    user_name=request.args.get('user_name')
    return "Lower Case of "+user_name+" : "+user_name.lower()


@yuggu.route('/div')
def division():
    a=request.args.get('a')
    b=request.args.get('b')
    return "Division of "+a+" / "+b+" : "+str (int (a) / int (b))


@yuggu.route('/factorial')
def fact():
    a=request.args.get("a")
    n=int(a)
    sum_=1
    for i in range(1,n+1):
     sum_=sum_*i
    return "Factorial of "+a+"! : "+str(int(sum_))


# Step 5 - Run the Flask
if __name__=='__main__':
    yuggu.run(debug=True)                                                         

