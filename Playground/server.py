from flask import Flask, render_template
# , render_template  # Import Flask to allow us to create our app

# Create a new instance of the Flask class called "app"
app = Flask(__name__)

# instructions when opened


@app.route('/')
def start_here():
    return ""
# route created for /play


@app.route('/play')
def index():
    # includes defaults
    return render_template("index.html", x=4, color="aqua")

# route created for /(x)/


@app.route('/play/<int:num>/')
def level_2(num):
    # includes defaults
    return render_template("index.html", x=num, color="aqua")

# route created for /(x)/(color)/


@app.route('/play/<int:num>/<color>/')
def level_3(num, color):
    # includes defaults
    return render_template("index.html", x=num, color=color)


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True, port=5001)
