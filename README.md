# Planning Phase

## Strategy:

### User Research:
Ireland attracts a large number of students from all over the world, making the search for accommodation challenging. Many students cannot afford expensive student accommodations and opt for cheaper options, such as shared houses with 2, 3, 4, or sometimes more roommates. Additionally, some students prefer single rooms depending on their budget.

*Note: The user research conducted for this project was based on personal experiences, as I, as an international student, faced similar challenges upon arriving in Ireland. Most of my friends also encountered similar difficulties.*

### Competitive Analysis:
Existing platforms often facilitate accommodation searches through real estate agencies, but response times can be slow due to high demand. Moreover, Facebook communities like "Brazilian Students in Dublin" or "Venezuelan Students in Dublin" also serve as a resource, but searching can be complicated due to various posts and outdated listings. Our platform will focus solely on available rooms, removing listings once they are rented out.

*Note: The competitive analysis was also informed by personal experiences and observations, recognizing the limitations of existing platforms.*

### Feature Prioritization:
Based on user research and competitive analysis, prioritize features that address the pain points identified. Key features include:
 - User-friendly room listing creation process, allowing users offering a room to specify details like price of rent, location, description and photos.
 - Robust search and filtering options to help users find suitable accommodation quickly.
 - Secure messaging system for communication between users interested in renting or listing rooms.
 - Communication with the Post Author, details offered like, email and phone.
 - User authentication and profile management functionalities like Delete and Edit posts.
 - Admin panel for content moderation and management to ensure the platform's integrity.

### User Personas:
Develop user personas representing different segments of the target audience, such as:
- **Maria:** A budget-conscious international student looking for an affordable shared room close to her university.
- **Ahmed:** An exchange student seeking a single room with specific amenities within a reasonable budget.
- **Emily:** A local homeowner interested in renting out a spare room to international students for extra income.

*Note: The creation of user personas was influenced by personal experiences and interactions with individuals facing similar accommodation challenges.*

### Brand Identity:
RoomFinder Ireland's brand identity, which includes the logo, colour scheme, and tone of voice, is designed to connect with its users. The logo represents simplicity and trust. The font is easy to read and friendly. The tone of voice is welcoming and helpful. Consistency across the platform ensures that users always feel at ease, reinforcing the platform's values of reliability, affordability, and inclusivity.

## Scope:

RoomFinder Ireland aims to provide a user-friendly online platform for international students in Ireland to find suitable accommodation. The scope of the project includes the development of key features essential for the platform's functionality and usability:

### User Registration and Authentication:
- Users will be able to create an account, providing necessary information such as name, email, and password.

### Room Listing Creation:
- Users can list available rooms for rent, specifying details like price of rent, room type (shared or single), location, description and photos.

### Location API Integration:
- Integration of a location API to provide advanced mapping and geocoding features, allowing users to visualize the location of listed rooms and find properties based on proximity to points of interest or specific areas of the city.

### Searching and Filtering:
- Students can search for available rooms based on criteria such as location, price range and room type.

### Messaging System:
- A secure messaging system would facilitate communication between users interested in renting or listing rooms, allowing for negotiation and arrangement of terms.

### Communication with Post Author:
- Users will have access to contact information, such as email and phone number of the author of a post, enabling direct communication for further inquiries or arrangements.

### User Management:
- Users will have the ability to manage their profiles, update personal information, view their own posts, and have options to delete or edit a post if needed.

### Admin Panel:
- An admin panel will allow for content moderation, user management, and monitoring of platform activity.

- Admins will be able to approve or unapprove a post for publication.

- Admins will have the capability to delete any post if necessary.

Additionally, features have been classified based on their importance using the MOSCOW prioritization:

UX efforts **must** address these:
- Register and Authentication.
- Login.
- Room Listing Creation.
- Post approved/unpproved (only by admin).
- User Profile Management.

Next topics, will be implemented in the future:

