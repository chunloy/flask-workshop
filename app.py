from flask import Flask, render_template, request
import requests, json

app = Flask(__name__)

isTrue = True


@app.get("/")
def index():
    return f"{__name__}"


@app.get("/string")
def render_string():
    return f"<h1>{__name__}</h1>"


@app.get("/html")
def render_html():
    return render_template("example.html", name=__name__, boolean=isTrue)


@app.get("/api")
def api():
    try:
        data = requests.get("https://api.kanye.rest")
        return data.json(), 200

    except requests.exceptions.RequestException as e:
        return f"Error while attempting to fetch data: {e}", 500


@app.get("/artists")
def get_artists():
    data = file_reader()
    return json.loads(data)


@app.post("/artists")
def post_data():
    response = request.get_json()
    data = file_reader()

    # convert data to python object for appending response
    data_list = json.loads(data)
    data_list.append(response)
    return data_list, 201


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


@app.route("/artists/<int:id>")
def get_artist(id):
    data_list = json.loads(file_reader())
    return data_list[id]


@app.errorhandler(404)
def handle_404(error):
    return f"Put a custom error message here: {error}", 404


# helper function
def file_reader():
    data = None

    with open("MOCK_DATA.json", "r") as mock_data:
        data = mock_data.read()

    return data
