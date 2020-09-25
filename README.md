# Shared-Global-Calculator
Take Home Test from Sezzle, Inc.

View hosted calculator application at (_https://shared-global-calculator.herokuapp.com/_)


## About

This web application serves as a calculator that logs the 10 most recent calculations with anyone and everyone connected to the website. Each new calculation is logged and presented to connected users in real time using asyncronous i/o and websockets. Each logged calculation presents the user's name (if given), the calculation, and the global time at which the calculation took place. Using the Django web framework, this application was deployed to Heroku and uses Heroku Redis to support the use of websockets. 

### Background

This app was created using Django and deployed to Heroku. You may notice the high amount of commits - 122 of them were related to deployment! Since I am new to integrating a Django project to Heroku, it took me a little longer to configure the settings and file structure to meet the requirements of a successful Heroku deployment. A possible solution to the frequent commits would be to perform a ```git rebase``` and ```squash``` the deployment process together. However, I am keeping all commits as they are for the full visibility of my process as you inspect my source code. 

### Future Work
There exist redundant files in my file structure. This mostly appeared well after my local app (Django only) worked beautifully on my local machine; folders needed to be moved around for Heroku deployment to be built successfully. In total, the file structure and commit history can be cleaned up, as it does seem a bit messy to me.

In the meantime, this application is up and working well - Thank you for this opportunity! 
