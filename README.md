# Dagoy - Content Sharing Platform (API)

Dagoy is a content platform for users to share their content. The concept is that you cannot follow any users, to keep content democracy on a high level and nobody gets to ride on the "high follower number bluff = quality".. What you can do on Dagoy is bookmark posts, filter them by category and also like posts if you appreciate a users content. 

Each user has access to their own profile once they are signed in where they can create posts, see all their bookmarks, edit their profile image and password.

If anyone needs to get in touch with the admin, they can fill out the contact form and the Admin will haveget in touch as soon as possible.

* Deployed FrontEnd - [Dagoy](https://dagoy-pp5.herokuapp.com/)

* Deployed BackEnd API - [Dagoy DRF API](https://pp5-api-bo.herokuapp.com/)

* BackEnd Repo - [LINK](https://github.com/Bo-Lennart/DRF-PP5-API)

* FrontEnd Repo - [LINK](https://github.com/Bo-Lennart/pp5-content-platform)

## Table of Contents

- [User Stories](#user-stories)
- [Database Schema](#database-schema)
- [Testing](#Testing)
    - [Validators](#validators)
    - [Bugs](#bugs)
- [Technologies used](#technologies-used)
    - [Modules](#modules)
    - [Languages](#languages)
    - [Libraries, Frameworks & Programs](#libraries-frameworks-&-programs)
- [Deployment](#deployment)
    - [JSON Webtokens](#json-webtokens)
    - [Prepare API for deployment](#prepare-api-for-deployment)
    - [Deploy to Heroku](#deploy-to-heroku)
    - [dj-rest-auth Bug fixes](#dj-rest-aith-bug-fixes)
- [Credits](#credits)
    - [content](#content)
    - [Media](#media)

# User Stories

All user stories can be accessed via the KanBan alike board from the "projects tab" on github.
* Front-End: [LINK](https://github.com/users/Bo-Lennart/projects/10)

Within the readme documentation of the Front-end you can have an insight of a detailed view of the agile methodology of this project. [LINK](https://github.com/Bo-Lennart/pp5-content-platform)

* Back-End: [LINK](https://github.com/users/Bo-Lennart/projects/8/views/1)

# Database Schema

# Testing

## Validators

## Bugs

# Technologies Used

## Modules

## Languages
* Python

## Libraries, Frameworks & Programs
* Django
* DRF (Django Rest Framework)
* Django Rest Auth
* PostgreSQL
* Cors Headers
* Cloudinary
* Pillow

# Deployment
1. Create GitHub Repository
2. Create a new app on Heroku
3. Via the resources tab on heroku, add postgres.
4. Start GitPod and install the packages you desire. For me I ran the following via the "pip install" command: 

![requirements.txt file](assets/screenshots/pip_packages.png)

5. Create django project, command:
- 'django-admin startproject project_name .'
6. Go back to Heroku and navigate to the "settings tab" -> Add the following config vars:
    * Key: SECRET_KEY - hidden
    * Key: CLOUDINARY_URL - Value: cloudinary://hidden
    * Key: DISABLE_COLLECTSTATIC - Value: 1
    * ALLOWED_HOST - API-app-name.heroku.com
7. Once you've set up the React app, go ahead and add the following config vars to the API heroku settings tab:
    * Key: CLIENT_ORIGIN - Value: HTTPS adress to your deployed react heroku page.
    * Key: CLIENT_ORIGIN_DEV - Value: The HTTPS adress to your local server when you preview your React app in the dev environment.
8. Create the env.py file and add the following variables to it:

![envpy file](assets/screenshots/envpy_file.png)

9. Make sure that all you packages are added inside the settinig.py file at the INSTALLED_APPS section. See the screen shot below:

![installed app in settings file](assets/screenshots/installed_apps_settings.png)

10. Import database to settings.py file and the env.py file when working in DEV environment.

![import_database](assets/screenshots/import_database_and_env.png)

11. Set cloudinary storage and add the following variable into the statement.

![Storage settings](assets/screenshots/cloudinary_storage_settings.png)

12. Below the INSTALLED_APPS section, set the "site ID": ![set Id](assets/screenshots/site_id.png)

13. Right below BASE_DIR, create the REST_FRAMEWORK and add the page pagination to improve the app loading efficency, pagination count and time/date format.

![set pagination](assets/screenshots/pagination.png)

14. Set render default to JSON

![jsom render](assets/screenshots/json_render.png)

15. Beneath the REST_FRAMEWORK section, add the following code:

![set jwt auth](assets/screenshots/set_jwt_auth.png)

## JSON Webtokens

## Prepare API for deployment

## Deploy API to Heroku

## dj-rest-auth bug fixes

# Credits

## Content
## Media