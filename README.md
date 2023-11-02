# ProgSD_TeamProject
UofG ProgSD TeamProject
## Introduction
This project is to create a software system to support an electric vehicle share programme.
We use Python for our implementation, with a user interface written in Tkinter.
Additionally, we set the database which is MySQL on Google Cloud to support our project.
## Environment Preparation 
### Install Anaconda Environment
`conda create -n projectBike python=3.6`

`conda activate projectBike`
### Install packages 
`pip install -r requirements.txt`
### Notice important package
- numpy version > 1.20.0
- tensorflow version > 2.6.0
- when you use MacOS, you might need to install ttk or tkmacos to instead tkinter

`pip install tkmacos`
## Database Preparation
You can download our data and structure to import your local or online service.  

We recommend the following software to load the database：
- Navicat
- Datagrip

## Run
### app.py 
This is the back-end system back-end system integration, which contains a number of test cases and calls to methods in the `__main__` function.  

### run.py 
This is the root file to start the project, run `run.py` to start the project.  

### Notice
- When you run before, please be sure to complete the environment configuration and database configuration has been changed, otherwise you are still running the data used by our project.  

- You have to change the `mysql_config` parameter of the file, usually it is written at the beginning of the file

### Test
Once you have successfully run it, you can register your own account to complete the test

## GUI Desgin
### Prototype
<img src="https://github.com/CreateMiracle0523/ProgSD_TeamProject/blob/0b3ef6f8d683f8b12d549955853bf05104eb9862/Prototype%20drawing/1.png" width="500">  

### Project Showcase
<img src="https://github.com/CreateMiracle0523/ProgSD_TeamProject/blob/1b9b37a80dec7442bf56e390c6e045c1b7f67dec/index.png" width="500">  
