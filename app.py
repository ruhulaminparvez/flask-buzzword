from flask import Flask, render_template


app = Flask(__name__)

all_posts = [

    {
        'title': 'Post 1',
        'content': 'This is the first post',
        'author': 'John Doe',
        'date_posted': 'April 20, 2018'
    },
    {
        'title': 'Post 2',
        'content': 'This is the second post',
        'author': 'Owali',
        'date_posted': 'April 21, 2021'
    },
    {
        'title': 'Post 3',
        'content': 'This is the third post',
        'author': 'Ruhul',
        'date_posted': 'April 1, 2008'
    },
    {
        'title': 'Post 4',
        'content': 'This is the fourth post',
        'date_posted': 'April 20, 2018'
    }

]


@app.route('/', methods=['GET'])
@app.route('/<int:id>', methods=['GET']) 
def index(id):
    return 'Hello, ' + str(id) + ' !'


@app.route('/home', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/posts', methods=['GET'])
def posts():
    return render_template('posts.html', posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)