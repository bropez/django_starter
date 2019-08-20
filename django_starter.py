import subprocess
import webbrowser


def django_setup(name):
    # create the conda environment for the django app
    # the environment will have the same name as the app
    # install django
    subprocess.run('conda create --name {} -y'.format(name))
    subprocess.run('conda activate {} && conda install pip -y && pip install django'.format(name), shell=True)

    # create the django app in the current directory
    subprocess.run('django-admin startproject {}'.format(name), shell=True)


def start_server(name):
    # go into the django app directory and start the server
    subprocess.run('python ./{}/manage.py runserver'.format(name))


# TODO: maybe make this work through another command prompt that opens
# def open_server():
#     # open up a window linked to localhost
#     webbrowser.open_new('http://127.0.0.1:8000/')



if __name__ == '__main__':
    name = input("Name of your django project: ")
    django_setup(name)
    start_server(name)
    # open_server()
