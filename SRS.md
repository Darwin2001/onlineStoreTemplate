# Software Requirements Specification Document

This serves as a template for each projects' Software Requirements Specification (SRS) document. When filling this out, you will be required to create user stories, use cases, requirements, and a glossary of terms relevant to your project. Each group member must contribute to every section, so it is crucial that your group's GitHub repository shows a commit history that reflects the work of each group member. It is highly recommended that you create separate branches for each member, but since this is one single document, you will need to manually merge the branches together. It is also advisable to have multiple working versions of this document (named separately) so that one person can compile the final SRS document from the multiple working versions. Ultimately, how you go about managing this is up to you, but consistent formatting, clear commit messages, and a thorough commit history with contributions from each group member are required.

Fill the document out following the guidelines listed in each section. Maintain [proper Markdown syntax](https://www.markdownguide.org/basic-syntax/) and be sure that your group has a `main` branch with this document and the entire [template repository codebase](https://github.com/david-gary/onlineStoreTemplate) either forked or downloaded and copied into your group's repository. If you have arranged to use a different codebase as a template, you do not need to have the original template included, but a `main` branch is still required.

## Group Members

* [Ben Jansson](bjansson@uncc.edu)
* [Darwin Peraza](dperaza@uncc.edu)
* [Monish Soundar Raj](mailto:msoundar@uncc.edu)
* [Name](mmailto:email@uncc.edu)

## Revisions

When a change is made to the document, a new revision should be created. The revision should be added to the table below with all information filled out.

| Version | Date | Description | Author | Reviewed By |
| --- | --- | --- | --- | --- |
| 1.0 | 03/22/23 | Initial draft | [David Gary](mailto:dgary9@uncc.edu) | [David Gary](mailto:dgary@uncc.edu) |

## Table of Contents

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Constraints](#constraints)
4. [Use Cases](#use-cases)
5. [User Stories](#user-stories)
6. [Glossary](#glossary)

## Introduction

In this section, you should give a brief overview of what your project will be. Describe the software system you are building and what problems it solves. You should also give a short description of the stakeholders (users of the system) and what their needs are. There is no set formatting requirement, but you should maintain a consistent structure across future sections. Not all members must contribute to this section.

## Requirements

Each group member must supply at least three functional requirements for the project. Each requirement should be written in the following format:

Ben Jansson:
* **ID:** REQ-1
  * **Description:** Comment section is a section where customers can leave comments on the website, products etc.
  * **Type:** Functional
  * **Priority:** 4
  * **Rationale:** Websites usually have a comment section so that the customer can get there opion out there
  * **Testing:** Try typing a comment and post it to see if it shows up on the website
* **ID:** REQ-2
  * **Description:** A contact page where a customer can eamil or call with questions or concerns
  * **Type:** Functional
  * **Priority:** 3
  * **Rationale:** This is important if the customer wants to get in contact with the company about the webiste or products
  * **Testing:** Try an actual email or number and see if you can contact it and someone will get the message
* **ID:** REQ-3
  * **Description:** Product images so the customer can see what the product looks like
  * **Type:** Functional
  * **Priority:** 1
  * **Rationale:** This is very important so the customer can scroll through to see different veiws and see what shoes they want to look at and buy
  * **Testing:** Put a random image to see if it shows up and then the actaul picture of the product

  Darwin Peraza:
*   **ID: req-trendList:**
 *  **Description:** This trending list would work like Amazon's shoppers like you love scroll section but keep track of the click through rates of all the products and then push the most popular ones.
 *  **Type:** Non-functional
 *  **Priority** This is a five
 *  **Rationale** This is a low prioriy because while it is a nice feauture that would push sales on a site, it isn't needed and doesn't change the functionality of the site.
 *  **Testing:** This requirement could be tested by clicking on items in specific orders/amounts and seeing whether or not they appear on the list.


*  **ID: req-wishList**
 *  **Description:** This is a wishlist similar to Amazon, it creates a list of things you want and pushes and email when that thing is on sale/cheaper.
 *  **Type:** Non-functional
 *  **Priority:** This is a four
 *  **Rationale** This allows people to continue to come back to our store when their favorite things go on sale but doesn't affect the main functionality itself.
 *  **Testing**: See when an items price is lowered that an email notificaiton is sent and that wishlist items are kept in list.


*  **ID req-UserAccount**
  *  **Description:** This is a create account page that takes email and password login
 *  **Type:** Functional
 *  **Priority:** This is a two
 *  **Rationale** This is important as an account allows for things like cart and wishlist among other functionalities to work, also fosters customer loyalty.
 *  **Testing:** You could test by making sure the user is in the database when created.

Member - Monish Soundar Raj

* **ID:** REQ-1. 
  * **Description:** A search bar to search for the items in the web application. 
  * **Type:** Functional.
  * **Priority:** 4
  * **Rationale:** It allows users to search products that they want instantly, instead of looking at all the products available in the site.
  * **Testing:** By searching for products of specific brands myself before making the site public.

* **ID:** REQ-2. 
  * **Description:** A product siplay page to show the products in a enlarged view, and to display all the product description, price, and quality selection. 
  * **Type:** Functional.
  * **Priority:** 2
  * **Rationale:** It allows users to view the products enlarged images, description -> to learn about the product, and to add no of quality. 
  * **Testing:** By displaying and checking the products details in this page at each building stage of the site. 

  * **ID:** REQ-3. 
  * **Description:**  A review section for each product.
  * **Type:** Functional.
  * **Priority:** 3
  * **Rationale:** It allows users to decided which product to buy based on the review from the previous users of the same product.
  * **Testing:** By populating the review section of the products with fake reviews and by asking some real people to post the fake reviews for some products. 

## Constraints

Ben Jansson constraints: 1) Using HTML for the website, while using html to create the website using a programming language might be better but would take a lot longer. 2) Another constraint might be to figure out what kind of shoe we want to sell mens, womens, kids, sytle, sports etc.

Darwin Peraza:
*  **Developer Experience:**  When it comes to flask and python I have little experience leading to our vision not being completed exactly the way we want.
*  **Version Control:** Version control is very hard for inexperienced github users, this can create issues in our work and delay it.

Monish Soundar Raj constraints:

1) Time available to complete the project is minor.
2) As the template code is written in Flask, it might be time consuming to learn about it first before working on the project.


