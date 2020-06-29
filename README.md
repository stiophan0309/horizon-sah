[![Build Status](https://travis-ci.org/stiophan0309/horizon-sah.svg?branch=master)](https://travis-ci.org/stiophan0309/horizon-sah)
# Horzon.        
### Artisan Landscape Art and Photography

# Contents:
#### User Experience
#### Design
#### Wireframes & Flowcharts
#### Features
#### Technologies Used


# User Experience

### Project Goals

The aim of this project is to promote the clients work as an artist and photographer. The project will showcase their work as well as offereing a bespoke commission service where the user can 
request a specific work within the remit of the artist.  Users can create an account, add items to their cart and make payments ahd have their orders available to view in their Profile page.  Non-registered users can browse the gallery/shop and contact the site administrator.

### Target Audience Goals

* To introduce and promote the work of the artist
* To promote the commission service and encourage users to register
* An easy to use layout and design that works on any device
* To be able to communicate with the artist
* Be able to browse the artworks, and make Purchases
* Registered users should be able to view their profile and order history

### Client/Site Owner Goals

* Promote the work of the artist
* Generate business via comissions
* Communicate and get feedback from users
* Get inspiration from users for projects for sale

### User Stories

As a user I want to be able to navigate the site easily and be able to view the artist's work and be enticed to purchase or commission a work.  I want to be able to easily contact the 
artist and be able to get information about the service provided.

As a user I want to be able to find out information about the artist and their influences and what inspires them and their work.

As a user I want to be able to use the site whether on a mobile, tablet or desktop.

As the artist and site owner I want to encourage users to browse my work and be inspired to purchase or commission a work.

As the artist and site owner I want users to be able to easily contact me and obtain information about me and my work and feel they can ask me anything.

### User Expectations and Requirements

In today's world, users should have the confidence to shop online to shop securely and comfortably with a easy to use interface.  A simple easy use UX experience plus a secure 
payment gateway (Stripe) is the ideal solution.

### Requirements

* Interactive and helpful design
* Use the site on any device
* Learn and be able to contact the site owner and artist
* Browse the gallery/shop and be able to add products to the cart and proceed and make payment securely
* View orders and profile information
* Contact the site owner and artist with any query/information

### Expectations

* The site will store user details securely
* Payment details will not be stored on the site or associated database
* The website will load quickly
* The website will have a responsive layout and work on any device
* The site can be navigated easily


# Design

### Design philosophy

The name and overall colour scheme reflect the artist's preferred subject - landscapes.  A blend of greens and blues augmented by off white was used to reflect
the combination of land, sea and sky.  I believe this is a palette that users will relate to and expect when looking at land and seascapes.

### Fonts

I chose 2 fonts from Google Fonts fot the design, Julius Sans for titles and subtitles which I though gave a tall, but not over imposing feel and Poppins for all other text,
which I thought gave a nice rounded contrast to reflect the shapes on the landscape.

### Icons

I have used icons from Font Awesome throughout the site which give a nice clean consistent appearance.

### Colours

The following colours have been utilised throughout the site:

![color scheme](wireframes/colour-scheme.png)

I chose these colours as I wanted to reflect land, sea, sky and sunshine

### Images

The images used as part of the UX are all the artist's work to keep in line the general context of the site.

# Wireframes & Flowcharts

I used Balsamiq to create the wireframes and they can be found as follows:

* [Desktop](https://github.com/stiophan0309/horizon-sah/tree/master/wireframes/desktop/)
* [Tablet](https://github.com/stiophan0309/horizon-sah/tree/master/wireframes/tablet/)
* [Mobile](https://github.com/stiophan0309/horizon-sah/tree/master/wireframes/mobile/)



The following is a flowchart of the login/registration process:

![flowchart](wireframes/flowcharts/user-login-flowchart.png)

### Database Design

* The development database was sqlite3 which comes with Django
* The production database in PostgresSQL and is hosted by Heroku.

### Data Models


The Works Model:

The Works model within the Works app is used for the artworks in the gallery/shop:

Name  | Database Name | Type
----- | ------------- | ----
Catalogue ID | name | CharField
Title   | title | CharField
Description | category | CharField
Media | media | CharField
Date | date | DateField
Image | image | CharField
Price | price | Decimal

The Order Model:

The Order model within the Checkout app holds the following data for the orders in the Gallery/Shop:

Name | Database Name | Type
---- | ------------- | ----
Name | full_name | CharField
Phone Number | phone_number | CharField
Email | email | EmailField
Country | country | CharField
Postcode | postcode | CharField
Town / City | town_or_city | CharField
Street Address 1 | street_address1 | CharField
Street Address | street_address1 | CharField
County | county | CharField
Date | date | DateField

The Order Line Item Model:

The OrderLineItem model within the checkout app holds the following data for the OrderLineItem(s) in the Gallery/Shop:

Name | Database Name | Type
---- | ------------- | ----
Order | order | ForeignKey
Work | work | ForeignKey
Quantity | quantity | IntegerField

# Features

### Features That Have Been Developed

* Gallery and Shop using Bootstrap Modals which gives users information about the work and enables to add quantities to the cart

* Ability to create an account, login view orders and male Purchases

* Ability to update and delete User Profile

* Search Bar users can search through the shop using key words

* Shopping Cart where users can amend or delete items or adjust quantities

* Use of Stripe API where users can pay for their cart via the Checkout app securely

* Contact Form where users can give feedback or ask queries

### Features That Will Be Developed In The Future

* Carousel view as an alterate view of the Gallery/Shop

* Intergrate the Custom section with the Shopping Cart

* Progress indicator for Custom requests showingb their Progress


# Technologies Used

Languages

* HTML
* CSS 
* JavaScript
* Python

Tools & Libraries

* jQuery
* Django
* Git 
* Bootstrap
* Font-Awewsome
* WhiteNoise
* Gunicorn
* PIP 
* Psycopg2
* Stripe
* Toast
* GitPod
* Heroku

Databases

* PostgresSQL - production
* SQLite3 - development

# Planning & Testing

#### Planning:

Planning is an essential stage in planning any project and Web Development is no exception, especially when using new technologies and tools.  The following details how Horizon was
planned and developed.

I started by using wireframes which I constructed on Balsamiq and using Bootstrap I was quicky able to draft temnplates for the basic look of the site.  Thanks to this and the Django templating language 
I was able to re-use code throughout the site.

#### Feature Testing:

#### Gallery / Shop

Planning: Having done a gallery type project before I was able to re-use and improve upon the methodology I used there, however I devided upon a simpler layout as I wanted to combine the gallery and
the shop into one, so decided upon displaying each image with minimal info then utilising Bootstrap Modals for a detailed view with option to buy.

Implementation: Once I had setup the product model and migrate the table into the database, I could then create the view within the Works app that sends a GET request to the database and returns all the works via the works variable, making this available to the front end via the context in the return statement meant that I could loop through each work from the database and render the details using Django's template language in the HTML including the Modal enabling me to re-use the modal code.

Testing: To test that this app worked, I navigated to the 'works.html' page using the link on the Navbar and looked to see if all the works in the database had been rendered into the HTML template, and tested clicking on each image to open the modal to make sure it displayed the correct info for each work.  I also resized the browser and used Google's tools so emulate different devices to test the resposiveness of the layout.

Outcome: The works displayed correctly, all the modals worked and correctly displayed the relevant info and the page was responsive.

Verdict:  The Works app passed testing based on the above criteria.

#### Cart

Planning:  Here I used the material from the eCommerce mini-project as the main basis for the Cart app bit and added my own styling.

Implementation:  I made a context.py file first and included it in the Context processors in settings.py to tell the app what info should need as the Cart is stored in session,
not in the database.  I then wrote the view for adding, editing and deleting from the Cart.

Testing: To test the app, I navigated the to the gallery and selected a work and from the modal, selected 'add to cart'.  I then went to the cart app and tested amending the quantity and removing it from the cart.

Outcome: The work added correctly to the cart and the icon in the Navbar correctly updated.  The app correctly also amended and removed items from the cart.

Verdict: The Cart app passed testing based on the above criteria.

#### Checkout

Planning: Again I used the material from the eCommerce mini-project as a basis for the Checkout app as I felt it would based on tried ans tested knowledge which should work according to users' expectations.

Implementation:  I first construted the models (Order and OrderLineItem) and migrated them to the database.  Then I created the forms and view and setup the validation required by STRIPE in the stripe.js file to handle the creation of the stripe_id, which is required in order to process a payment with the API.

Testing: I added a selection of products to the cart and navigated to the checkout.html page, I then entered dummy contact information and used stripe test card details to attempt to create a purchase, I also tested this feature with incorrect payment information in order to check that the error messages were visible.  I also checked the Stripe website to see if the payment was processed.

Outcome: Payment was processed successfully and showed on the Stripe website and error messages appeared visiblbly and correctly when using invalid credentials.

Verdict: The Checkout app passed testing based on the above criteria.

#### Profile

Planning: I wanted to develop the Profile page covered in the eCommerce mini-project as one of my 2 additional apps for the project.

Implementation:  

Outcome: 

Verdict:

#### Custom 

Planning: As well as selling existing works any artist will offer a service for commissions or custom works and I wanted Horizon to be no exception.  

Implementation:  The object was to capture information based on the users requirements so I set up a model based on criteria required by the artist including an image upload function.  I then created the view and form and rendered the template. The feature functions like a Contact Form so the artist will contact the user to discuss final requirements and payment.

Testing:  Testing was by navigation to the custom.html which presents the user with an info page and option to request a Custom Work.  When selected the form was filled out to see if user is presented with a success or error message.

Outcome: The form successfully sent and was presented with a success popup then presented with an information page on the next steps in the process.

Verdict: The Custom app passed testing based on the above criteria

#### Search Bar

Planning: 

Implementation:

Testing:

Outcome: 

Verdict:

#### User Authentication

Planning:  I wanted users to be able to login/logout of their account so this feature was very important as is commonplace on any e-commerce site. Using the django.auth settings this feature would be heavily supported by the existing functionality that comes already pre-packed with Django.

Implementation: The user table exists in Django as standard, so all that was needed to do was construct the forms and views in order to allow the user to register an account, login to their account and logout of their account.

Testing: In order to test the User features I had to perform each view step by step, First I Created a user account and checked that the records had been added to the database, Then I attempted a login to the website using those details, after that I logged out of the account using the logout view.

Outcome: The 'ussr account I had created was visible in the database, and when I attempted to login to the account I was redirected to the profile page which displayed personal info. Finally logging out cleared my session and meant that I would have to log back into the user account to return to the profile page.

Verdict: The Checkout app passed testing based on the above criteria.



# Deployment

To run a local copy of Horizon, please do the following:

### Pre-requisites

An IDE (interactive development environment) e.g. Visual Studio Code.
You MUST have the following installed locally:

* PIP
* Python3
* Git

You will need to create accounts with the following online services in order to run this project:

* Stripe

Instructions:

1. Clone the Horizon repository by either downloading from here or type the following command into your terminal:
`git clone https://github.com/stiophan0309/horizon-sah`
2. Navigate to this folder in your terminal.
3. Enter the following command into your terminal:
`python3 -m .venv venv`
4. Initialize the environment by using the following command:
`.venv\bin\activate`
5. Install the requirements and dependancies from the requirements.txt file:
`pip3 -r requirements.txt`
6. Within your IDE now create a file where you can store your secret information for the app, I personally used an env.py file.

```
import os
os.environ.setdefault("STRIPE_PUBLISHABLE", "your_stripe_publishable_key")
os.environ.setdefault("STRIPE_SECRET", "your_stripe_secret_key")
os.environ.setdefault("SECRET_KEY", "your_django_secret_key")

```
7. Enter the following command into the terminal to migrate models into database:
`python3 manage.py migrate`
8. Then you need to Create a 'superuser' for the project using the terminal, enter the following command:
`python3 manage.py createsuperuser`
9. The app can now be ran locally using the following command:
`python3 manage.py runserver`

Deploying Horizon to Heroku:

1. Create a requirements.txt file using the following command:
`pip3 freeze > requirements.txt`
2. Create a procfile with the following command:
`echo web: python3 app.py > Procfile`
3. Push these newly created files to your repository.
4. Create a new app for this project on the Heroku Dashboard.
5. Select your deployment method by clicking on the deployment method button and select GitHub.
6. On the dashboard, set the following config variables:

```
Key	Value
DATABASE_URL	<your_database_url>
SECRET_KEY	<your_secret_key>
STRIPE_PUBLISHABLE	<your_stripe_publishable_key>
STRIPE_SECRET	<your_stripe_secret_key>
```

7. Click the deploy button on the heroku Dashboard.
8. Wait for the build to finish and click the view project link once it has!

Congratulations, Horizon is now hosted on Heroku and is live!



# Credits

Coolors.co

# Disclaimer

