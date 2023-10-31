from flask import Flask, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB configuration
client = MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB connection string
db = client["mydatabase"]
collection = db["mycollection"]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form['name']
        email = request.form['email']

        # Store data in MongoDB
        data = {
            'name': name,
            'email': email
        }
        collection.insert_one(data)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
