from flask import Flask, render_template, request, redirect
from scraper_sof import get_job_infos

app = Flask("Goodscraper")

db = {}


@app.route("/")
def home():
    return render_template("front.html")


@app.route("/report")
def a():
    word = request.args.get("word")
    if word:
        word = word.lower()
        get_word = db.get(word)
        if get_word:
            jobs = get_word
            print("wow~!!!")
        else:
            jobs = get_job_infos(word)
            db[word] = jobs
            print("wow!!")
    else:
        return redirect("/")
    return render_template("search.html",
                           word1=word,
                           jobs_count=len(jobs),
                           jobs=jobs)


app.run(host="0.0.0.0")
