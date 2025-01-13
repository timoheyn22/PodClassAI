from flask import Flask, render_template

# Flask-Instanz erstellen und den Pfad für Templates anpassen
app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    # Rendert die Datei home.html aus dem Ordner templates
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5005)
