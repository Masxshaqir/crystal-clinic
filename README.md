
# Crystal Dent
![welcome](https://github.com/user-attachments/assets/26d9fd14-7c87-47b0-a76e-d368ebd748fe)

Welcome to **Crystal Dent**, a comprehensive web application designed to offer an exceptional dental service experience. This project aims to provide users with easy access to various dental services, enabling them to book appointments and leave reviews about their experiences.

# Modern list Design with Animation
![Screenshot from 2024-10-28 23-02-10](https://github.com/user-attachments/assets/c658b0a7-7672-437c-a3aa-ff46a1d931ae)

    •	Enhanced User Engagement: The combination of animations and striking visuals captures user attention, encouraging them to explore further and interact with the site.

# Booking Section 
![Screenshot from 2024-10-28 23-02-43](https://github.com/user-attachments/assets/33c1f5d5-c6e3-477a-a6fd-c1c72de43ea8)


# Show all Appointments Section 
![Screenshot from 2024-08-06 23-27-07](https://github.com/user-attachments/assets/d7e7ae94-b844-473c-8dbb-4198ccfe8d1b)

# Edit Appointments Section 
![Screenshot from 2024-08-06 23-27-26](https://github.com/user-attachments/assets/c7acf767-6401-4496-9683-9efbfd0d495a)

## Features

- Form Structure: The form is structured using HTML form tags and includes input fields for user

### Input Fields: The form contains the following fields:
- Name: A text input for the user’s full name.
- Email: An email input to capture the user’s email address.
- Phone: A text input formatted to accept a 10-15 digit phone number.
- Date: A date input allowing users to select their preferred appointment date.
- Time: A time input for selecting the preferred time slot.



## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)

## Features

- **Responsive Design**: The application is fully responsive and works on various devices, ensuring a seamless user experience.
- **Dynamic Content**: Features such as dynamic navigation and background image slider for the hero section.
- **Service Listing**: Users can view a list of dental services, including General Dentistry, Orthodontics, Periodontics, Oral Surgery, and Cosmetic Dentistry.
- **Reviews Section**: Patients can read reviews and share their experiences.
- **Appointment Booking**: A booking form is available for scheduling dental appointments, complete with a confirmation modal.
- **User show all upcomming Appointments**: An interactive section where users can view all his upcomming Appointment.
- **User Edit Appointment**: An interactive section where users can Edit on his submitted Appointment.
- **User delete Appointment**: An interactive section where users can delete his submitted Appointment.
- **Double Booking Prevention**: The system is developed to avoid double booking by ensuring that no two appointments are scheduled at the same time.
- **Instant Confirmation**: After booking an appointment, the client will see a popup message confirming the appointment and will receive an email with the appointment details.
- **Admin Panel Access**: Admins can access the admin panel using a username and password to manage data, including services, appointments, and user feedback.
- **User Comments**: An interactive section where users can leave and read comments about their experiences.
  

 ### Usage

	1.	Explore Services: Navigate through the website to explore services, read reviews, and book appointments.
	2.	Book an Appointment: Use the booking form by selecting your preferred date and time.
	3.	Receive Confirmation: Get a popup message and an email with the appointment details upon successful booking.
	4.	Leave a Review: Share your experience with other patients.
	5.	Admin Panel Management: Admins can log into the admin panel to manage services, appointments, and user feedback.


## Installation

### Prerequisites

- Python 3.x
- Node.js and npm
- Django

### Steps

  1. Clone the Repository

   ```bash
   git clone https://github.com/your-username/crystal-dent.git
   cd crystal-dent


	2.	Install Backend Dependencies
Install Python dependencies using pip:
pip install -r requirements.txt

	3.	Set Up the Database
Configure your PostgreSQL database and update the settings.py file accordingly.

	4.	Apply Migrations
Run the following command to apply migrations:

python manage.py migrate

	5.	Create a Superuser
To access the admin panel, you’ll need to create a superuser:

python manage.py createsuperuser

	6.	Run the Development Server
Start the Django development server:

python manage.py runserver

	7. Access the Admin Panel
Navigate to http://127.0.0.1:8000/admin and log in using the superuser credentials you created
```
## Databse Access
to access databse go to https://crystal-website-21a243b9531a.herokuapp.com/admin
and login with Email : admin@admin.com
	       password : admin

## Testing
This project includes both manual and automated testing to ensure reliable functionality and a smooth user experience for patients and staff.

- Unit Tests: Verify individual components and utility functions, like appointment scheduling and patient data handling.
- Integration Tests: Confirm interactions between modules, such as managing appointments, patient records, and notifications.
- End-to-End Tests: Simulate real user actions, like patient registration, booking an appointment, and receiving reminders.
- UI Tests: Ensure proper rendering and responsiveness across various devices.
- Performance Tests: Check load times and responsiveness, especially for viewing and managing appointments.
Manual Testing

- Basic Functionality: Register a new patient, log in, schedule appointments, and manage appointments.
- UI Responsiveness: Test adaptability of the interface on mobile, tablet, and desktop devices.
- Error Handling: Verify that appropriate error messages are shown for issues like missing required fields in booking.

## Admin Panel Access
to access databse go to https://crystal-website-21a243b9531a.herokuapp.com/admin
and login with Email : admin@admin.com
	       password : admin
	
### Deployment to Heroku
To deploy the application to Heroku, follow these steps:
1. **Prerequisites**
    - Ensure you have a Heroku account.
    - Ensure your project is hosted on GitHub.
2. **Steps**
   - Create a New Heroku App.
       Log in to your Heroku dashboard.
       Click on the New button in the top right corner and select Create New App.
       Provide a unique name for your app and choose a region. Click Create App.

   - Connect to GitHub Repository
       In your Heroku app dashboard, go to the Deploy tab.
       In the Deployment method section, select GitHub.
       Search for your repository by name and click Connect.

   
   - Enable Automatic Deploys (Optional)
       In the Deploy tab, you can enable Automatic Deploys from the GitHub branch of your choice. This will automatically deploy your app whenever you push changes to that branch.
       Alternatively, you can deploy manually by clicking Deploy Branch under the Manual Deploy section.

## Wireframes
![WhatsApp Image 2024-10-28 at 11 18 30 PM](https://github.com/user-attachments/assets/889ab41b-f42b-4fa0-8f3a-240ec7f65175)
![WhatsApp Image 2024-10-28 at 11 18 30 PM (1)](https://github.com/user-attachments/assets/196b06bc-5709-4b3c-a173-f5589938b35e)
![WhatsApp Image 2024-10-28 at 11 18 31 PM](https://github.com/user-attachments/assets/3a5a4752-db88-487b-83f4-6b5488a20545)
![WhatsApp Image 2024-10-28 at 11 18 31 PM (1)](https://github.com/user-attachments/assets/c9007d10-6054-44b9-8f93-21da9cdca179)
![WhatsApp Image 2024-10-28 at 11 18 31 PM (2)](https://github.com/user-attachments/assets/dcf45f27-0fdf-46fb-a4e4-768dde8e14fd)

