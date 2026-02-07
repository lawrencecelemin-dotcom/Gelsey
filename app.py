import os
from flask import Flask, render_template, request, url_for

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route("/", methods=["GET", "POST"])
def valentine():
    answer = None
    if request.method == "POST":
        answer = request.form.get("answer")
    
    # Always return inside the function
    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    # Use the PORT provided by Render, default to 5000 locally
    port = int(os.environ.get("PORT", 5000))
    # Enable debug locally if needed (optional)
    debug_mode = os.environ.get("DEBUG", "False").lower() == "true"
    app.run(host="0.0.0.0", port=port, debug=debug_mode)