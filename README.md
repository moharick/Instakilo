# Instakilo

[![BCH compliance](https://bettercodehub.com/edge/badge/moharick/Instakilo?branch=master)](https://bettercodehub.com/)
## Description
This is a clone of the instagram app

## Author
### [Moharick](https://github.com/moharick)



## Screenshots
<img src="https://github.com/moharick/Instakilo/blob/master/clone/static/images/login%20shot.png" width="1000">
<img src="https://github.com/moharick/Instakilo/blob/master/clone/static/images/reg%20shot.png" width="1000">

## Setup Instructions:
### Requirements

##### 1. Clone the repository
Clone the the repository by running

   ```bash
   git clone https://github.com/moharick/Instakilo.git
   ```
 or download a zip file of the project from github


Navigate to the project directory
```bash
cd Instakilo
```

##### 2. Create a virtual environment
 Install `Virtualenv`

   ```prettier
   pip install virtualenv
   ```

To create a virtual environment named `virtual`, run

   ```prettier
   virtualenv virtual
   ```
To activate the virtual environment we just created, run

   ```bash
   source virtual/bin/activate
   ```

##### 3. Create a database
You'll need to create a new postgress database, Type the following command to access postgress
   ```bash
    $ psql
   ```
   Then run the following query to create a new database named ```gallery```
   ```prettier
   # create database gallery
   ```


#####  4.Install dependencies
To install the requirements from `requirements.txt` file,

   ```prettier
   pip install -r requirements.txt
   ```

#####  5.Create Database migrations
Making migrations on postgres using django

```prettier
python manage.py makemigrations gallery
```


then run the command below;

 ```bash
 python manage.py migrate
 ```

##### 6.Run the app
To run the application on your development machine,

    python3 manage.py runserver

### Running Tests
>To run tests;

    python manage.py test

## Technologies Used
* Django
* Python
* Html
* Css
* Javascript
* Bootstrap


## User stories
As a user of the application I should be able to:

* Sign in to the application to start using.
* Upload my pictures to the application.
* See my profile with all my pictures.
* Follow other users and see their pictures on my timeline.
* Like a picture and leave a comment on it.


## Bugs
There are no known bugs at the moment

## License
[![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](http://opensource.org/licenses/MIT)
>MIT license &copy;  2019 Moharick

## Collaboration Information
* Clone the repository
* Make changes and write tests
* Push changes to github
* Create a pull request

## Contacts
> Send me an [email](moharick@gmail.com) to collaborate on the project.

