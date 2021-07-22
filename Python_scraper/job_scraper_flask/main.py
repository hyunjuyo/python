from flask import Flask, render_template, request, redirect, send_file
from scraper_sof import get_job_infos
from exporter import save_jobs

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


@app.route("/export")
def export_to_csv():
    try:
        word = request.args.get("word")
        if word == None:
            raise Exception
        else:
            word = word.lower()
            jobs = db.get(word)
            if jobs == None:
                raise Exception
        save_jobs(word, jobs)
        return send_file(f"jobs_{word}.csv")
    except:
        return redirect("/")


app.run(host="0.0.0.0")