In this section, you should list any constraints that you have for the project. Each group member must supply at least two constraints. These can be constraints on the project itself, the software system, or the stakeholders. Constraints can be anything that limits the scope of the project. For example, that this project's template code is written using Flask and Python constitutes a constraint on the backend of the project. Constraints can also be things like the required timeline of the project. Be creative.

## Use Cases

In this section, you should list use cases for the project. Use cases are a thorough description of how the system will be used. Each group member must supply at least two use cases. Each use case should be written in the following format:

Ben Jansson:

* **ID:** UC-1
  * **Description:** The user can look through the products that we sell through pictures/decriptions and figure out what shoe they want to buy. 
  * **Actors:** The only actors here would be the customer shopping given that the store is a online website.
  * **Preconditions:** The website must be working for the customer to make a purchase and have a valid credit card to enter into the website to pay.
  * **Postconditions:** The website should get the customers order and the customer must have entered their address for the website to ship the product to.

* **ID:** UC-2
  * **Description:** A comment section can be interacted with by the customer entering in their comment and psoting it to the website for other people to read.
  * **Actors:** An actor would only be a customer, in this case who is commenting on the website.
  * **Preconditions:** The website must ahve a comment section and for the comment entered to be posted on the website.
  * **Postconditions:** The comment entered by the user needs to be posted and be able to be seen on the website.

Darwin Peraza:

*  **UC-Login**
   *  **Description:** The user inputs both a valid email and password consistent with a user in the database to login to our website.
   *  **Actors:** The customer
   *  **Preconditions:** The customer must have already registered with a valid email and password. Then login with the appropriate credentials.
   *  **Postconditions:** The customer must be logged into their account.


* **UC-SignUp**
   *  **Description:** The user must create an account with the site using name, valid email, and valid password.
   *  **Actors:** The customer
   *  **Preconditions:** The user must have a valid email that can recieve emails. A password that fits safety constraints, and a name to attatch to the account.
   *  **PostCondition:** The user must be logged in with their account and have their previous wishlist load as well as cart if anything wasn't removed from last login session.

Member - Monish Soundar Raj

* **ID:** UC-1
  * **Description:** Searching for shoes by brand.
  * **Actors:** User, Online Shoe store.
  * **Preconditions:** The user clicks on the search bar located in the nav-bar to make it active and searches to find shoes of a specific brand.
  * **Postconditions:** The user is presented with a page displaying the shoes of the brand the user searched for.

  * **ID:** UC-2
  * **Description:** Viewing product details to make a purchase.
  * **Actors:** User, Online Shoe store.
  * **Preconditions:** The user clicks on the product that they wanted to learn more about. 
  * **Postconditions:** The user is displayed with a product display page, which shows the user the selected product desciption, price, let's users select the quantity, let's users select the size and let's user to add the product to cart or buy it with one click.


## User Stories

In this section, you should list user stories for the project. User stories are a short description of how a user will be interacting with the system. Each group member must supply at least two user stories. Each user story should be written in the following format:

Ben Jansson:

* **ID:** US-1
  * **Type of User:** Customer
  * **Description:** I want to look at pictures of different shoes that I want to buy, I expect to see the multiple different pictures/veiws of the product and buy the product I want

* **ID:** US-2
  * **Type of User:** Customer
  * **Description:** I have a comment on the product that I bought and would like to leave it on the website for people to see what I think about it, I expect to enter the comment on the wbesite and for the comment to be posted on the websitefor other people to see. 

  Darwin Peraza:

*  **US-Wishlist:**
 *  **Type:** Customer
 *  **Description:** Customer logs in and sees a pair of shoes they would like.They look at their bank account and decide that this price isn't right for them. They then log in and then add that item to their wishlist. It is now stored in a list with other items he's waiting to buy and can see whenever he logs in. Additionally, he gets an email notification when it's on sale and waits until he can afford these shoes.


  **US-CreateAccount:**
 *  **Type:** Customer
 *  **Description:** Customer sees an item they want to buy, then are prompted to create an account or continue as guest.
 
 Member - Monish Soundar Raj

* **ID:** US-1
  * **Type of User:**  Customer
  * **Description:**  As an online shoe shopper, I should be able to read reviews written by others who previously brought the same product, so that I can make my decision on whether to purchase a product or not. And also, I need to be able to leave a review on a product I purchase, to help the future customer choose a product.

  * **ID:** US-2
  * **Type of User:**  Customer
  * **Description:**  As an online shoe shopper, I should be able to search for specific brand shoes, I donot want to look at all the brand shoes without having a interest to purchase them. So, having a search bar allows me look up prodcuts fast and complete the purchase soon. 

## Glossary

In this section, you should list any terms that are used in the document that may not be immediately obvious to a naive reader. Each group member must supply at least one term. Each term should be written in the following format:

* **Term:** The term that is being defined. This should be a single word or phrase that is being defined.
  * **Definition:** A definition of the term. This should be a short description of the term that is being defined. This should be a single sentence that describes the term.

**Version Control:**
 **Definition:** The practice of tracking and manging changes to a software
