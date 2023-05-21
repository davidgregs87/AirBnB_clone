![image](https://github.com/davidgregs87/AirBnB_clone/assets/108700012/c83b2dab-ce26-4f6b-92fc-d20513970870)


README CLONE AIRBNB
Description
In this project we create the first part of the clone of Arbnb, which one is about to create a console in order to get different commands because we are going to have Objects in our platform as Places, Cities, States, Amenities, Users, and Review based in a parent class called BaseModel. And we have to manage it so that have a interactive web application, that is why we have to create, update, show, count, destroy and print the differents instances that are in our platform.

How to use it
excecution or Start: For excecute the console type:

./console.py

help command: Help command helps you to understand each one of the commands that we create. If you want to know what are all the possible commands you have to type:

help

But if you want to know what is an specific command you have to type:

help command like help quit

create command: If you want to create a new object you have to type:

create <object class>

So the classes that we manage are:

BaseModel
User
Amenity
City
Place
State
Review
So you have to take care of the capital letters when you call the class. Once the object was created it will return the its id number:

all command: With this command you will be able to print all the created objects that exists nowadays, if you want to do that you have to type:

all or .all()

But if you want to print all the objects of a specific class you have to type:

all <class name> like all Userir the second way <class name>.all() like City.all()

count command: With count you can print the number of objects that belong to a specific class so if you want to do it you have to type:
count <class name> like count Place or the second way <class name>.count() like Review.count()

show command: This command prints the string representation of a specific objects. To see the information type: show <class name> <id> ex: show Review 12345or the second way <class name>.show("id") like Review.show("12345").

destroy command: This command deletes a specific objects. To remove the object type: destroy <class name> <id> ex: destroy Review 12345or the second way <class name>.destroy("id") like Review.destroy("12345").

update command: This command updates a specific objects. To update the object type one of these three way to do it:

update <class name> <id> <name> "<value>" ex: update Review 12345 name "Marco"
<class name>.update("id", "<name>", "<value>") ex: City.update("12345", "item", "bed")
<class name>.update("id", {'<name1>: "<value1>", '<name2>': "<value2>"}) ex City.update("12345", {'item1': "bed", 'item2': "bathroom"})
if the attribute of the class exists it will be replace with the new value, otherwise it will create a new attribute for the specified instance.

commands to exit the program if you want to exit the program you should type:

quit or Ctrl+D or EOF
