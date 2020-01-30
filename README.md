# Freds Recipes
 I have used many different technologies to create an online recipe website.
 The website allows users to view, edit, delete and create recipes.
 
### UX
The target audience of this website is for anyone who is looking to cook a meal
but is not too sure on what recipe to make. This site is very good
for these type of users as they will have a wide range of recipes to select from.
The user will have full access to all the ingredients, instructions and an image
so that they know exactly what to and what the recipe is meant to look like.
If the user decides that they would like to change something about the recipe, they would 
be able to do so as the website does allow each recipe to be edited.

###Features
Add a recipe - This can be done by clicking on the "Add Recipe"
option on the navbar.

Edit a Recipe - This can be done by clicking on a recipe of the users choice and clicking on the 
"EDIT" button on the bottom right. After this, the site will redirect the user to
a page which has a form on there with all the information pre-filled. The user 
will be able to change any information on any of the input boxes. 
Once this has been done, the "Update" button will need to be clicked on.
This will redirect the site to the Edited recipe. 

Delete a Recipe - This can be done by clicking on a recipe of the users choice and clicking on the 
"DELETE" button on the bottom right.

View a recipe - This can be done through the user going to the recipes page
by clicking on "recipes". Once the recipes page has loaded, a recipe 
will need to be chosen by clicking on the "CHECK ME OUT!" button. The recipe will then load.

###### Features to be implemented
1. A search bar to allow users to search for recipes.
2. Allow each user to have their own personal accounts.

### Technologies used
* HTML
* CSS
* Bootstrap
* Python
* MongoDB

### Testing 

I have done many different tests on the site to make sure that it is fully
functioning. 

###### Adding a new recipe:
I have tested this by clicking on the "Add Recipe" option on the navbar and then filled it out.
Afterwards, I have checked on the recipes page to make sure that it is added.

###### Deleting a recipe:
I have checked this by clicking on the "DELETE" button on a recipe and seeing if
it is still part of the recipes on the recipes page.

###### Editing a recipe:
I have checked this by clicking on the "EDIT" button and changing some of the
information on the input boxes. Afterward, I clicked on "UPDATE" and checked to see
if the information I put in had been changed or not.

###### Viewing a recipe:
I have checked this by clicking on one of the recipes on the recipes page and making
sure that all the information is on there.

###### Seeing if the navbar collapses on smaller screens:
I checked this through google chrome developer tools.

I have also made sure that the website works on different browsers such as Microsoft Edge,
Firefox, and Google Chrome.

Furthermore, I have also tried my site on different screen sizes via the developer
tools on Google Chrome.

### Deployment

I started of deploying my site on Heroku by commiting everything to my repositary :

1. git init 
2. git add .
3. git commit -m "Initial commit"

One I commited everything I had to download the Heroku CLI so that I could type in to 
my terminal "heroku login". This prompted me to login to my Heroku account with my username
and password. Then I put in the following things in to my terminal:

1. heroku git:clone -a recipewebsite123
2. git push heroku master

I then realised, that I would need a requirements.txt and Profile so I created them through the following:

1. pip freeze --local > requirements.txt
2. echo web: python run.py > Procfile

Once I had done the above, I pushed my file to heroku again through "git push heroku master".
The next thing, I did was type in the following code in to my terminal "heroku:ps scale web=1"

The final thing that needed to be done was to set my IP, PORT, MONGO URI and MONGO NAME 
in Heroku. I did this in the settings options. The link to my website:
https://recipewebsite123.herokuapp.com/


### Credits

###### Content

I got the content and images of the recipes from BBC Good Food.

###### Acknowledgement

I took inspiration for this website from BBC Good Food.