UX efforts **should have** these:
- Location API Integration.
- Room Searching and Filtering.
- Messaging System.

UX efforts **could have** these:
- Advanced Notification System: Implementation of an advanced notification system to alert users about new listings matching their preferences, updates on their inquiries, or important platform announcements.
- Social Media Integration: Integration with social media platforms to allow users to share listings or invite friends to join the platform, enhancing user engagement and expanding the platform's reach.
- Advanced Notification System: Implementation of an advanced notification system to alert users about new listings matching their preferences, updates on their inquiries, or important platform announcements.
- Review and Rating System: Incorporation of a review and rating system where users can provide feedback and rate their experiences with landlords and accommodations, helping other users make informed decisions.
- Localized Language Support: Addition of localized language support to cater to users from diverse linguistic backgrounds, providing a more inclusive experience and expanding the platform's accessibility.

## Structure
The structure of RoomFinder Ireland's platform is designed to ensure intuitive navigation and easy access to key features.

![User flow chart](docs/images/workFlow.png)

(I used [Lucidchart](https://www.lucidchart.com/) to help me visualize the user journey)

The flowchart illustrates the user journey within the platform, detailing every step from user registration to room listing creation, searching for accommodations, communication with post authors, and Admin management. Each stage is carefully mapped out to optimize user interaction and streamline the process of finding and renting accommodations

### User Stories:

- #### As **an Admin**...

As an **Admin**, I can **utilize a text editor within the admin panel** so that **I can create and edit room listings in a clear and visually appealing way.**

As an **Admin**, I can **filter and search all room listings from the admin page** so that **I can review, edit, and delete listings quickly.**

As an **Admin**, I can **easily navigate the admin panel** so that **I can view, search, add, and delete room listings.**

As an **Admin**, I can **approve new room listings offered by users for the community** so that **I can ensure listings are accurate and suitable.**

As an **Admin**, I can **access a list of pending room listings** so that **I can review details such as location, price, and photos.**

As an **Admin**, I can **reject room listings that do not meet the platform's standards or violate community guidelines** so that **I can provide clear reasons for rejection to users.**

As an **Admin**, I can **receive notifications when a room is rented** so that **remove the listing from the platform, ensuring accurate availability information for users searching for available rooms.**


- #### As a **user offering a room**...

As a **user offering a room**, I can **create an account** so that **I can access the platform's features.**

As a **user offering a room**, I can **easily create a listing for a room I have available for rent, providing all necessary details and photos**, so that **I can attract potential tenants.**

As a **user offering a room**, I can **receive an alert** so that **I am informed when my post has been submitted for review.**

As a **user offering a room**, I can **manage my room listings, including editing or deleting them as needed**, so that **I have control over my listings.**

As a **user offering a room**, I can **receive notifications when someone contacts me regarding my room listing, and I can respond promptly**, so that **I can engage with potential renters effectively.**

As a **user offering a room**, I can **easily find relevant contact information** so that **I can contact the site administrator via email if needed.**


- #### As a **user searching for a room**...

As a **user searching for a room** I can **create an account** so that **I can access all the features.**

As a **user searching for a room** I can **search for available rooms based on my preferences (location, price, type of room)** so that **I can find suitable accommodation that meets my needs.**

As a **user searching for a room** I can **view detailed information and photos of available rooms** so that **I can make informed decisions about potential accommodations.**

As a **user searching for a room** I can **get the contact details of the owner, such as email or phone** so that **I can communicate directly regarding the room.**

As a **user searching for a room** I can **access the platform from any screen size and still have a good browsing experience** so that **I can easily search for rooms using any device.**

As a **user searching for a room** I can **easily navigate to various pages of the website by typing a URL into the web browser** so that **can explore different listings effortlessly.**

As a **user searching for a room** I can **quickly locate relevant contact information** so that ** I can contact the site administrator via email if necessary.**

## Skeleton

The skeleton of RoomFinder Ireland's platform translates the structural design into wireframes, outlining the placement of key elements and functionalities on each page. Ensuring a clear and intuitive user experience. Key components of the skeleton include:

**Wireframes:** Wireframes are created for each page of the platform, depicting the layout of elements such as navigation bar, search filters, listing cards, room details, user profile, and messaging interface.

* [Homepage - Sign up](docs/images/homepage-signup.png)

* [Homepage - Logged in](docs/images/homepage-loggedin.png)

* [Creating a List](docs/images/create-a-list.png)

* [Available Rooms](docs/images/available-rooms.png)


**Colour Scheme:**
The chosen colors for the project development were inspired by the colors of the Irish flag, which are green, white, and orange. Since the app is about room search in Ireland, I thought it would be a good idea for users to have this association in mind when accessing the platform.

I used the following [Ireland Flag](docs/images/flag02.png) to generate the following color scheme on coolers.co. The theme colors selected were: #03a64a (dark green), #02733e (light green), #f27405 (dark orange), #f25c05 (light orange), and #f2f2f2 (white) was added.

![Colour Schema](docs/images/color_schema.png)


**Typography:**

The typography chosen for the project is "Roboto", a clean and modern sans-serif font. This font was selected for its readability and versatility, making it suitable for various text elements throughout the application.

![Typography - Roboto sans-serif font](docs/images/font-roboto.png)

**Database Schema:**

This diagram depicts the relationship between two tables: Room and User. The Room table stores information about available rental rooms, while the User table, provided by Django, stores user data.

The Room table is linked to the User table through a foreign key relationship using the room_owner_id field, representing the room owner.

Below is the preliminary layout for the database tables:

![Database Schema](docs/images/ERD_project4.png)

**Agile Methodology**

The entire development process following Agile methodology can be found here [AGILE](AGILE.md). I wanted to leave a note, stating that all user stories, epics, Kanban board were verified, and a comment was added at the conclusion of each user story. It's worth noting that some user stories had more than one task, and while some tasks remained open, I've added a note that they will be achieved in the future. For all other completed tasks, a tick mark was placed on each of them.

## Live Website

To access the live version of the website, click [here](https://room-finder-ireland-6026a4a9591e.herokuapp.com/).

## Features:

**Navbar**:

I chose "RoomFinder Ireland" because it clearly tells users what the app does: helps them find rooms in Ireland. TThe inclusion of the magnifying glass symbolizes the search functionality, indicating to users that they can search for available rooms using the platform.
Additionally, the use of "RoomFinder Ireland" as the application name emphasizes its focus on room finding services specifically in Ireland.

![Logo](docs/images/logo.png)

**Signed Out**
When the user is signed out, they are directed to a simplified navbar with only "Register" and "Login" options.

![Signed Out](docs/images/sign_out.png)

**Signed In**

When signed in, users have access to all navigation links. Additionally, a message indicates the user's logged-in status, displaying their username.

![Signed In](docs/images/navigation.png)

As soon as the user signs in, a modal pops up:

![Signed In Modal](docs/images/modal_logged_as_user_1.png)


**Log In**

The "Log In" page is a simple form requesting the username and password for users who already have an account.

![Log In](docs/images/log_in.png)

**Register/Sign Up**

The "Register" or "Sign Up" page features a simple form for new users to create an account. The form typically includes fields for username, email, password, and password confirmation. Additionally, instructions are provided on password requirements for users.

![Register/SignUp](docs/images/sign_up.png)

**Log out**

The "Log Out" page displays a confirmation message asking the user if they really want to log out. If confirmed, a modal appears confirming the successful logout.

![Log out page](docs/images/log_out.png)

![Modal Successful sign out](docs/images/modal_sign_out.png)

**Hamburguer menu**

On smaller screen sizes, a hamburger menu is displayed.

![Hamburguer Menu](docs/images/menu-toggle.png)

**Carousel**
A carousel effect on the homepage automatically displays several photos of rooms.

![Carousel](docs/images/carousel.png)

**Add a Room page**

The add_room page allows users to fill out a form with room information (listing), and upon submission, it is sent for approval by the admin. Once approved, it is available to view in card format on the room_finder page.

![Add Room Form](docs/images/add_room.png)

![Modal awaiting](docs/images/modal_awaiting.png)

**Room finder page**

The room_finder page displays cards that have been approved by the admin. If the user is a superuser (admin), they have access to all the cards and can approve pending ones, as well as delete or edit existing ones. Regular users can only see approved cards, and they have the option to delete or edit their own listings if needed.

![Room Finder page](docs/images/room_finder.png)

![Card displayed for Admin](docs/images/card_admin_all_buttons.png)

![Card displayed dor Regular user](docs/images/card_user_edit_delete_button.png)

**Edit room page**

When a user clicks on the edit button, they are redirected to a page containing the same form as the add_room page. After making the necessary edits and submitting the form, the listing becomes pending approval by the admin.

![Edit Form](docs/images/edit_form.png)

**Delete Button**

Both superusers and regular users, when clicking on the delete button, are prompted with a modal for confirmation to ensure they indeed want to delete the post. This practice aims to provide a good user experience.

![Modal Delete Confirmation](docs/images/modal_delete.png)

**Contact us page**

The "Contact Us" page is simple, providing direct contact information such as email, phone number, and links to social media profiles.

![Contact us page](docs/images/contact_us.png)

## Technologies Used

- **HTML**: Formed the foundation language for structuring the layout of all templates.

- **CSS**: Customized CSS was applied to enhance the visual aesthetics of the page.

- **JavaScript**: Integrated JavaScript extensively to manipulate the Document Object Model (DOM) and interact with the backend for CRUD (Create, Read, Update, Delete) operations on the database.

- **Python**: We used Python in the Room Finder project for the backend development, which includes the system's logic and interaction with the database.

- **Django**: Employed as the primary Python framework for this project.

- **Django All Auth**: Implemented to manage user authentication functionalities such as sign-in, sign-up, and sign-out.

- **Cloudinary**: Integrated Cloudinary to manage image uploads and storage efficiently within the Room Finder project

- **Heroku**: Utilized as the deployment platform to host the project and make it accessible to the public.

- **Heroku PostgreSQL**: Served as the database solution both during development and deployment phases.

## Testing

**Google's Lighthouse Performance**

- [Homepage - Desktop](docs/images/lighthouse_homepage_desktop.png)
- [Homepage - Mobile](docs/images/lighthouse_homepage_mobile.png)
- [Contact - Desktop](docs/images/lighthouse_contact_desktop.png)
- [Contact - Mobile](docs/images/lighthouse_contact_mobile.png)
- [Sign in - Desktop](docs/images/lighthouse_login_dasktop.png)
- [Sign in - Mobile](docs/images/lighthouse_login_mobile.png)
- [Register - Desktop](docs/images/lighthouse_register_dasktop.png)
- [Register - Mobile](docs/images/lighthouse_register_mobile.png)
- [Add room - Desktop](docs/images/lighthouse_addroom_dasktop.png)
- [Add room - Mobile](docs/images/lighthouse_addroom_dasktop.png)
- [Room Finder - Desktop](docs/images/lighthouse_findroom_desktop.png)
- [Room Finder - Mobile](docs/images/lighthouse_findroom_desktop.png)


**Code Validation**

**Python files** have been validated using [Python Linter](https://pep8ci.herokuapp.com/). Attached are screenshots of the validation.

- [Setting.py](docs/images/validador_settings_py.png)
- [Admin.py](docs/images/validator_admin_py.png)
- [Forms.py](docs/images/validator_forms_py.png)
- [Models.py](docs/images/validator_models_py.png)
- [Urls.py](docs/images/validator_urls_py.png)
- [Views.py](docs/images/validator_views_py.png)

**HTML pages** have been validated through [W3C](https://validator.w3.org/).

- [add_room.html](docs/images/validator_add_room_html.png)
- [contact.html](docs/images/validator_contact_html.png)
- [edit_room](docs/images/validator_edit_form_html.png)
- [index/base.html](docs/images/validator_html_home.png)
- [login.html](docs/images/validator_login_html.png)
- [signup.html](docs/images/validator_register_html.png)
- [room_finder.html](docs/images/validator_room_finder_html.png)
- [signout.html](docs/images/validator_sign_out_html.png)

**CSS file** has been validated through [W3C](https://jigsaw.w3.org/css-validator/).

- [style.css](docs/images/validator_css.png)

**JavaScript** has been validated through [Jshint](https://jshint.com/)

- [script.js](docs/images/validator_js_script.png)

**Responsiveness**

Special attention is given to ensuring that the platform is responsive across various devices and screen sizes. The wireframes are optimized to adapt seamlessly to laptops, tablets, and smartphones, providing a consistent user experience across all devices.

- [Homepage - large](docs/images/responsiveness_home_largedevice.png)
- [Homepage - medium](docs/images/responsiveness_home_medium.png)
- [Homepage - small](docs/images/responsiveness_home_small.png)
- [Contact - Large](docs/images/responsiveness_contact_large.png)
- [Contact - Medium](docs/images/responsiveness_contact_medium.png)
- [Contact - small](docs/images/responsiveness_contact_small.png)
- [Add Room - large](docs/images/responsiveness_addroom_large.png)
- [Add Room - medium](docs/images/responsiveness_addroom_medium.png)
- [Add Room - small](docs/images/responsiveness_addroom_medium.png)
- [Room Finder - large](docs/images/responsiveness_roomfind_large.png)
- [Room Finder - medium](docs/images/responsiveness_roomfind_medium.png)
- [Room Finder - small](docs/images/responsiveness_roomfind_small.png)

**Manual Test**

*Note: "?" - Will be implemented in the future*

**As an Admin I can ....**

| Status  | Feature |                                                                           
|:-------:|:--------|
| &check; | utilize a text editor within the admin panel, create and edit room listings |       
| &check; | filter and search all room listings from the admin page |
| &check; | easily navigate the admin panel, view, search, add, and delete room listing |
| &check; | approve new room listings offered by users, ensure listings are accurate and suitable |
| &check; | access a list of pending room listings |
| &check; | reject room listings that do not meet the platform's standards |
| &check; | utilize a text editor within the admin panel |
|    ?    | receive notifications when a room is rented |

**As a User offering a room ....**

| Status  | Feature |                                                                           
|:-------:|:--------|
| &check; | create an account |       
| &check; | access the platform's features |
| &check; | easily create a listing for a room I have available for rent, providing all necessary details and photos |
|    ?    | receive an alert, so be nformed when my post has been submitted for review  |
| &check; | manage my room listings, including editing or deleting them as needed |
| &check; | receive notifications when someone contacts me regarding my room listing |
| &check; | easily find relevant contact information, contact the site administrator via email |

**As a User searching a room ....**

| Status  | Feature |                                                                           
|:-------:|:--------|
| &check; | create an account |       
| &check; | access the platform's features |
|    ?    | search for available rooms based on my preferences (location, price, type of room) |
| &check; | receive an alert, so be nformed when my post has been submitted for review  |
| &check; | view detailed information and photos of available rooms |
| &check; | get the contact details of the owner, such as email or phone |
| &check; | easily find relevant contact information, contact the site administrator via email |
| &check; | access the platform from any screen size and still have a good browsing experience |


**Manual Testing features**

| Status  | Feature |
| &check; | Homepage|                                                                             
|:-------:|:--------|
| &check; | Easy Navigation on the Navbar Links |       
| &check; | Visual Information, such as Images |
| &check; | Easy Identification of the Searched Content on the Page |
| &check; | Informative Indication of User Authentication Status |


| Status  | Feature  |
| &check; | Add room |                                                                             
|:-------:|:--------|
| &check; | Simple and Descriptive Form |       
| &check; | Icons Associated with Each Input |
| &check; | Ability to Upload Photos |
| &check; | Error Messages for Incorrect Field Entries |
| &check; | An informative button for form submission. |
| &check; | Receive a message confirming that my form has been submitted after sending it. |


| Status  | Feature  |
| &check; | Room Finder |                                                                             
|:-------:|:--------|
| &check; | Easy visualization of each advertisement (card) |       
| &check; | Essential information displayed clearly for choosing my room. |
| &check; | Delete button available if I want to remove any of my posts.|
| &check; | Edit button provided if I need to correct any information.|
| &check; | Contact information available for the owner of the advertisement |
| &check; | Have a confirmation prompt when pressing the delete button to prevent accidental deletion. |


| Status  | Feature  |
| &check; | Contact |                                                                             
|:-------:|:--------|
| &check; | Easy location of telephone number if I want to speak with the site administrator. |       
| &check; | Easy location of email if I want to send a message to the site administrator. |
| &check; | Ability to Upload Photos. |
| &check; | Links to social media profiles. |

## Bugs


**Issue** - The image thumbnails were not displaying correctly on the room detail page.

- Cause - Initially, I suspected an issue with the image file paths. However, upon closer inspection, I discovered that the Cloudinary URLs were not being rendered properly due to a missing attribute in the template.

- Solution - Adding the .url attribute to the image reference in the template resolved the issue, ensuring that the correct Cloudinary URLs were generated and displayed.

**Issue** - Was encountering errors when uploading room images, with the images failing to display after the upload process.

- Cause - After investigating, find out that the Cloudinary upload preset configured in the frontend did not match the preset specified in the backend settings, causing the upload process to fail.

- Solution - Aligning the Cloudinary upload preset settings between the frontend and backend resolved the issue, ensuring that images were uploaded successfully and displayed correctly after the upload process.

**Issue** - The footer section of the website was not staying fixed at the bottom of the page, causing it to overlap with the content on certain pages.

- Cause - Upon inspection of the CSS styles, it was found that the footer did not have the appropriate positioning properties to keep it fixed at the bottom of the page.

- Solution - By applying the CSS property position: fixed to the footer element and setting bottom: 0, the footer was successfully fixed at the bottom of the page, resolving the overlapping issue.

**Issue** - I encountered an issue during deployment where images and some static files were not being uploaded properly to Heroku, resulting in discrepancies between the production and preview versions of the site.

- Cause - After seeking assistance from the course tutor, it was suggested that there might be a conflict between Whitenoise and Cloudinary. Upon investigation, I removed the line of code STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' from the settings file. This initially resolved the issue, and the images started uploading correctly during deployment on Heroku. However, after two days, the problem resurfaced, and no files were being uploaded again.

- Solution - Upon further consultation with the tutor, it was recommended to add STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage' to the settings file. After adding this line and running python3 manage.py collectstatic, all static files, including images, were successfully uploaded during deployment, ensuring consistency between the deployed version and the preview.


**Issue** - I encountered an error in the console when clicking the edit button. The error message displayed is: [](docs/images/error.png)

- Cause - The main issue seems to originate from the file "script.66f705e79209.js" at line 9, column 21. This indicates an attempt to access a file in the staticfiles directory. However, even after running the command python3 manage.py collectstatic and making changes to my script, the file does not update, preventing access.

- Status - As of now, the error remains unresolved. Despite the error, the edit functionality seems to be working fine, as I can open the modal and edit the content successfully. However, the presence of this error in the console is concerning.

*Note: Due to the tight deadline for the project delivery tomorrow, it was decided to leave the issue as it is, as all other functionalities are working as expected. Further investigation may be required after the deadline.*


## Deployment

This website is deployed to Heroku from a GitHub repository, the following steps were taken:

**Setting up a GitHub Repository**
- To begin, ensure that you're logged into GitHub and navigate to the Code Institute's template.
- Select "Use this template" and opt to "Create a new repository" from the dropdown menu.
- Provide a name for the repository and hit "Create repository from template."
- Upon successful creation of the repository, I utilized the green Gitpod button to establish a workspace in Gitpod, facilitating the coding process for the site.

**Creating an Application on Heroku**
- Following the setup of the GitHub repository, proceed to Heroku and log in to your account.
- Once logged in, navigate to the home page and click on "New," then select "Create new app" from the dropdown menu.
- Assign a unique name to your app and select a region—I opted for Europe since I reside there.
- Finally, click "Create app" to complete the process.

**Setting up a Database on ElephantSQL**
- Begin by logging into the ElephantSQL website and navigate to the dashboard.
- Click on "Create new Instance" to initiate the database creation process.
- Provide a distinctive Name for your instance and ensure the plan is set to "Tiny Turtle Free." The tags field can be left blank.
- Select a region closest to your location.
- Proceed to review your settings and click "Create instance" to finalize the setup.
- Once the instance is created, navigate to the dashboard and locate your database instance name.
- Access the details of your database instance, and in the URL section, click on the copy icon to copy the database URL.
- Switch back to Gitpod and navigate to your project's env.py file.
- Create a new environment variable named "DATABASE_URL" and paste the copied URL as its value. This will ensure your application can connect to the database seamlessly.


**Deploying to Heroku**

- Return to the Heroku dashboard and select your app. Then, navigate to the Settings tab.
- In the Settings page, scroll down to the "Config Vars" section. Here, you'll need to set up several environment variables:
- Set DATABASE_URL to the ElephantSQL URL.
- Create a SECRET_KEY; this can be any secure string.
- Set CLOUDINARY_URL to your Cloudinary URL.
- Finally, set the PORT variable to 8000.
- After configuring the environment variables, scroll to the top of the page and switch to the Deploy tab.
- n the Deployment method section, choose GitHub and sign in to your GitHub account if prompted.
- In the "Search for a repository to connect to" box, enter the name of your GitHub repository and click "Connect."
- Once the repository is connected, scroll down to the Manual Deploy section and click "Deploy Branch."
- After the deployment process is complete, you'll see a "View App" button below. Click on it to access your newly deployed app.

## Credits

- Balsamiq: Used for creating wireframes.
- GitHub: Store my repository.
- Font Awesome: A library of icons and symbols used for the webpage.
- Google Fonts: Imported fonts for the website.
- Paint: Used to edit screenshots and convert image extensions for the readme file.
- Chrome Dev Tools: Frequently used to experiment with code and preview on different screens.
- TinyPNG: Used for compressing and optimizing images to improve performance.
- Simple Image Resizer: Used for resizing images.
- Unicorn Revealer: Chrome extension for debugging layout issues and visualizing hidden properties on webpages.
- coolers.co: Color schema
- Django documentation
- Bootstrap documentation


## Acknowledgment

- I would like to give a huge shoutout to my mentor, David Bowers, for his amazing feedback and guidance. Thanks a bunch for all the help, feedback, and encouragement along the way

- I'd like to extend a heartfelt thank you to the course's tutoring channel. Their professionalism, attention, and patience always come through, especially during those panic-inducing moments. A special shoutout to Tutor Tomas, who helped me out when I felt stuck and couldn't see a way forward.

- To the entire Slack community, across its various channels, thank you for your unwavering support throughout the course. A special shoutout goes to Marko_ci, my course cohort, who consistently shared helpful resources and messages that greatly contributed to the completion of this project. I'm truly grateful for it!


