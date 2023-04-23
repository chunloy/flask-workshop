from flask import Flask, render_template, request
import requests, json

# declare app with all the Flask superpowers
# __name__ is an example of dunder method and returns the name of the current module
# in this case it will return 'app' because it gets called in the app.py module
app = Flask(__name__)

# not used for anything other than being rendered in example.html
isTrue = True


# root endpoint used to return the name of the module
@app.get("/")
def index():
    return f"{__name__}"


# example of serving up string with html tags
@app.get("/string")
def render_string():
    return f"<h1>{__name__}</h1>"


# example of rendering an html file
@app.get("/html")
def render_html():
    return render_template("example.html", name=__name__, boolean=isTrue)


# api example
# when making a request, there's a chance something could go wrong
# it's best to add defensive programming to handle errors using try/except blocks
# any errors in the try block will be caught in the except block
# at minimum you should return a message and status code in the except block
# optional: you can include an argument in the except block and include it in the message
@app.get("/api")
def api():
    try:
        # get data from api and return it as json
        data = requests.get("https://api.kanye.rest")
        return data.json(), 200

    except requests.exceptions.RequestException as e:
        return f"Error while attempting to fetch data: {e}", 500


# fetching data from MOCK_DATA.json and return it
@app.get("/artists")
def get_artists():
    # read in data
    data = file_reader()

    # uncomment the line below and observe the difference
    # return data
    return json.loads(data)


# see README for notes on making a post request
@app.post("/artists")
def post_data():
    # parse incoming request data as json
    response = request.get_json()

    # recall that incoming data will not persist because we never wrote to MOCK_DATA.json
    # instead we're returning a copy of the data with incoming data appended

    # convert data to python object e.g., a list, and append incoming data
    data = file_reader()
    data_list = json.loads(data)
    data_list.append(response)

    return data_list, 201


# an example of using the route method insteads of get/post
# if using this version, comment out the other two above
@app.route("/artists", methods=["GET", "POST"])
def artist_list():
    data = file_reader()
    if request.method == "GET":
        return json.loads(data), 200

    if request.method == "POST":
        response = request.get_json()

        # convert data to python object for appending response
        data_list = json.loads(data)
        data_list.append(response)
        return data_list, 201


# example of a get request for a single artist
# note the endpoint structure, we want the id to be an integer for indexing
@app.route("/artists/<int:id>")
def get_artist(id):
    data_list = json.loads(file_reader())
    return data_list[id]


# example of creating a custom error for non-existent endpoints
@app.errorhandler(404)
def handle_404(error):
    return f"Put a custom error message here: {error}", 404


# helper function
# reads data from MOCK_DATA.json and returns it as a string
def file_reader():
    data = None

    with open("MOCK_DATA.json", "r") as mock_data:
        data = mock_data.read()

    return data
