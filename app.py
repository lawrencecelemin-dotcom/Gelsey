import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def valentine():
    answer = None
    if request.method == "POST":
        answer = request.form.get("answer")
    
    # If this line is NOT indented, the site stays white
    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)