database-sraping
================

Gather the database information using django and sqlalchemy.

Why database-scraping ?

 - Used to scrap the database information.
 - Store Database inforamation in local database.
 - Connect the database remotely.

    - Connection for mysql:
        - You provide remote mysql Privileges to run server Ip
        - Comment the bind-address in my.conf. Path [cd /etc/mysql]
        - Then restart the remote mysql server.
    - Connection for sqlite:
        - You need to browse sqlite db file.

 - You view the database tables, Table columns and Table records.

Installation:

 - pin install -r requirements.txt

Run server:

 - python manage.py runserver
