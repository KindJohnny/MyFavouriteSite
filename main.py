# This is a sample Python script.
import bottle
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from bottle import route, get, post, request, run, template, Bottle, url
from bottle import static_file

# bottle.debug(False)

app = Bottle()


@app.route("/")
def html_index():
    return template("index", url=url)


@app.route('/hello/<name>')
def greet(name='Stranger'):
    return template('<b>Hello {{name}}</b>! How are you?', name=name)


@app.route('/goodbye')
def goodbye():
    return "Bye,Bye Johhny!"


@app.route('/wiki/<pagename>')
def show(pagename):
    return template("<b>Hello,Wiki!\t\t\tPagename:{{pagename}}</b>", pagename=pagename)


# @app.route('/static/<path:path>')
# def callback(path):
#     return path


# @app.route('/<action>/<user>')
# def user(action="action", user='John Snow'):
#     return template("{{action}} : {{user}};", action=action, user=user)


@app.get('/login')
def login():
    return '''
    <form action="/login" method=post>
    Username:<input name="username" type="text"/>
    Password:<input name="password" type="password"/>
    <input value= "Login" type="submit"/>
    
    </form>
    '''


def check_login(user, passwd):
    if user == 'Ado' and passwd == "johnny":
        return True
    return False


@app.post('/login')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Correct</p>"
    else:
        return "<p>Failed!</p>"


@app.get('/upload')
def upload():
    return '''
    <form action = "/upload" method="post" enctype="multipart/form-data">
    Category <input type ="text" name = "category">
    Select a file: <input type ="file" name = "upload">
    <input type ="submit" value = "start upload">
    </form>
    '''


@app.route('/upload', method='POST')
def do_upload():
    upload = request.files.get('upload', '')
    if not upload.filename.lower().endswith(('.jpg', '.jpeg')):
        return 'File ext not allowed!'
    save_path = get_save_path()
    upload.save(save_path)
    return 'Upload OK.Filepath:%s%s' % (save_path, upload.filename)


def get_save_path():
    path_dir = './static/'
    return path_dir


@app.route("/static/<filepath>", name='static_file')
def static(filepath):
    if "sun" in filepath:
        return static_file("SeaSunset.jpg", root="./static/")
    else:
        return static_file(filepath, root="./static/")

    # < img src = "/home/fedor/bottle/static/SeaSunset.jpg" alt = "" >
    # return static_file(filename, root='/home/fedor/bottle/static', mimetype='image/jpeg')


# import mimetypes
# print(mimetypes.guess_type("/home/fedor/bottle/static/SeaSunset.jpg")[0])

if __name__ == '__main__':
    run(app, host='localhost', port=8080)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
