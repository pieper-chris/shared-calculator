# Shared-Global-Calculator
Take Home Test from Sezzle, Inc.

**View hosted calculator application at (_https://shared-global-calculator.herokuapp.com/_)**

Please note the following:

*-This application is using free "[dyno hours](https://devcenter.heroku.com/articles/free-dyno-hours)" provided by Heroku. Therefore, if this calculator application receives no web traffic in a 30-minute period, it will sleep (idle). When sleeping, any user who connects will experience a delayed initial load/start up. In my experience, this delay should not last longer than 8-10 seconds.*

*-The internal redis connection may update automatically by Heroku-Redis. When this occurs, the list of "Recent Global Calculations" below the calculator may not load properly or be visible. This is easily fixed after I update the application's settings to match the new Heroku-Redis update. I will do my best to monitor these updates, but cannot guarantee that these fixes will be applied immediately due to the unknown timing of these automatic updates.*


## About

This web application serves as a calculator that logs the 10 most recent calculations with anyone and everyone connected to the website. Each new calculation is logged and presented to connected users in real time using asynchronous i/o and WebSockets. Each logged calculation presents the user's name (if given), the calculation, and the global time at which the calculation took place (in [Zulu time/GMT](https://zulutime.net)) . Using the Django web framework, this application was deployed to Heroku and uses Heroku Redis to support the use of WebSockets.


![Error Loading Gif](https://github.com/pieper-chris/shared-calculator/blob/master/gifs/calc.gif)

### Background

You may notice the high amount of commits - 122 of them were related to deployment! Since I am new to integrating a Django project to Heroku, it took me a little longer to configure the settings and file structure to meet the requirements of a successful Heroku deployment. A possible solution to the frequent commits would be to perform a ```git rebase``` and ```squash``` the deployment process together. However, I am keeping all commits as they are for the full visibility of my process as you inspect my source code.

### Current Version 1.3.1
What's New:
```
-Resolved bootstrap.min.css SourceMap Error [solution was addressed in link below]
```
Link: [Issue related to comment in bootstrap.min.css file](https://github.com/pkp/healthSciences/issues/117)

New in previous version 1.3
```
-Routine internal maintenance (including Redis-server location updates). With this version, all future redis_url updates should be corrected automatically.
-Security Patches: Addressed previous vulnerabilities using the wonderful "django-environ" package.
-Python 3.9.1 support: Upgraded from 3.8.6 to 3.9.1 for deployment and macOS Big Sur development support.
```
See more on [django-environ](https://django-environ.readthedocs.io/en/latest/).

New in previous version 1.2.2
```
-Routine internal maintenance (including redis-server location updates).
```
New in previous version 1.2.1
```
-Added error handling for undefined user input.
```
New in previous version 1.2
```
-Python 3.8.6 support.
-Decimal computations are now rounded to the nearest ten-thousandths place.
-Routine internal maintenance (including redis-server location updates).
```

### Future Work
There exist redundant files in my file structure. This mostly appeared well after my local app (Django only) worked beautifully on my local machine; folders needed to be moved around for Heroku deployment to be built successfully. In total, the file structure and commit history can be cleaned up, as it does seem a bit messy to me. Alternate date and time formats can be used instead of Zulu time - this can be changed with other future design ideas.

In the meantime, this application should be up and working well. If you have any issues with this application, please contact me [here](https://clpieper.com/contact.html).


### Documentation
For any visitors of this page, I am still new to front-end development even after my computer science degree, which is very deeply concerned with theory, mathematics, and back-end development. I still have much to learn, but that's what is exciting! The major pillars of personal inspiration and instruction behind this application's design/deployment are contained within the following links:

- https://www.fullstackpython.com/django.html
- https://devcenter.heroku.com/articles/deploying-python
- https://devcenter.heroku.com/articles/getting-started-with-python
