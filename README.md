# Woodland Heath Golf Club

Woodland Heath Golf Club, is a golf club based in norfolk. The purpose of this site is to be able to provide information to future customers and also a booking system for members to be able to book tee times online.

The targetted audience is all who have a love of golf and also family and friend time.

![Landing Page](documentation/home-page.png)

Live Site - [Woodland Health Golf Club](https://woodland-health-golf-club.herokuapp.com/) <br>
Project Repository - [Woodland Heath Golf Club - Repository](https://github.com/NDOMINEY/Woodland-heath-golf-club)

## Table of Contents

- [Requirements](#requirements "Requirements")
- [Design](#design "Design")
  - [Wireframes](#wireframes "Wireframes")
  - [Colour Scheme](#colour-scheme "Colour Scheme")
- [Features](#features "Features")
  - [Existing Features](#existing-features "Existing Features")
  - [Future Features](#future-features "Future Features")
- [Testing](#testing "Testing")
  - [Development Process](#development-process "Development Process")
  - [Usability Testing](#usability-testing "Usability Testing")
  - [User Requirement Testing](#user-requirement-testing "User Requirement Testing")
  - [Functional Testing](#functional-testing "Functional Testing")
  - [Validator Testing](#validator-testing "Validator Testing")
- [Technologies Used](#technologies-used "Technologies Used")
  - [Main Languages Used](#main-languages-used "Main Languages Used")
- [Deployment](#deployment "Deployment")
- [Credits](#credits "Credits")
  - [Content](#content "Content")
  - [Media](#media "Media")

## Requirements

Please see below a table showing the key requirements of the site and their importance.

| Requirement                                                                         | Importance | Viability/Feasibility |
| ----------------------------------------------------------------------------------- | :--------: | :-------------------: |
| Have a clear and purposeful landing page displaying the golf course                 |     5      |           5           |
| Provide the site visitor with information about the facilities available            |     5      |           5           |
| Enable the user to be able to register for a login to gain access to online booking |     5      |           5           |
| Enable a login link so user can easily login                                        |     5      |           5           |
| Enable logged in user to log out                                                    |     5      |           5           |
| Have a memberzone which provides ability to book a tee time, edit, and delete it    |     5      |           5           |
| Provide the site user a way to be able to submit an online contact form             |     4      |           5           |

## Design

### Wireframes:

- Please find link to [Full Screen Wireframe](documentation/wireframe-large-screen.pdf)
- Please find link to [Mobile Screen Wireframe](documentation/wireframes-mobile.pdf)

### Colour Scheme:

A neutral colour scheme was selected with a green accent colour to compliment the golf course image back ground.

![Colour Scheme](documentation/colour-scheme.png)

## Features

### Existing Features

#### Navigation Bar

The navigation bar is a fixed element of the top of the page and is uniform accross all areas of the site. It have the company logo and clear links to explore different areas of the site. When the user is not logged in, the nav bar shows links to 'login' and 'register'. Once logged in, this changes to 'memberzone' and 'log out'

##### Navigation bar - user not logged in

![Navigation - user not logged in](documentation/navbar-logged-out.png)

##### Navigation bar - user logged in

![Navigation - user logged in](documentation/navbar-logged-in.png)

The navigation also changed to a hamburger menu when the screen size is smaller for viewability and usability.

##### Navigation bar - hamburger view

![Navigation - hamburger view](documentation/navbar-hamburger.png)

##### Navigation bar - collapsed hamburger view

![Navigation - collapsed hamburger view](documentation/navbar-hamburger-collapsed.png)

#### Footer

In addition to the navigation bar, on the bottom on every page is a footer. This shows the golf club logo and basic contact information for easy access for the site user.

![Footer](documentation/footer.png)

#### Home Page/Landing Page

When you first access the site, you are directed to the home page. This has a bold welcome statement so the user can verify the site they have visited quickly.

There is a summary of the course, club house and membership for quick information. For a user that is not logged in, it presents them with the following buttons which sign posts them to key areas of the site.

- 'Check out our facilities'
- 'Register to make a booking'
- 'Login in you already have an account'

![Home page](documentation/home-page-new-user.png)

#### About - Facilities

The facilities page presents the site user with an overview of facilities available at the golf course. This is shown with relevant images to show case them with overlaying banners in the accent green colour enhance them and make them eye catching.

![Facilities page](documentation/facilities-page.png)

#### Contact Us

The 'Contact Us' page give the user basic location and contact information, with an embeded google maps.
Additionally, for ease of submitting an enquiry the user is able to complete a contact form. This form will then send an email to the whgcproshop@gmail.com account and send an automatic reply to the user to confirm receipt.

![Contact page](documentation/contact-page.png)

If the user is logged in, this online enquiry form will auto populate their basic details for ease of use.

![Contact page - user auto](documentation/contact-page-user.png)

#### User Registration

Within the navigation bar, there is a link to register for a new account. This takes the user to a registration page to complete.

![Registraion](documentation/user-register.png)

Once completed, the user is redirected back to the home page and a success alert is displayed.

![Registraion Success](documentation/register-success.png)

#### User Login

Within the navigation bar, there is a link to login for users who already have an account. This takes the user to a login page. Upon sucessful login, the user is directed to the home page.

![Login](documentation/login.png)

#### User Logout

Within the navigation bar, there is a link to logout for users who have already logged in. This logs the user out, returning them to the home page with a success alert displayed.

![Logout](documentation/user-logout.png)

#### Memberzone

When a user has sucessfully logged in, they are able to click into the memberzone from the navigation bar. From here they are greated with a welcome message including their name.
From this page they are able to select to create a new booking or view and edit existing ones.

![Memberzone](documentation/memberzone.png)

#### Booking a Tee Time

##### First step - select date

Booking a tee time is completed in two steps. In the first instance, the site user is directed to the page to select a date they wish to book from. The date will default to the next calendar day.

![Booking - Select a Date](documentation/select-booking-date.png)

To prevent the user from selecting a date prior to this, an error message will be displayed and the button to progress the booking is no longer visible.

![Booking - Select a Date Error](documentation/booking-date-error.png)

##### Second step - select time and number of players

After the date is selected, the user can then view available times for that day. They will need to select their time, and the number of players for the booking to then submit it.

![Booking - Select time and players](documentation/booking-time.png)

Once the booking is complete, the user will be redirected back to the memberzone page and an alert will appear confirming the booking.

![Booking - Confirmation](documentation/booking-confirmation.png)

#### View, Edit, and Cancel Bookings

#### View Bookings

Within the memberzone, the user is able to select to view and edit bookings. This directs the user to a page listing their current bookings. If there are no bookings present it will display a message to let them know that this is the case.

![View Bookings](documentation/view-bookings.png)

#### Edit Players in Bookings

Each booking displayed has a button to enable to the user to edit the number of players for their booking. This redirects the user to an edit page which displays the selected booking and a drop down to change the total number of players.

![Edit Booking](documentation/edit-booking.png)

#### Cancel Bookings

Each booking also has a cancel button. Upon clicking this a modal pops up for the user to confirm that they want to cancel that particular booking.

![Cancel Booking](documentation/cancel-booking-prompt.png)

If the user continues to cancel the booking, they are returned to the view bookings page and an alert is displayed to confirm this has been completed.

![Cancel Booking Confirmation](documentation/cancel-success.png)

### Future Features

## Testing

### Development Process

Throughout the development process, each feature added was manually tested locally to ensure it worked as intended. Once I was happy with the result whilst in localhost, I would then add, commit and push to GitHub. This resulted in realtime changes and adjustments before committing the new code through to main.
<br>
This particularly enabled me to highlight styling issues where I predominantly used bootstrap and then customised accordingly in a separate style.css. For instance, on one circumstance through the debugging process I found that bootstrap had used !important. Although not best practice, I had to use this in my own css to be able to override it.

### Usability Testing

All text throughout the site has been styled to be clear and easy to ready. Although the background is an image through out the website, I used a translucent layer between this and text to ensure it was still readable.
<br>
Within my colour scheme, I also ensure I had an accent colour which I was able to use to direct the user to the next steps.

### User Requirement Testing

To ensure that the website meets the expectation of user, please see below user cases which summarise whether they pass and also which tests relate to them.

| <br>User Case | <br>Description                                                                               | <br>Relevant test cases                                                                                    | <br>Result |
| ------------- | --------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------- |
| <br>UC-001    | <br>As a user I want to be presented with a clear landing page with basic contact information | <br>TC-001, TC-002                                                                                         | <br>Pass   |
| <br>UC-002    | <br>As a user I want to be able to see want services are available at the golf course         | <br>TC-003, TC-009                                                                                         | <br>Pass   |
| <br>UC-003    | <br>As a user I want to be able to submit an online enquiry                                   | <br>TC-010, TC-011, TC-012, TC-013                                                                         | <br>Pass   |
| <br>UC-004    | <br>As a user I want to be able to create an account                                          | <br>TC-007, TC-016, TC-017                                                                                 | <br>Pass   |
| <br>UC-005    | <br>As a user I want to be able to view available booking                                     | <br>TC-005, TC-008, TC-014, TC-015, TC-022                                                                 | <br>Pass   |
| <br>UC-006    | <br>As a user I want to be able to create a booking                                           | <br>TC-005, TC-008, TC-014, TC-015, TC-022, TC-023, TC-024, TC-025, TC-026, TC-027, TC-028, TC-029, TC-030 | <br>Pass   |
| <br>UC-007    | <br>As a user I want to be able to view my bookings                                           | <br>TC-005, TC-008, TC-014, TC-015, TC-022, TC-031, TC-032                                                 | <br>Pass   |
| <br>UC-008    | <br>As a user I want to be able to edit the total number of player in bookings                | <br>TC-005, TC-008, TC-014, TC-015, TC-022, TC-033, TC-034, TC-035, TC-036, TC-037                         | <br>Pass   |
| <br>UC-009    | <br>As a user I want to be able to delete my bookings                                         | <br>TC-005, TC-008, TC-014, TC-015, TC-022, TC-033, TC-038, TC-039, TC-040, TC-041                         | <br>Pass   |
| <br>UC-010    | <br>As a user I want to be able to logout to keep my information private                      | <br>TC-042                                                                                                 | <br>Pass   |
| <br>UC-011    | <br>As a user I want to be able to navigate through the whole site from each page             | <br>TC-018, TC-019, TC-020                                                                                 | <br>Pass   |

### Functional Testing

Upon deployment through heroku, a total of 42 functional tests were carried out to ensure the website functioned correctly.

Please expand 'Functional Test Cases' below to see a breakdown of the tests carried out.

<details>

<summary>Functional Test Cases</summary>
|  <br>Test Case  |  <br>Description                                                                                                                                                                                                           |  <br>Pre Conditions                                                                   |  <br>Steps to Executed                                                                                                                                                                                          |  <br>Result  |  <br>Comments  |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|----------------|
|  <br>TC-001     |  <br>Website Landing Page - Upon loading the site the user is greeted with a home page                                                                                                                                     |  <br>N/A                                                                              |  <br>1. Open game in browser<br> <br><br><br> <br>2. Enter website URL<br> <br><br><br> <br>3. Check home page is loaded                                                                                        |  <br>Pass    |  <br>          |
|  <br>TC-002     |  <br>Website Landing Page - The home page demonstrates that the site is for Woodland Heath golf club and basic contact information is present                                                                              |  <br>Home page loaded                                                                 |  <br>1. Golf Club name and info is displayed<br> <br><br><br> <br>2. Check that the footer contains basic contact information                                                                                   |  <br>Pass    |  <br>          |
|  <br>TC-003     |  <br>Website Landing Page - The home page button to view golf club facilities redirects user to facilities page                                                                                                            |  <br>Home page loaded                                                                 |  <br>1. Click Check out our Facilities button<br> <br><br><br> <br>2. Check user is directed to facilities page                                                                                                 |  <br>Pass    |  <br>          |
|  <br>TC-004     |  <br>Website Landing Page - If user is logged in, two buttons are displayed in main content. These are Check out our Facilities and Go to member zone to manage bookings                                                   |  <br>User logged in, home page loaded                                                 |  <br>1. In the main content, check that two buttons are present for Check out our Facilities and Go to member zone to manage bookings<br> <br>                                                                  |  <br>Pass    |  <br>          |
|  <br>TC-005     |  <br>Website Landing Page - The home page button for Go to member zone to manage bookings<br> <br>Redirects user to member zone page                                                                                       |  <br>User logged in, home page loaded                                                 |  <br>1. Click button for Go to member zone to manage bookings<br> <br><br><br> <br>2. Check user is redirected to member zone page                                                                              |  <br>Pass    |  <br>          |
|  <br>TC-006     |  <br>Website Landing Page - If user is not logged in, three buttons are displayed in main content. These are Check out our Facilities, Register to make a booking, and Login if you already have an account                |  <br>User is not logged in, home page loaded                                          |  <br>1. In the main content, check that two buttons are present for Check out our Facilities, Register to make a booking, and Login if you already have an account                                              |  <br>Pass    |  <br>          |
|  <br>TC-007     |  <br>Website Landing Page - Home page Register to make a booking button redirects user to register page                                                                                                                    |  <br>User is not logged in, home page loaded                                          |  <br>1. Click button for Register to make a booking<br> <br><br><br> <br>2. Check user is redirected to register page                                                                                           |  <br>Pass    |  <br>          |
|  <br>TC-008     |  <br>Website Landing Page - Home page Login if you already have an account button redirects user to login page                                                                                                             |  <br>User is not logged in, home page loaded                                          |  <br>1. Click button for Login if you already have an account<br> <br><br><br> <br>2. Check user is redirected to login page                                                                                    |  <br>Pass    |  <br>          |
|  <br>TC-009     |  <br>Facilities - Facilities page displays available services from golf club                                                                                                                                               |  <br>Facilities page is loaded                                                        |  <br>1. Check facilities details are displayed to the user                                                                                                                                                      |  <br>Pass    |  <br>          |
|  <br>TC-010     |  <br>Contact Us - Contact page loaded with online enquiry form with no pre-populated date                                                                                                                                  |  <br>User is not logged in, contact us page loaded                                    |  <br>1. Check contact form is present with no pre-populated data                                                                                                                                                |  <br>Pass    |  <br>          |
|  <br>TC-011     |  <br>Contact Us - Contact page loaded with online enquiry form withpre-populated date                                                                                                                                      |  <br>User is logged in, contact us page loaded                                        |  <br>1. Check contact form is present with pre-populated data from the user account                                                                                                                             |  <br>Pass    |  <br>          |
|  <br>TC-012     |  <br>Contact Us - When contact form is submitted an email is sent to the pro shop                                                                                                                                          |  <br>Contact form has been submitted                                                  |  <br>1. On form submission an email with the details is received at the pro shop email                                                                                                                          |  <br>Pass    |  <br>          |
|  <br>TC-013     |  <br>Contact Us - When contact form is submitted an email is sent to user to confirm receipt                                                                                                                               |  <br>Contact form has been submitted                                                  |  <br>1. On form submission an email is sent to the user to confirm receipt                                                                                                                                      |  <br>Pass    |  <br>          |
|  <br>TC-014     |  <br>Login - If incorrect login details are entered an error is displayed to the user                                                                                                                                      |  <br>Login page is loaded                                                             |  <br>1. Fill in login form with incorrect details<br> <br><br><br> <br>2. Submit form <br> <br><br><br> <br>3. Check error is displayed to user                                                                 |  <br>Pass    |  <br>          |
|  <br>TC-015     |  <br>Login - If correct login details are entered and user is redirected to home page                                                                                                                                      |  <br>Login page is loaded                                                             |  <br>1. Fill in login form with correct details<br> <br><br><br> <br>2. Submit form <br> <br><br><br> <br>3. Check user is redirected to home page                                                              |  <br>Pass    |  <br>          |
|  <br>TC-016     |  <br>Registration - On the registration page, the form displays errors when incorrect details are loaded                                                                                                                   |  <br>Register page is loaded                                                          |  <br>1. Fill in register form with incorrect details<br> <br><br><br> <br>2. Submit form <br> <br><br><br> <br>3. Check error is displayed to user                                                              |  <br>Pass    |  <br>          |
|  <br>TC-017     |  <br>Registration - On the registration page, when correct information is submitted the user is redirected to home page                                                                                                    |  <br>Register page is loaded                                                          |  <br>1. Fill in register form with correct details<br> <br><br><br> <br>2. Submit form <br> <br><br><br> <br>3. Check user is redirected to home page                                                           |  <br>Pass    |  <br>          |
|  <br>TC-018     |  <br>Navigation - Navigation bar is displayed at the top of each page                                                                                                                                                      |  <br>                                                                                 |  <br>1. Cycle through each available page and check that navigation bar is present                                                                                                                              |  <br>Pass    |  <br>          |
|  <br>TC-019     |  <br>Navigation - when the user is logged out, the following links are available - Home, Facilities, Contact Us, Login, Register                                                                                           |  <br>User is logged out                                                               |  <br>1. Check that the following links are available - Home, Facilities, Contact Us, Login, Register                                                                                                            |  <br>Pass    |  <br>          |
|  <br>TC-020     |  <br>Navigation - when the user is logged out, the following links are available - Home, Facilities, Contact Us, Memberzone, Logout                                                                                        |  <br>User is logged in                                                                |  <br>1. Check that the following links are available - Home, Facilities, Contact Us, Memberzone, Logout                                                                                                         |  <br>Pass    |  <br>          |
|  <br>TC-021     |  <br>Memberzone - Page greets user by name                                                                                                                                                                                 |  <br>User is logged in and member zone page loaded                                    |  <br>1. Check greeting displays user first name                                                                                                                                                                 |  <br>Pass    |  <br>          |
|  <br>TC-022     |  <br>Memberzone - the following action buttons are available to the user - Make a Booking and View and Edit Bookings.                                                                                                      |  <br>User is logged in and member zone page loaded                                    |  <br>1. Check the following buttons are present - Make a Booking and View and Edit Bookings.                                                                                                                    |  <br>Pass    |  <br>          |
|  <br>TC-023     |  <br>Memberzone - when the Make a Booking  button is clicked the user is redirected to the booking page                                                                                                                    |  <br>User is logged in and member zone page loaded                                    |  <br>1. Click button for Make a Booking  <br> <br>2. Check user is redirected to booking page                                                                                                                   |  <br>Pass    |  <br>          |
|  <br>TC-024     |  <br>Booking - on select booking date page user is alerted of an error when the select a date with the value of today or prior                                                                                             |  <br>User is logged in and first booking page is loaded                               |  <br>1. Select a date before today<br> <br><br><br> <br>2. Check date error is displayed to user                                                                                                                |  <br>Pass    |  <br>          |
|  <br>TC-025     |  <br>Booking - on select booking date page View Available Times button is not displayed when user selects a date with the value of today or prior                                                                          |  <br>User is logged in and first booking page is loaded                               |  <br>1. Select a date before today<br> <br><br><br> <br>2. Check View Available Times button is no longer visable                                                                                               |  <br>Pass    |  <br>          |
|  <br>TC-026     |  <br>Booking - on select booking date page when a future date is selected, the user can click View Available Times button                                                                                                  |  <br>User is logged in and first booking page is loaded                               |  <br>1. Select a future date<br> <br><br><br> <br>2. Check View Available Times button is available                                                                                                             |  <br>Pass    |  <br>          |
|  <br>TC-027     |  <br>Booking - when the user clicks View Available Times button they are directed to the next booking page                                                                                                                 |  <br>User is logged in and first booking page is loaded and a future date is picked   |  <br>1. Click View Available Times<br> <br><br><br> <br>2. Check user is redirected to second stage of booking                                                                                                  |  <br>Pass    |  <br>          |
|  <br>TC-028     |  <br>Booking - when the second stage of booking page is loaded, the user is able to view available time slots                                                                                                              |  <br>User is logged in and progressed to second page of booking                       |  <br>1. Check available times are showing                                                                                                                                                                       |  <br>Pass    |  <br>          |
|  <br>TC-029     |  <br>Booking - when the user has selected a time and the total number of played they are able to click Book Time                                                                                                           |  <br>User is logged in and progressed to second page of booking                       |  <br>1. Select a time for booking and total number of players<br> <br><br><br> <br>2. Check user is able to click Book Time                                                                                     |  <br>Pass    |  <br>          |
|  <br>TC-030     |  <br>Booking - when the user clicks Book Time they are redirected to the member zone page and a success alert is displayed                                                                                                 |  <br>User is logged in and submitted booking details                                  |  <br>1. Submit booking via Book Time button<br> <br><br><br> <br>2. Check user redirected to member zone page and success alert is displayed.                                                                   |  <br>Pass    |  <br>          |
|  <br>TC-031     |  <br>Memberzone - when the View and Edit Bookings  button is clicked the user is redirected to the view bookings page                                                                                                      |  <br>User is logged in and member zone page loaded                                    |  <br>1. Click button for View and Edit Bookings  <br> <br>2. Check user is redirected to view bookings page                                                                                                     |  <br>Pass    |  <br>          |
|  <br>TC-032     |  <br>View, Edit and Cancel Bookings - All current bookings under that user is displayed                                                                                                                                    |  <br>User is logged in and view bookings page loaded                                  |  <br>1. Check all relevant bookings are displayed                                                                                                                                                               |  <br>Pass    |  <br>          |
|  <br>TC-033     |  <br>View, Edit and Cancel Bookings - Each booking displays two buttons Edit Players and Cancel Booking                                                                                                                    |  <br>User is logged in and view bookings page loaded                                  |  <br>1. Check the following buttons are displayed for each booking - Edit Players and Cancel Booking                                                                                                            |  <br>Pass    |  <br>          |
|  <br>TC-034     |  <br>View, Edit and Cancel Bookings - when user click Edit Players they are redirected to the edit booking page                                                                                                            |  <br>User is logged in and view bookings page loaded                                  |  <br>1. Click the Edit Players button on a booking<br> <br><br><br> <br>2. Check user redirected to edit booking page                                                                                           |  <br>Pass    |  <br>          |
|  <br>TC-035     |  <br>View, Edit and Cancel Bookings - when the edit booking page is loaded check that the correct booking details is loaded on the page                                                                                    |  <br>User is logged in and edit bookings page loaded                                  |  <br>1. Check that the correct data is displayed through to the edit booking page                                                                                                                               |  <br>Pass    |  <br>          |
|  <br>TC-036     |  <br>View, Edit and Cancel Bookings - user is able to change the total number of players and click Amend Booking                                                                                                           |  <br>User is logged in and edit bookings page loaded                                  |  <br>1. Change total number of players for booking via the drop down<br> <br><br><br> <br>2. Check user is able to click Amend Booking button                                                                   |  <br>Pass    |  <br>          |
|  <br>TC-037     |  <br>View, Edit and Cancel Bookings - when Amend Booking button is clicked user is redirected to the view bookings page and the record is updated                                                                          |  <br>User is logged in and user has submitted a change to the booking                 |  <br>1. Click Amend Booking<br> <br><br><br> <br>2. Check user is redirected back to the view bookings page and the updated information is reflected in the booking                                             |  <br>Pass    |  <br>          |
|  <br>TC-038     |  <br>View, Edit and Cancel Bookings - when user click Cancel Booking a pop up appears to ask the user to confirm if they want to proceed                                                                                   |  <br>User is logged in and view bookings page loaded                                  |  <br>1. Click the Cancel Booking button on a booking<br> <br><br><br> <br>2. Check a pop up appears to confirm whether the user wishes to continue                                                              |  <br>Pass    |  <br>          |
|  <br>TC-039     |  <br>View, Edit and Cancel Bookings - when the cancel booking pop up appears the following buttons are displayed - Back to Bookings and Cancel Booking                                                                     |  <br>User is logged in and cancel booking button has been clicked                     |  <br>1. Check pop up contains the following two buttons - Back to Bookings and Cancel Booking                                                                                                                   |  <br>Pass    |  <br>          |
|  <br>TC-040     |  <br>View, Edit and Cancel Bookings - when the cancel booking pop up appears and the Back to Booking is clicked the user is redirected back to the view bookings page                                                      |  <br>User is logged in and cancel booking button has been clicked                     |  <br>1. Click the Back to Booking button<br> <br><br><br> <br>2. Check user is redirected back to view bookings page                                                                                            |  <br>Pass    |  <br>          |
|  <br>TC-041     |  <br>View, Edit and Cancel Bookings - when the cancel booking pop up appears and the Cancel Booking button is clicked the user is redirected back to the view bookings page and confirmation of cancellation is displayed  |  <br>User is logged in and cancel booking button has been clicked                     |  <br>1. Click Cancel Booking Button<br> <br><br><br> <br>2. Check user is redirected back to view bookings page <br> <br><br><br> <br>3. Check alert is displayed to user to confirm the booking was cancelled  |  <br>Pass    |  <br>          |
|  <br>TC-042     |  <br>Logout - When the logout button is clicked in the navigation bar, the user is redirected to the home page and a success alert is displayed                                                                            |  <br>User is logged in                                                                |  <br>1. Click Logout link in navigation bar<br> <br><br><br> <br>2. Check user is redirected back to home page <br> <br><br><br> <br>3. Check alert is displayed to user to confirm they have been logged out   |  <br>Pass    |  <br>          |

</details>

<br>

### Validator Testing

#### Lighthouse

Lighthouse tests were carried out accross the site to ensure performance and accessibility scored highly.

- [Home](documentation/home-lighthouse.pdf)
- [Facilities](documentation/facilities-lighthouse.pdf)
- [Contact Us](documentation/contact-lighthouse.pdf)
- [Booking - Date](documentation/booking-lighthouse.pdf)
- [Booking - Time](documentation/bookingtime-lighthouse.pdf)
- [View Bookings](documentation/viewbookings-lighthouse.pdf)

#### HTML Validator

HTML validator tests were carried out accross the site.

#### Python

Through the IDE pep8 compliance was checked to ensure the code was validated

# Technologies Used

- Whitenoise was used to serve the static files - [Whitenoise](https://whitenoise.readthedocs.io/en/stable/)
- Bootstrap was used for basic html styling - [Bootstrap](https://getbootstrap.com/)
- jQuery was used for dom manipulation in the script files - [jQuery](https://jquery.com/)
- Elephantsql was used for the sites database - [ElephantSQL](https://customer.elephantsql.com/)
- EmailJS was used to send online requests to the proshop and an autoreply to
  the site user - [EmailJS](https://www.emailjs.com/)

### Main Languages Used

- Python
- Javascript
- HTML5
- CSS3

## Deployment

This site is deployed through Heruko. The following steps where followed within Heroku -

Whilst on the main dashboard, click 'Create new app'
Then enter the name of the project, select your region, and the click 'Create App'
Within the settings tab, you must update the 'Config Vars' to include the following: DATABASE_URL, DEBUG, HEROKU_POSTGRESQL_PURPLE_URL, SECRET_KEY.
Click 'Reveal Config Vars' to add.
In the deploy tab, under deployment method select 'GitHub'
Next search and connect to the correct repository from GitHub
Finally, scroll down towards the bottom and you will see 'Manual Deployment'. Select the branch you would like to deploy from and click 'Deploy Branch'. Once complete, you will be presented with a link to open the deployed site.
You can also set up auto deployments, this means Heroku will re-deploy the site every time you push an update to your GitHub repository.

#### Future development

To carry out further development on the project you can clone the repository locally. This is completed by carrying out the following steps -

Within your repository, make sure you are on the 'Code' tab
Click on the button that shows '<> Code'
Then select how you wish to clone
To create an isolated version of the project, you may add a branch off of main. To do this follow the below steps -

Whilst in the code section, click on 'branch'
You will then see a breakdown of the exisiting branches
To add a new branch, click 'New Branch' which is a green button
Then name your branch and select the branch source

## Credits

### Content

#### EmailJS

Set up for EmailJS was aided by the CodeInstitue tutorials and the EmaiJS suppoting documentation.

#### Django login and registration

Django tutorial videos from Codemy on youtube to help implement the register, login and logout functionality - [Codemy](https://www.youtube.com/@Codemycom/search?query=django%20user)

#### Image compression

The following online tool was used to compress the size of images for the site - [tinypng & tinyjpeg](https://tinypng.com/)

### Media

#### Images

The following images were sourced from [Pexels](https://www.pexels.com/)

- [Background golf course](https://www.pexels.com/photo/green-leaf-trees-on-grass-field-914682/)
- [Features - Mini Golf](https://www.pexels.com/photo/green-and-yellow-putters-on-green-grass-6370068/)
- [Features - Golf Tuition](https://www.pexels.com/photo/boy-holding-golf-club-in-front-of-crouching-woman-1325655/)
- [Features - Pro Shop](https://www.pexels.com/photo/man-standing-beside-man-holding-gray-club-1325735/)
- [Features - Putting Area](https://www.pexels.com/photo/person-playing-golf-1325661/)
- [Features - Golf Buggy](https://www.pexels.com/photo/bag-bus-car-cart-274108/)
- [Features - Practice Range](https://www.pexels.com/photo/person-swinging-golf-club-on-field-1325659/)

#### Logo

The logo was created using [Adobe Express](https://www.adobe.com/express/create/logo/website)

#### Favicon

The following generator was used for the sites favicon - [favicon.io](https://favicon.io/favicon-converter/)

#### Icons

The following was used for icons on the site - [font awesone](https://fontawesome.com/icons/golf-ball-tee?f=classic&s=solid&pc=%23ffffff)
