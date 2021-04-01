# React-Django-Tutorial
Following https://youtu.be/JD-age0BPVo playlist


# Tutorial One Commands
* Make folder called "React-Django-Tutorial"
* Install Python
* Install Prettier, Python, Django, React, JavaScript, and Kite extensions (not mentioned in tutorial, but noticed Tim used Kite) from VS Code.
* Type `pip` or `pip3` (depends on OS) on command line and see if it works out.
* `django-admin startapp frontend`
* `pip install django djangorestframework`
* `django-admin startproject music_controller`
 * `cd music_controller`
 * `django-admin startapp api`
 * In `INSTALLED_APPS` in `music_controller/settings.py`, add:
 * `'api.apps.ApiConfig'`
 * `'rest_framework'`
 * In `api` directory, create a `urls.py` to navigate the remaining URL (that were cut off in 

# Tutorial One Notes
* In Django, you have a project folder. We have apps within a single project.
* Don't worry about `migrations` folder in `api` folder
* In a Django app directory, that is where we have endpoints (e.g. domain.com/hi, domain.com/hello, etc.) be navigated to frontend view functions from `views.py`. A method has a `request` parameter.
 
 ## Changes to databases
 * `python manage.py makemigrations`
 * `python manage.py migrate`
 
 # How to Run
 `python manage.py runserver`
 

# File/Directory Structure
| File/Directory | Description |
| -- | -- |
| [api](music_controller/api) |  Our database/model (class implementation in Django)/REST API.| 
| [frontend](music_controller/frontend) | React frontend to visually display our music controller app.|
| [music_controller/music_controller](music_controller/music_controller) | Administers app as a whole (e.g. we include `INSTALLED_APPS` in [settings.py](music_controller/music_controller/settings.py))|
