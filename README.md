# Stage1 - chiptuning app
> Simple chiptuning application created with Python and MongoDB

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)
* [Inspiration](#inspiration)

## General info
This project is simple stage-one chiptuning file generator.
Using the pattern found in the database, the program modifies the original car ecu file in order to obtain a safe power gain.

## Technologies
* Python - version 3.7
* MongoDB - version 4.4

## Setup
You will need Python and the appropriate libraries.
The latest version of Python for your system can be found at:
https://www.python.org/downloads/

Then you will need to install 3 libraries:

- intelhex
- pymongo
- pydns

For Windows, the easiest way is to install using the pip package.
In windows command line use:

pip install library_name

To start using program in Windows go in cmd to the appropriate directory and type the command: 

python main.py

## Features
List of features ready and TODOs for future development
* Tuning of Injections maps
* Tuning of Turbo pressure maps
* Tuning of Rail maps

To-do list:
* Divide the tuning functions into more precise sections
* Add functions to modify the limiters and ignitions
* Add features for file compliance checking
* Add more drivers to database

## Status
Project is: _in progress_

## Inspiration
The project was inspired by a passion for motorization and fast cars