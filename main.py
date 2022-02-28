from flask import Flask
from flask import url_for

app = Flask(__name__)


@app.route('/')
def nn():
    return 'Миссия Колонизация Марса'
@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"

@app.route('/image_mars')
def image():
    return '''
<!doctype html>
<html lang="ru">
    <head>
        <meta charset="utf-8">
        <title> Привет, Марс!</title>
    </head>
    <body>
        <h1>Жди нас, Марс!</h1>
        <img src="/static/img/mars.png" alt="здесь должна была быть картинка, но не нашлась", width = 400p, height = 400p>
        <p>Вот она какая, красная планета</p>
    </body>
</html>'''

@app.route('/promotion')
def promotion():
    return '''<!doctype html>
                    <html lang="ru">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                        crossorigin="anonymous">
                      </head>
                      <body>
                        <h3>Человечество вырастает из детства.<br></h3>
                        <h3>Человечеству мала одна планета.<br></h3>
                        <h3>Мы сделаем обитаемыми безжизненные пока планеты.<br></h3>
                        <h3>И начнем с Марса!<br></h3>
                        <h3>Присоединяйся!<br></h3>
                      </body>
                    </html>'''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')