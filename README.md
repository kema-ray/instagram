# Instagram

#### Author: [Rachel Oyondi](https://github.com/kema-ray)


* Link to live site: [Instagram](https://keminstagram.herokuapp.com/)

## Description
This is an application that works like instagram. It allows a user to sign up,login,add a new post,comment,like,follow and unfollow a particular user. It also shows the time a particuler post was posted.
   |
## User Stories
As a user I would like to:

* Sign in to the application to be able to use it.
* Upload my photos to the application.
* See my profile with all my pictures.
* Follow other users and see there pictures on my timeline.
* Like a picture and leave a comment on it.


## Specifications

| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| Login	if already have an account |if you dont have , click on the sign up link and fill the form  | If login is successful, user is navigated to home page | Click on `Comment` | Taken to where you can comment | Signs In/ Signs Up |
| Edit profile | On the account link, click on the  update profile | Redirected to the home page |
| Click on profile | Redirects to the profile page | User adds bio and profile picture |
|Comment and like on a post|Click on the comment and like icon and add a comment and like|The comment and like will be added to the post's
|Add a new post|Click on the New Profile icon to be redirected to the new post form|the post will be rendered to the home page
| Click on log Out in the accounts| Redirects to the login form | Logs out user  |

## Setup and installations
* Fork the data onto your own personal repository.
* Clone Project to your machine
* Activate a virtual environment on terminal: `source virtual/bin/activate`
* Install all the requirements found in requirements file.
* On your terminal run `python3.8 manage.py runserver`
* Access the live site using the local host provided



## Getting started

### Prerequisites
* python3.8
* virtual environment
* pip

#### Clone the Repo and rename it.
```bash
git clone https://github.com/kema-ray/instagram.git
#### Initialize git and add the remote repository
```bash
git init
```
```git
git remote add origin <your-repository-url>
```

#### Create and activate the virtual environment
```git
python3.8 -m virtualenv virtual
```

```git
source virtual/bin/activate
```

#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Make and run migrations

* python3.8 manage.py check
* python manage.py makemigrations insta
* python3.8 manage.py sqlmigrate insta 0001
* python3.8 manage.py migrate


#### Run the app

python3.8 manage.py runserver


## Testing the Application
`python manage.py test insta`
        
## Built With

* Python3.8
* Django 4.0.5
* Postgresql 
* Boostrap
* HTML
* CSS


## Support and contact details
 Incase you come across errors, have questions, ideas ,concerns, or want to contribute to the application, feel free to reach me at :rachelkemuma99@gmail.com

### License

MIT License

Copyright (c) 2022 Rachel Oyondi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.