<h1 align="center">Django Class Based Views RestFramework (ViewSet) Todo App</h1>
<h3 align="center">A simple todo app project with class based views restframework with ViewSet classess for learning</h3>
<p align="center">
<a href="https://www.python.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a>
<a href="https://www.djangoproject.com/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/django/django-original.svg" alt="django" width="40" height="40"/> </a>
<a href="https://www.django-rest-framework.org/" target="_blank"> <img src="https://www.django-rest-framework.org/img/logo.png" alt="sqlite" width="90" height="40"/> </a>
<a href="https://getbootstrap.com" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a>
<a href="https://www.w3.org/html/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank">
</a>
<a href="https://www.sqlite.org/" target="_blank"> <img src="https://www.vectorlogo.zone/logos/sqlite/sqlite-icon.svg" alt="sqlite" width="40" height="40"/> </a>

</p>



### Overview
- [Overview](#overview)
- [Demo](#demo)
- [Features](#features)
- [Setup](#setup)
- [Getting ready](#getting-ready)
- [options](#options)
- [Reformat and check](#reformat-and-check)
- [Database schema](#database-schema)
- [Todo](#todo)
- [Bugs or Opinion](#bugs-or-opinion)

### Demo
This is a brief demo of the functionality of the project
<p align="center">
<img src="https://user-images.githubusercontent.com/29748439/135094064-c0b90164-d601-41b2-83cc-614d622daf77.gif" alt="database schema" width="720"/>
</p>

### Features
- Django LTS
- Class Based View
- Django RestFramework
- ViewSet 
- User authentication
- Black
- Flake8
- Responsive Design
- Bootstrap5



### Setup
To get this repository, run the following command inside your git enabled terminal
```bash
git clone https://github.com/alibigdeli/Django-CBV-DRF-ViewSet-TodoApp
```

### Getting ready
Create an enviroment in order to keep the repo dependencies seperated from your local machine.
```bash
python -m venv venv
```

Make sure to install the dependencies of the project through the requirements.txt file.
```bash
pip install -r requirements.txt
```

Once you have installed django and other packages, go to the cloned repo directory and run the following command

```bash
python manage.py makemigrations
```

This will create all the migrations file (database migrations) required to run this App.

Now, to apply this migrations run the following command
```bash
python manage.py migrate
```

### options
Project it self has the user creation form but still in order to use the admin you need to create a super user.you can use the createsuperuser option to make a super user.
```bash
python manage.py createsuperuser
```

And lastly let's make the App run. We just need to start the server now and then we can start using our simple todo App. Start the server by following command

```bash
python manage.py runserver
```

Once the server is up and running, head over to http://127.0.0.1:8000 for the App.

### Reformat and check
If you want your code to be check by pep8 and all the guide lines, there are two packages added to requirements in order to check and reformat code.
you can use it by this command:
```bash
black -l 79 . && flake8
```
### Database schema
A simple view of the project model schema.
<p align="center">
<img src="https://user-images.githubusercontent.com/29748439/134964183-595bd7cf-df01-4089-8d22-bfb765d62c18.png" alt="database schema" width="300"/>
</p>

### Todo
- [ ] refactor accounts view classes
- [ ] refactor javascript codes in list.html
- [ ] leave comments for codes
- [ ] add unit tests
- [ ] add heroku config files
- [ ] complete the documentation
- [ ] create a video tutorial

### Bugs or Opinion
Feel free to let me know if there are any problems or any request you have for this repo.
