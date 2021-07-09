# Schedule Manager Server
A Simple work order schedule management application server.  This application utilizes `Django` aplication framework and `MYSQL` database. 

The final application contains additional tables and fields  not specific in the specifications. Please see the `service_manager.sql` in the root folder of the application for the `database schemas`.


## Getting Started
To get the application up and running there are some few things you will need to do. Ensure that you have at least 
``` 
Python 3.8
``` 
installed on your computer.  See the details below for setting up the application using both `Docker` and `Django-admin`


### Docker
To create a docker image of the application using docker compose, do the following from the application root folder:

``` bash
$  docker-compose build
```
After a successful build, from the same terminal run the folowing command to start the developemt server:

``` bash
$  docker-compose up
```
Copy the  development server address `http://0.0.0.0:8000/` from the console and paste.

Open a new browser window and paste. You application should show the default api page with response `API WORKING`. Don't worry. This is the default route. 

### DJANGO ADMIN
While you can run the application by cerating a docker image, you can also run directly via using the Django Admin. To run, from the application root directory, run the following comand: to activate the virtual enviroment

``` bash
$ source/venv/bin/activate

```
Once the virtual enviroment is activated, move to the app direcotry using:

``` bash
$ cd servicemanager

```

It is now time to install the application dependencies defined in the `requirements.txt` file. run the following command to 
install all the required dependencies.

``` bash
$ pip install -r requirements.txt

```

Finally, run the application server with the following commands:
``` bash
$ python manage.py runserver

```


## Local Migrations
You need to connect the django models to an actial database. Create a new  `mysql` database with the name `service_manager`

```
Follow this section only if you are creating a local database for the application. Also remember to update the `DATABASE` settings of the `settings.py` file to reflect this database connection.

```

To migrate models to the database, run the command below:
``` bash
$ python manage.py makemigrations

```
Once completed, tell Django to create this models as database tables.

``` bash
$ python manage.py migrate 

```

## API Connections

The following API are available within the application. Don't forget to use your local development server path 
if you are running application locally.

 ### Service API
 - return the list of available services
 - [link]https://maccabeus.pythonanywhere.com/service 

 ### Employee API
 - return the list of available employees
 - [link]https://maccabeus.pythonanywhere.com/employee 
  
 ### Holiday API
 - return the list of holidays
 - [link]https://maccabeus.pythonanywhere.com/holiday

 ### WorkOrder API
 Handles the creation, search, delete, and update of work order schedules. Please follow link for the list of the required parameters and their types.

 #### WorkOrder Add
 - Adds a new work order
 - [link]https://maccabeus.pythonanywhere.com/workorder

 #### WorkOrder Search
 - Search workorder by user `email` of `service id`.
 - [link]https://maccabeus.pythonanywhere.com/workorder/search

#### WorkOrder Search By Date
 - Search work orders using the `date range` provided. Will also use `service id` if provided.
 - [link]https://maccabeus.pythonanywhere.com/workorder/search/date

#### WorkOrder Delete
 - Delete a work order using the `id` of the request.
 - [link]https://maccabeus.pythonanywhere.com/workorder/delete

## Live Server
Please check out the application [server here](https://maccabeus.pythonanywhere.com/)

