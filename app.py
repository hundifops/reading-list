from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

reading_list = []

@app.route('/')
def index():
    return render_template('index.html', reading_list=reading_list)

@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    status = request.form['status']
    reading_list.append({
        'title': title,
        'author': author,
        'genre': genre,
        'status': status
    })
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)