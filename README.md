# Password manager implemented with 3DES, Flask and SQLite
### Author:
Tim Givois <tim.givois.mendez@gmail.com>
### Idea
Using a 3DES cipher, we created a password manager that lets you modify, delete and create triplets of password, username and platform. This info is stored in SQLite. Passwords are encrypted with 3DES. Keys are important for encrypting/decrypting the information, a general key is recommended but not enforced.
### How to use
1. Clone this repository:
```
git clone https://github.com/timgivois/password_manager
```
2. Create and activate virtualenv for its dependencies:
```
virtualenv venv
source venv/bin/activate
```
3. Install python dependencies
```
pip install -r requirements.txt
```
4. Create a data directory and running the migrations:
```
mkdir data
python manage.py db migrate
python manage.py db upgrade
```
5. Finally, we can run the app with the following command:
```
export FLASK_APP=app.py
python -m flask run
```
