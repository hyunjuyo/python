import requests
from flask import Flask, render_template, request

base_url = "http://hn.algolia.com/api/v1"

new = f"{base_url}/search_by_date?tags=story"
popular = f"{base_url}/search?tags=story"


def make_detail_url(id):
    return f"{base_url}/items/{id}"


db = {}
app = Flask("DayNine")


@app.route("/")
def index():
    res = request.args.get("order_by")
    if res == "new":
        order_by = "new"
        if db.get("new") == None:
            r = requests.get(new)
            json_data = r.json()
            db["new"] = json_data["hits"]
    else:
        order_by = "popular"
        if db.get("popular") == None:
            r = requests.get(popular)
            json_data = r.json()
            db["popular"] = json_data["hits"]
    return render_template(f"index_{order_by}.html", hits=db[f"{order_by}"])


@app.route("/<id>")
def detail(id):
    detail_url = make_detail_url(id)
    r = requests.get(detail_url)
    json_data = r.json()
    return render_template("detail.html", id=json_data, children=json_data["children"])


app.run(host="0.0.0.0")
