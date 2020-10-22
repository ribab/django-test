Look at these files:

[app/views.py](https://github.com/ribab/django-test/blob/main/app/views.py) -- Creates and returns the plotly graph to display

[templates/index.html](https://github.com/ribab/django-test/blob/main/templates/index.html)

[mysite/settings.py](https://github.com/ribab/django-test/blob/main/mysite/settings.py) -- For this, TEMPLATES is what I changed.

[mysite/urls.py](https://github.com/ribab/django-test/blob/main/mysite/urls.py) -- just pointing to app/urls.py

[app/urls.py](https://github.com/ribab/django-test/blob/main/app/urls.py) -- defines the one test page, using the function I made called "index()" to return the web page to display.

