# Shared-Global-Calculator
Take Home Test from Sezzle, Inc.

View hosted calculator application at (_https://shared-global-calculator.herokuapp.com/_)

*Please note that this application is using free "[dyno hours](https://devcenter.heroku.com/articles/free-dyno-hours)" provided by Heroku. Therefore, if this calculator application receives no web traffic in a 30-minute period, it will sleep (idle). When sleeping, any user who connects will experience a delayed initial load/start up. In my experience, this delay should not last longer than 8-10 seconds.*

## About

This web application serves as a calculator that logs the 10 most recent calculations with anyone and everyone connected to the website. Each new calculation is logged and presented to connected users in real time using asyncronous i/o and websockets. Each logged calculation presents the user's name (if given), the calculation, and the global time at which the calculation took place (in [Zulu time/GMT](https://zulutime.net)) . Using the Django web framework, this application was deployed to Heroku and uses Heroku Redis to support the use of websockets. 

### Background

This app was created using Django and deployed to Heroku. You may notice the high amount of commits - 122 of them were related to deployment! Since I am new to integrating a Django project to Heroku, it took me a little longer to configure the settings and file structure to meet the requirements of a successful Heroku deployment. A possible solution to the frequent commits would be to perform a ```git rebase``` and ```squash``` the deployment process together. However, I am keeping all commits as they are for the full visibility of my process as you inspect my source code.

### Current Version 1.2
What's New:
```
-Python 3.8.6 support
-Decimal computations are now rounded to the nearest ten-thousandths place
-Routine internal maintenance (including redis-server location updates)
```

### Future Work
There exist redundant files in my file structure. This mostly appeared well after my local app (Django only) worked beautifully on my local machine; folders needed to be moved around for Heroku deployment to be built successfully. In total, the file structure and commit history can be cleaned up, as it does seem a bit messy to me. Alternate date and time formats can be used instead of Zulu time - this can be changed with other future design ideas.

In the meantime, this application should be up and working well. If you have any issues with this application, please contact me [here](https://chris-pieper.bss.design/contact.html). 


### Documentation
For any visitors of this page, I am still new to front-end development even after my computer science degree, which is very deeply concerned with theory, mathematics, and back-end development. I still have much to learn, but that's what is exciting! The major pillars of personal inspiration and instruction behind this application's design/deployment are contained within the following links:

-https://www.fullstackpython.com/django.html
-https://devcenter.heroku.com/articles/deploying-python
-https://devcenter.heroku.com/articles/getting-started-with-python


