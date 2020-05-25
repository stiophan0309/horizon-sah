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
request a specific work within the remit of the artist.

### Target Goals

* To introduce and promote the work of the artist
* To promote the commission service and encourage users to register
* An easy to use layout and design that works on any device
* To be able to communicate with the artist

### Client/Site Owner Goals

* Promote the work of the artist
* Generate business via comissions
* Communicate and get feedback from users
* Get inspiration from users for projects for sale

### User Stories

# Design

### Design philosophy

The name and overall colour scheme reflect the artist's preferred subject - landscapes.  A blend of greens and blues augmented by off white was used to reflect
the combination of land, sea and sky.  I believe this is a palette that users will relate to and expect when looking at land and seascapes.

### Fonts

### Icons

### Colours

The following colours have been utilised throughout the site:

![color scheme](wireframes/colour-scheme.png)

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

The following datatypes are used in the database:

* ObjectID
* String
* Boolean
* Number

Works Collection:

Name  | Database Name | Type
----- | ------------- | ----
Work ID | _id | ObjectId
Title   | title | String
Category | category | String
Image | image | String
Surface | surface | String
Media | media | String
H Size  | h_size | Number
V Size | v_size | Number
Commission | commission | Boolean
Price | price | Number

Users Collection:

Name | Database Name | Type
---- | ------------- | ----
User ID | _id | ObjectId
Name | name | String
Password | password | String
Email | email | String

Purchases Collection:

Name | Database Name | Type
---- | ------------- | ----
Purchase ID | _id | ObjectId
Name | name | String
Email | email | String
Date | date | String
Total | total | number






# Features

# Technologies Used

