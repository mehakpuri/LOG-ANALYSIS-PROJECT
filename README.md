# Logs Analysis Project
## by Mehak Puri
This is the third project for the Udacity Full Stack 1 Nanodegree. In this project, a large database with over a million rows is explored by building complex SQL queries. The project builds an internal reporting tool for a newpaper site to discover what kind of articles the site's readers like by interacting on a live database.

## Technologies used In this project
1. PostgreSQL
2. Python3
3. Linux-based virtual machine (VM) Vagrant

## Project Requirements
Reporting tool should answer the following questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

* Project follows good SQL coding practices, i.e each question is answered with a single database query.  
* The code is error free and conforms to the PEP8 style recommendations.
* The code presents its output in clearly formatted plain text.

## System setup and how to view this project

1. Download Vagrant and install.
2. Download Virtual Box and install. 
3. Clone this repository to a directory of your choice.
4. Download the **newsdata.sql** (extract from **newsdata.zip** (not provided here though)) and **newsdata.py** files from the respository and move them to your **vagrant** directory within your VM.

#### Run these commands from the terminal in the folder where your vagrant is installed in: 
1. ```vagrant up``` to start up the VM.
2. ```vagrant ssh``` to log into the VM.
3. ```cd /vagrant``` to change to your vagrant directory.
4. ```psql -d news -f newsdata.sql``` to load the data and create the tables, to run the database and then use necessary commands.
5. ```python finalnews.py``` to execute the program.

The database includes three tables:
- Authors table
- Articles table
- Log table
