
# Crystal Dent
![Screenshot 2024-08-01 at 21 46 04](https://github.com/user-attachments/assets/531f7b45-80d4-4641-8fab-30771166d040)
Welcome to **Crystal Dent**, a comprehensive web application designed to offer an exceptional dental service experience. This project aims to provide users with easy access to various dental services, enabling them to book appointments and leave reviews about their experiences.

# Modern list Design with Animation
![Screenshot 2024-08-01 at 21 47 10](https://github.com/user-attachments/assets/60ec8dc3-0b2b-4912-9e23-1cd551b44b88)
    •	Enhanced User Engagement: The combination of animations and striking visuals captures user attention, encouraging them to explore further and interact with the site.

# Booking Section 
![Screenshot 2024-08-01 at 21 47 33](https://github.com/user-attachments/assets/fa8d9449-3cbf-4af1-bf62-a71f504ec945)

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


