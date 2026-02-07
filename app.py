import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def valentine():
    answer = None
    if request.method == "POST":
        # Get the form value when Yes is clicked
        answer = request.form.get("answer")
    
    # This return must be aligned with the 'if' above
    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    # Use the port Render provides, or default to 5000 for local testing
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)