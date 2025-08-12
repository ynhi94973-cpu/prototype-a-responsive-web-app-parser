import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def parser():
    if request.method == 'POST':
        url = request.form['url']
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.find('title').text
            meta_description = soup.find('meta', attrs={'name': 'description'})['content']
            meta_keywords = soup.find('meta', attrs={'name': 'keywords'})['content']
            return render_template('result.html', title=title, meta_description=meta_description, meta_keywords=meta_keywords)
        except Exception as e:
            return 'Error: ' + str(e)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)