[Link to the live project](https://flask-easy-cooking-project.herokuapp.com/)


# Easy Cooking - Third Milestone Project

Easy cooking is an app that allows its users to save, edit and share recipes with other users.


## User Experience (UX)

### Project Goals

The primary Project Goal is to create an online cookbook.

The target audience are people who want to store their recipes online or are just looking for cooking ideas.

### User Stories

*   User stories
    * As a user I want to see recipes from other users to get new cooking ideas.
    * As a user I want to be able to store my recipes online.
    * As a user I want to be able to edit my recipes.


### Design choices


### Wireframes


## Features


## Technologies used

### Languages used

* [HTML5](https://en.wikipedia.org/wiki/HTML5) used to create the structure of the website.
* [CSS3](https://en.wikipedia.org/wiki/CSS) used to style the website
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript) used to add interactivity to the website.
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) used to created logic of the website.
* [Jinja](https://en.wikipedia.org/wiki/Jinja_(template_engine)) used for template inheritance, loops and if statements in the html files.


### Frameworks, Libraries & Programs Used

* [Google Developer Tools](https://developer.chrome.com/docs/devtools/) was used for testing responsiveness of the website.

* [Git](https://git-scm.com/) was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

* [GitHub](https://github.com/) is used to store the projects code after being pushed from Git.

* [jQuery](https://jquery.com/) required for the Materialize JavaScript components to function.

* Flask web framework 

* [Materialize](https://materializecss.com/getting-started.html)


## Testing

* Navigation and other internal links were tested to confirm that User is directed to the relevent pages when any of the links is clicked.

* Confirmed that a new User can successfully register, Flash message is displayed confirming the sucessfull registration and a new record is created in the database.

* Confirmed that an existing User can successfully log in to application by clicking on the login button after inputting credentials into username and password fields.

* Confirmed that a User can fill out the "Add Recipe" form and submit data inputs. Validated that a new records is successfully inserted to database

* Confirmed that a User can upload and image file

* Confirmed that if no image is provided by User then a default image is displayed.

        
* Known Bugs

    * Images uploaded by Users are not rendered from MongoDB


## Deployment

### Heroku

The project was deployed to Heroku using the following steps:

1. Log in to Heroku
1. Click New in the top right corner and select "Create a New App"
1. Gave the app a name and select the closest region, then click 'Create App
1. Setup Automatic Deployment from GitHub repository:
    1. Go to "Deploy" tab and scroll to the “Deployment method” section
    1. Click on "GitHub"
    1. Ensure the correct GitHub profile is displayed
    1. Locate the [GitHub Repository](https://github.com/ip69719/ms_project_3) then click "Connect"
    1. Go to "Settings" tab, then click on "Reveal Config Vars"
    1. Configure variables for IP, PORT, SECRET_KEY and MONGO_URI and MONGO_DBNAME
    1. Go back to the "Deploy" tab, scroll down to "Automatic deploys" section and click on "Enable Automatic Deploys"
1. In "Deploy" tab scroll down to "Manual deploy" section, select main branch and click on "Deploy Branch"
1. Click "View" to launch the app.

## Credits

### Content

* Content of READ.md was written with reference to [Example README.md template](https://github.com/Code-Institute-Solutions/SampleREADME).

### Media

* Image was sourced from [Shutterstock](https://www.shutterstock.com/home)

### Code

* * Used Code Institute Backend Development Mini Project  tutorial as a reference to implement project idea.

### Acknowledgements

* Special thanks to my Mentor for support and guidance and to Code Institute for exellent leaning materials.