# API Yatube

Empower connection, inspire interaction.

## Description

Enhance your application's social engagement with our robust API, designed for seamless integration and powerful functionality. Create and manage posts, foster interactive discussions through comments, and build a dynamic community by following your favorite authors. Our API provides all the tools you need to deliver an engaging user experience with ease and efficiency.

## Getting Started

### List of used technologies

* `Python`
* `Django REST Framework`
* `Django ORM`
* `SQLite`

### Dependencies

You can find all used packages in `requirements.txt` file.

### Installation

Use the following commands in your terminal to prepare your project for local lauch and modification.

* Creating local copy of the project
```
git clone https://github.com/ArtemMaksimov-trial/api_final_yatube.git
```
* Creating virtual environment from the root folder `.../api_final_yatube`
```
python -m venv venv
```
* Activating a virtual environment
```
source venv/Scripts/activate
```
* Setting up of the required dependencies
```
pip install -r requirements.txt
```
* Switching to an internal folder `.../api_final_yatube/yatube_api`
```
cd yatube_api
```
* Applying of necessary migrations
```
python manage.py migrate
```
* Creating superuser
```
python manage.py createsuperuser
```
* Running of the local server
```
python manage.py runserver
```

Now you are ready to use our API through any of web or desktop platform for your choice!

## Contact

Artem Maksimov - [@ovienrait](https://t.me/ovienrait) - [nirendsound@gmail.com](https://nirendsound@gmail.com)

Project Link: [API Yatube](https://github.com/ArtemMaksimov-trial/api_final_yatube.git)