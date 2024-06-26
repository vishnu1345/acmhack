from flask import Flask, request, jsonify, session
from flask_bcrypt import Bcrypt
from flask_cors import CORS, cross_origin 
from models import Provider, User,Location
from models import db
app = Flask(__name__)
app.config['SECRET_KEY'] = 'BinaryPhantoms'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345@localhost/userlog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
 
bcrypt = Bcrypt(app) 
CORS(app, supports_credentials=True)
db.init_app(app)
  
with app.app_context():
    db.create_all()
 
@app.route("/")
def hello_world():
    return "Hello, World!"
 
@app.route("/signup", methods=["POST"])
def signup():
    email = request.json["email"]
    password = request.json["password"]
 
    user_exists = User.query.filter_by(email=email).first() is not None
 
    if user_exists:
        return jsonify({"error": "Email already exists"}), 409
     
    hashed_password = bcrypt.generate_password_hash(password)
    new_user = User(email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
 
    session["user_id"] = new_user.id
 
    return jsonify({
        "id": new_user.id,
        "email": new_user.email
    })
 
@app.route("/login", methods=["POST"])
def login_user():
    email = request.json["email"]
    password = request.json["password"]
  
    user = User.query.filter_by(email=email).first()
  
    if user is None:
        return jsonify({"error": "Unauthorized Access"}), 401
  
    if not bcrypt.check_password_hash(user.password, password):
        return jsonify({"error": "Unauthorized"}), 401
      
    session["user_id"] = user.id
  
    return jsonify({
        "id": user.id,
        "email": user.email
    })

@app.route("/foodform", methods=["POST"])
def foodform():
    Name = request.json["name"]
    Phone = request.json["phoneno"]
    Food = request.json["food"]
    Address=request.json["address"]
    

    new_donor = Provider(name=Name,phoneno=Phone,address=Address,food=Food)
    db.session.add(new_donor)
    db.session.commit()
  
    return jsonify({
        "name": new_donor.name,
        "phone": new_donor.phoneno,
        "food": new_donor.food,
        "address": new_donor.address,
       
    })
 
@app.route("/foodform", methods=["GET"])
def get_food():
    food = Provider.query.all()
    food_list = [{'name': user.name, 'phone':user.phoneno, "food": user.food,"address": user.address,} for user in food]
    return jsonify(food_list)



@app.route("/location",methods=["POST"])
def locationn():
    Latitude=request.json["latitude"]
    Longitude=request.json["longitude"]
    newloc = Location(latitude=Latitude,longitude=Longitude)
    db.session.add(newloc)
    db.session.commit()
    return jsonify({
        "latitude": newloc.latitude,
        "longitude": newloc.longitude

    })
@app.route("/location", methods=["GET"])
def loc_get():
    loca = Location.query.all()
    loca_list = [{'latitude':loc.latitude,"longitude":loc.longitude} for loc in loca]
    return jsonify(loca_list)


if __name__ == "__main__":
    app.run(debug=True)