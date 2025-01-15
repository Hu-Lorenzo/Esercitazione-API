from flask import Flask, render_template, redirect, url_for
import requests
app = Flask(__name__)
NASA_API_KEY = 'PUwbKFwdp2CfSoihYYXBB8pJjbO8mMPR8UdcSnSp'

# Route per la home
@app.route('/')
def home():
    return render_template('home.html')

# Route per la pagina NASA
@app.route('/nasa')
def nasa_home():
    response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}')
    data = response.json()  # Converti da JSON a dizionario Python
    return render_template(
        'nasa.html',
        title=data.get("title"),
        description=data.get("explanation"),
        image_url=data.get("url")
    )

# Route per la pagina dei fatti sui gatti
@app.route('/cat')
def cat_home():
    response = requests.get('https://catfact.ninja/fact')  # Richiesta dati
    data = response.json()  # Converti da JSON a dizionario Python
    return render_template('cat_fact.html', fact=data.get("fact"))

# Route per cambiare il fatto sui gatti
@app.route('/cat/change', methods=['POST'])
def cat_change():
    return redirect(url_for('cat_home'))  # Reindirizza alla stessa pagina per aggiornare il fatto

if __name__ == '__main__':
    app.run(debug=True)