Field Reservation App

Welcome to the Field Reservation App! This application is designed to streamline the process of reserving sports fields, catering to both customers and field managers.

Technologies Used

Frontend: Built with Flutter and Dart for a responsive and seamless user experience across both Android and iOS devices.
Backend: Powered by Python Flask, ensuring a robust and secure server-side architecture.
Features

For Customers:
Field Reservation: Easily browse and reserve sports fields based on availability.
Favorites: Add your preferred fields to a favorites list for quick access.
Payment Management: Securely add and delete payment methods for seamless transactions.
Reservation Status: Track the status of your reservations in real time.

For Field Managers:
Field Management: Effortlessly add, edit, and delete field listings with all necessary details.
Reservation Handling: Approve or deny customer reservations with just a few clicks.
Reports: Access various reports to gain insights into field usage and reservations.
Field Parameters: Update field details, including name and available reservation times.

Additional Features:
Location Services: The app reads your current location and shows fields based on proximity.
Google Maps Integration: Navigate to fields and explore the surrounding area using the fully embedded Google Maps.
Google Sign-In: Easily sign in to your account using your Google credentials for a secure and streamlined experience.


Once the App Loads the user will have the option to allow access to the device's location or not 
![image](https://github.com/user-attachments/assets/90565f2f-2493-401f-8b05-38c144f2d299)

That is the Sign-In Page, which includes encryption of the user's password, Or the user can choose to log in with Google (fully working Google Sign-In Integration) 

![image](https://github.com/user-attachments/assets/aa56111f-6da3-4db7-93f7-f74c2c4be061)

 ![image](https://github.com/user-attachments/assets/7f4f7bbc-ac10-4658-9565-f499c163375a)

This is where the user chooses between the different Sports (Currently there is Football and tennis) You can also see the different tabs that the user can navigate to 

![image](https://github.com/user-attachments/assets/894d1eec-20cd-459e-8307-29a0a464b11a)

This user is presented with this page once he clicks one of the sport types (as you can see the fields are sorted according to the user's preferences and location (An Algorithm that is implemented in the back-end)

![image](https://github.com/user-attachments/assets/982f9b81-6102-4ca4-892c-9854bab0dd21)

The user can use many different filters 

![image](https://github.com/user-attachments/assets/45b9abd2-020e-4b9d-97bf-a6b8a783cdfc)

Users can search fields on the Map (Fully working GoogleMaps)
![image](https://github.com/user-attachments/assets/1f537303-30ad-4156-92e8-3e6d45ce2bd8)


After clicking the desired fields, the user will be presented with the following Page that includes details about the field and the Availability of the field itself
The user can add the field to their Favorites as well by clicking the Star Icon found on the top right corner 

![image](https://github.com/user-attachments/assets/a5385935-91cb-48cd-86b0-a6f5cf4d0b54)

![image](https://github.com/user-attachments/assets/34d0e032-31e4-42cc-aba7-8801216fa03c)

The availability of the field.
The user also can change the dates if the fields current date does not match his requirements

![image](https://github.com/user-attachments/assets/74868907-120e-403d-bd5f-af3d5f7d0abd)

![image](https://github.com/user-attachments/assets/2c5a85e6-08fd-44bc-96af-a27ce82447f4)

After clicking one of the available times the user will be navigated to the checkout page where he will be presented with all the reservation details as well as his payment method he currently has, by clicking on the payment method he will be able to remove the current payment method and add another one. 

![image](https://github.com/user-attachments/assets/5493d705-3bfa-4273-a2e4-c76b16c4acc2)

![image](https://github.com/user-attachments/assets/c8634bfe-4f4c-42ef-b47f-7b937f41e82f)

By swiping from right to left the user will be able to delete his payment method and add another one. 

![image](https://github.com/user-attachments/assets/6eac1114-b181-4955-b6fa-6a195b009fc5)

After clicking confirm the reservation will be booked and it will be in the Reservations in the pending section 

![image](https://github.com/user-attachments/assets/81295f36-1d23-407c-aa51-b0a0a30a1c8f)

The reservations Tab of the navigation bar 

<img width="378" alt="image" src="https://github.com/user-attachments/assets/848216bc-84d4-46fb-bddc-e5677dca5c22">

The user can edit his own Preferences because the Algorithm for finding the best fields takes into consideration the preferences of the user aswell 

![image](https://github.com/user-attachments/assets/d88728e9-e14d-431c-bd62-85383e8e2fe4)

