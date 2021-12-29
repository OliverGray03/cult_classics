# Cult Classics
![Website mock ups](media/readme/cultclassicsmockups.png)
Cult Classics is an online shop, which sells authentic vintage football shirts. This project was built as the 4th Milestone Project for the Code Institute - Full Stack Developer Course.
**IMPORTANT (disclaimer): This project is meant for educational purposes only. Stripe's credit card payment functionality is real but remains in a "test mode" so that no payments will be taken. Please do not enter any personal credit/debit card numbers whilst using the site. This project contains real products from existing brands. If you want to make a test purchase on my site you can use the deteails below.
Test transaction details:

credit card: 4242 4242 4242 4242
expiration date: 04 / 24
CVC: 424
ZIP: 42424

The live site can be viewed [here]()

# Table of contents
1. [User Experience (UX)](#UX)
    1. [Strategy & Scope](#Strategy)
    2. [Features](#Structure)
    3. [Skeleton](#Skeleton)
    4. [Design/Surface](#Design)
2. [Information Architecture](#Database)
3. [Technologies](#TechnologiesUsed)
4. [Testing](#Testing)
5. [Deployment](#Deployment)
    1. [Local]()
    2. [Heroku]()
    3. [AWS]()
    4. [Stripe]()
6. [Credits](#Credits)
7. [Acknowledgements](#Acknowledgements)

# UX
## Strategy
### Project Goals
The goal of this project is to build a full stack Ecommerce website based around the market for reselling and collecting vintage and rare football shirts. The site will act a destination site for all potential buyers but also give users the opportunity to sell their shirts to the site owners. 

## User Stories
### Viewing and Navigation
 - As a first time user i would like to know what the website is offering so i can make a decision on whether i would like to continue using the site. 
 - As a first time user i would like to see easy to understand and use navigation to move around the site

### Registration and User Accounts
 - As a site user i would like to register an account to make future purchases easier. 
 - As a logged in user i would like to see a profile summary and all my previous order details. 
 - As a returning user i would like to save products to a wishlist so i can easily purchase at a later date. 
 - As a site user with an account i would like to easily log in and log in of my account. 

### Sorting and Searching
 - As a shopper i would like to view all the products available to buy on the site so i can browse options i may not have seen before. 
 - As a shopper i would like to narrow down the products on the site to a specific category so i can find a product quickly. 
 - As a shopper i would like to view the products in specific orders for example acending price order or decending rating order. 
 - As a shopper i would like to search for products using key words so i can quickly narrow down to a product i know i would like to purchase. 
 - As a shopper i would like to be able to add products i like to a favourites list to view at a later time. 

### Purchasing and Checkout
 - As a shopper i would like to be able to add items to a basket should i wish to make more than one purchase. 
 - As a shopper i would like to see live updates to the total cost of my basket so i can make a decision as to if i can purchase more. 
 - As a shopper i would like to be able to update my basket by further adding and removing products i have changed my mind on. 
 - As a shopper i would like to checkout and pay for my items securely. 
 - As a shopper i would like to see an order confirmation so i can validate my purchase. 

### Admin and Store Management 
 - As site admin i would like to be able to easily add, edit and remove products from the site so i can minimise process time. 
 - As site admin i would like to be able to view contact messages that have been sent in by site users and respond to them. 

# Structure
## Features 

### Base Template 
- Navigation Bar
    - The nav bar is split into two levels. The first level contains the business name/brand, a clickable link that will return the user to the home page from any page, a product search bar useful for returning users wanting to search/purchase a specific product, a register/login link and a bag icon that updates once users add items to their bag. 
    - The second Nav bar contains searchable links by category, useful for returning users.
- Navigation Bar - Mobile 
    - When used on mobile the nav bar condenses down to include the bag icon, account icon and a search icon with an interactive dropdown search box. 
- Footer
    - The footer contains clickable social media icons, useful for new users wanting to learn more about the business.
    - The footer also contains useful company links to login/register to the site, a link to an about us page and a link to a contact page, all useful for new interactive users.
    - The footer also contains useful quick category search links to the products page. 
- Toast Messages
    - Toast messages have been used throughout the site to give the user feedback on their actions, the messages are colour coded, Green for success, Yellow for warning, Blue for information and Red for an error.

### Home Page
- Home Page
    - The home page incorporates all of the above base template features additionally it simply features a large banner image, a specific product image to give a clear indication to the user what the sites purpose is. 
    - On top of this image a large "Shop now" button is displayed to draw the user into the product page. 

### Products
- Product Page 
    - In the top left of this page there is a product counter to indicate how many products are being shown depending on the search criteria. 
    - In the top right of this page there is a sorting selector so a customer can sort the products by price (high or low), rating (high or low), name (high or low) or category (high or low).
    - The page is responsive, displaying 4 products on extra large screens, 3 on large screens, 2 on medium and 1 on small screens. 
    - The products are displayed in a card format, a large image with small key informative information below like the price and rating. 

- Product Detail page 
    - The product detail page shows the product image as a large image on the left of the screen or on top on small screens.
    - Product detail including the price is displayed to the right of this or just below on smaller screens.
    - Below the detail there is a quantity section where a user can adjust the quantity of a product before purchase on which the price updates. 
    - There is then a favorites section where logged in users will see their saved items enticing them to add these products to their bag before checking out. 
    - There are then two buttons, a back button for users to continue shopping and an add to bag button which adds the product to the users shopping bag. 
    - The product detail page displays four random products saved to the users favourites to entice the customer to add a further product to their bag. 

### Shopping Bag & Checkout 
- Shopping Bag 
    - The shopping bag has similar attributes to the product detail page, it shows a large product image to the left of the screen and the product detail to the right of this, including the name, sku number, price and quantity. 
    - At this point the quantity is still an adjustable field for the use to make any final amendments, they also have the option to remove the product from the bag completely. 
    - A sub total and grand total price are shown next to the product and at the bottom of the screen with the continue to purchase button. The grand total includes any shipping costs. 

- Checkout Page
    - The checkout page is split into two sections, on the left side of the page there is a form, this needs to be complete by the user to gather all the relevant information like name , delivery information and payment information. 
    - On the right hand side of the page there is an order summary, this includes the product information and the total payable amount including the delivery costs. 
    - There is a back to bag button giving the user the opportunity to make any last minute changes. 

### About us and Contact information 
- About us 
    - This page is split into two sections, a small paragraph about the business and why it is run. 
    - Secondly on the right side of the page there is an address to the store and a timetable detailing opening times. 
    - Finally, there is a link to the contact page for users to direct a question to site owners. 
- Contact us 
    - TIhis page allows users to directly contact the business admin by completing an online form. 
    - One the user completes the form a success message is given as feedback.

### Register, Login and Profile
- Profile 
    - The profile page is split into two sections, on the left hand side the user can update their default delivery information by complting an online form and using the update button. 
    - The right had side of the page details the users order history. 
- Favourites 
    - Logged in users will be able to see their saved favourites using the favourites link in the nav bar from here they can add these products to their basket. 
    - Users will also be able to add further products from the products page or remove products from their favourites using the relevant icons on the product cards. 
- Allauth 
    - The sign up, register, password reset, email confirmation pages etc, have all been provided by Django allauth.

### Admin Features
- Admin has access to th all additional features accross the site. 
    - Theadmin profile includes a product management page in the nav bar. From here the admin has access to full CRUD functionality being directed to a form to add, remove and edit any product for or on the site. 

# Skeleton
- Home
    - [Desktop](media/readme/wireframes/homedesktop.png)
    - [Mobile](media/readme/wireframes/homemobile.png)
    - [tablet](media/readme/wireframes/hometablet.png)
- Products
    - [Desktop](media/readme/wireframes/productsdesktop.png)
    - [Mobile](media/readme/wireframes/productsmobile.png)
    - [Tablet](media/readme/wireframes/productstablet.png)
- Product Detail
    - [Desktop](media/readme/wireframes/productdetaildesktop.png)
    - [Mobile](media/readme/wireframes/productdetailmobile.png)
    - [Tablet](media/readme/wireframes/productdetailtablet.png)
- Checkout
    - [Desktop](media/readme/wireframes/checkoutdesktop.png)
    - [Mobile](media/readme/wireframes/checkoutmobile.png)
    - [Tablet](media/readme/wireframes/checkouttablet.png)
- Bag
    - [Desktop](media/readme/wireframes/bagdesktop.png)
    - [Mobile](media/readme/wireframes/bagmobile.png)
    - [Tablet](media/readme/wireframes/bagtablet.png)
- Login
    - [Desktop](media/readme/wireframes/logindesktop.png)
    - [Mobile](media/readme/wireframes/loginmobile.png)
    - [Tablet](media/readme/wireframes/logintablet.png)
- Logout
    - [Desktop](media/readme/wireframes/signoutdesktop.png)
    - [Mobile](media/readme/wireframes/signoutmobile.png)
    - [Tablet](media/readme/wireframes/signouttablet.png)
- Register
    - [Desktop](media/readme/wireframes/registerdesktop.png)
    - [Mobile](media/readme/wireframes/registermobile.png)
    - [Tablet](media/readme/wireframes/registertablet.png)
- Profile
    - [Desktop](media/readme/wireframes/profiledesktop.png)
    - [Mobile](media/readme/wireframes/profilemobile.png)
    - [Tablet](media/readme/wireframes/profiletablet.png)
- Favourites
    - [Desktop](media/readme/wireframes/favouritesdesktop.png)
    - [Mobile](media/readme/wireframes/favouritesmobile.png)
    - [Tablet](media/readme/wireframes/favouritestablet.png)
- Contact 
    - [Desktop](media/readme/wireframes/contactdesktop.png)
    - [Mobile](media/readme/wireframes/contactmobile.png)
    - [Tablet](media/readme/wireframes/contacttablet.png)
- About us 
    - [Desktop](media/readme/wireframes/aboutdesktop.png)
    - [Mobile](media/readme/wireframes/aboutmobile.png)
    - [Tablet](media/readme/wireframes/abouttablet.png)

# Design
## Typography
- The typography used throughout the site was called Lato taken from [Google Fonts](https://fonts.google.com/)

## Colour Scheme 
 - I took inspiration for my colour scheme from big sporting brand websites like Nike and Addidas. Both these use start contrast of white and black with accent colours throughout. With Cult Classics being a sports related website i wanted to replicate the feel of these brands. 

 - The below was my full colour scheme created using [Coolers](https://coolors.co/)

![colour scheme](media/readme/colourscheme.png)

    - #FFF Was primarily used for the background and some contrasting buttons
    - #000 Was primarily used as contrasting features, for example the nav bar and footer
    - #DEE0C8 was used throughout the site for detailing, including line breaks and the delivery banner
    - #7E7E7E Was used for text throughout the site

## Icons
- Icons were chosen and used throughout the site using [Font Awesome](https://fontawesome.com/), i have used icons that are recognisable to everyone from using day to day apps and websites 

# Database

# Technology Used
Languages
- [HTML](https://en.wikipedia.org/wiki/HTML)
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

Libraries & Integrations
- [Django](https://www.djangoproject.com/)
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/index.html)
- [Django Countries](https://pypi.org/project/django-countries/)
- [Stripe](https://stripe.com/gb)
- [Amazon Web Services](https://aws.amazon.com/)
- [SQLite](https://www.sqlite.org/index.html)
- [Font Awesome](https://fontawesome.com/)
- [Google Fonts](https://fonts.google.com/)
- [JQuery](https://jquery.com/)

Version control
- [Git](https://git-scm.com/) 
- [Git Hub](https://github.com/)

Wireframes 
- [Balsamiq](https://balsamiq.com)

Other
- [Heroku](https://id.heroku.com/login)
- [Google Dev Tools](https://developers.google.com/web/tools/)
- [Responsinator](https://www.responsinator.com/)
- [Chrome lighthouse](https://developers.google.com/web/tools/lighthouse)
- [W3C Jigsaw](https://jigsaw.w3.org/css-validator/)
- [Favicon](https://favicon.io/)

# Testing

[Testing.MD](https://github.com/OliverGray03/cult_classics/blob/main/TESTING.MD)


# Deployment
## Local Deployment
The below requirements will need to be set up before deployomg the project
- First ensure the following are set up on your chosen IDE:
    - PIP3 Python package installer
    - Python 3.6
    - Git version control
- Secondly you will need an account with Stripe to allow online payments.

To set the project up locally you can follow the following steps:
    1. Navigate to the repository - cult_classics
    2. Click the code dropdown button, ensure the HTTPS tab is selected in the dropdown and copy the url.
    3. In your IDE navigate to the desired directory.
    4. Open the terminal and enter the following code: git clone https://github.com/Tawnygoody/Tarmachan.git
        - Note: Alternatively you can select the "Download Zip" option from the dropdown menu, and extract the zip file to your chosen directory within your IDE.
    5. To install the required dependencies needed to run the application type the following into the terminal: pip3 install -r requirements.txt
    6. Environment variables will then need to be set up. This can be done in a couple of ways:
        - Create an env.py file in the root directory, and ensure that it is added to the .gitignore file so that secret keys aren't published to github. Add to the following code to the the env.py file:
            -   import os
  os.enviorn["DEVELOPMENT"] = True
  os.environ["SECRET_KEY"] = "Your Secret Key"
  os.environ["STRIPE_PUBLIC_KEY"] = "Your Stripe Public Key"
  os.environ["STRIPE_SECRET_KEY"] = "Your Stripe Secret Key"
  os.environ["STRIPE_WH_SECRET"] = "Your Stripe WH Secret Key"
        - Set the environment variables with your IDE settings (if available):
            - Key | Value 
              DEVELOPMENT| True
              SECRET_KEY | your secret key
              STRIPE_PUBLIC_KEY | your stripe public key
              STRIPE_SECRET_KEY | your stripe secret key
              STRIPE_WH_SECRET | your stripe WH secret key
            - Your stripe variables can be located on your stripe dashboard.
            - You can generate a secret key at [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/)
    7. To set up the database you will need to migrate the database models. To do so type the following into the terminal:
          - python3 manage.py makemigrations
            python3 manage.py migrate
    8. To load the product fixtures into the database type the following into the terminal:
        

## Deployment to Heroku



# Credits
- Code Institutes Boutique Ado project was used as inspiration and the underlining building blocks of the projects. 
- Bootstrap documentation for helping to fix the padding on the header on the home page for mobile screens.


## Media
- Product images for the site were obtained from [Greatest Kits](www.greatestkits.co.uk)
# Acknowledgements

