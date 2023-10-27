<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/SheCodesAus/layer_8_victory_backend_bris_2023">
    <img src="https://raw.githubusercontent.com/SheCodesAus/layer_8_victory_frontend_bris_2023/main/public/1.png" alt="Logo" width="300" height="300">
  </a>

<h3 align="center">MentorShip</h3>

  <p align="center">
  MentorShip connects professionals in the technology industry with aspiring coders.
    <br />
    <a href="https://github.com/SheCodesAus/layer_8_victory_backend_bris_2023"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/SheCodesAus/layer_8_victory_backend_bris_2023">View Demo</a>
    ·
    <a href="https://github.com/SheCodesAus/layer_8_victory_backend_bris_2023/issues">Report Bug</a>
    ·
    <a href="https://github.com/SheCodesAus/layer_8_victory_backend_bris_2023/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
MentorShip’s purpose is to make finding and choosing mentors for She Codes workshops seamless.
This repository hosts the code for the back end of the website. You can find the front end repository [here][front-end-repo].
The deployed DRF project can be found [here](https://mentorship.fly.dev/events/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Django][Django.com]][Django-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.


### Prerequisites

* `python`
* `pip`
* unrestricted execution policy (Windows requirement)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/SheCodesAus/layer_8_victory_backend_bris_2023.git
   ```
2. Create the local environment
    ```sh
    python -m venv venv
    ```  
3. Activate the virtual environment
    
    - navigate to the folder that contains the `requirements.txt` file
      - If you're on a windows machine, run the command
   ```sh
   . venv/Scripts/activate
   ```
      - If you're on a linux machine, run the command
   ```sh
   source venv/bin/activate
   ```

4. Install the required libraries 
   ```sh
   python -m pip install -r requirements.txt
   ```

5. Make initial migrations 
   ```sh
   cd mentorship
   python manage.py migrate
   ```

6. Run the server
   ```sh
   python manage.py runserver
   ```

  - Use the url http://127.0.0.1:8000/, your favourite API Tool (e.g. Insomnia, Postman) and refer to the [API Specifications](#api-specification) to create HTTP requests
  - When you're finished press CTRL+C to quit the server
  - Deactivate the virtual environment by either using the command `deactivate` or terminate your terminal session.
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## API Specification

| HTTP Method | Url                  | Purpose                               | Request Body                    | Successful Response Code | Authentication <br /> Authorization                                                                                                                 |
| ----------- | -------------------- | ------------------------------------- | ------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| GET         | events/              | Return all events                     | N/A                             | 200                      | N/A to see published events. Must be authenticated as staff to see unpublished events                                                               |
| GET         | mentor-events/       | Return all mentor event registrations | N/A                             | 200                      | N/A to see confirmed records. Must be authenticated as staff to see all. Authenticated mentors can see their own records.                           |
| GET         | users/               | Return all users                      | N/A                             | 200                      | Bearer Token authentication. <br /> Staff user can view list of all users. Non staff user will only return own user object.                         |
| GET         | skills/              | Return all skills                     | N/A                             | 200                      | N/A                                                                                                                                                 |
| GET         | mentor-events/self   | Return records for own event registration records| N/A                  | 200                      | Bearer Token authentication.                                                                                                                        |
| POST        | events/              | Create a new event                    | event object                    | 201                      | Bearer Token authentication. <br /> Only available to staff users.                                                                                  |
| POST        | mentor-events/       | Register mentor against event         | event_id, mentor_id (mentor_id only required if request is made by staff user)| 201| Bearer Token authentication. <br /> Only available to users with onboarding_status of "Ready".                              |
| POST        | skills/              | Create a new skill                    | skill name                      | 201                      | Bearer Token authentication. <br /> Only available to staff users.                                                                                  |
| POST        | users/               | Create a new user                     | user object                     | 201                      | N/A for creating general mentors. Must be authenticated as a staff user if creating another staff user                                              |
| POST        | api-token-auth/      | Obtain Bearer Token for Authorisation | username and password           | 200                      | N/A                                                                                                                                                 |
| PUT         | events/< int:pk >/   | Update event                          | event object or event field     | 201                      | Bearer Token authentication. <br /> Only available to staff users.                                                                                  |
| PUT         | mentor-events/< int:pk >/| Update mentor-event record        | available and/or confirmed fields| 201                     | Bearer Token authentication. <br /> Mentors can update the available field of own record only. Staff users can update both fields for any record.   |
| PUT         | users/< int:pk >/    | Update user                           | user object or user field       | 201                      | Bearer Token authentication. <br /> Mentors can update the available field of own record only. Staff users can update both fields for any record.   |


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Mentorship was created by 
- Andrea del Pilar Rivera Peña
- Jenny Waller
- Maya Dominice
- Oriyan Nadav
- Rosie Maguire

If you would like to get in contact with the application creators, you can do so by emailing mentorshiplayer8@gmail.com

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/SheCodesAus/layer_8_victory_backend_bris_2023.svg?style=for-the-badge
[contributors-url]: https://github.com/SheCodesAus/layer_8_victory_backend_bris_2023/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/SheCodesAus/layer_8_victory_backend_bris_2023.svg?style=for-the-badge
[forks-url]: https://github.com/SheCodesAus/layer_8_victory_backend_bris_2023/network/members
[stars-shield]: https://img.shields.io/github/stars/SheCodesAus/layer_8_victory_backend_bris_2023.svg?style=for-the-badge
[stars-url]: https://github.com/SheCodesAus/layer_8_victory_backend_bris_2023/stargazers
[issues-shield]: https://img.shields.io/github/issues/SheCodesAus/layer_8_victory_backend_bris_2023.svg?style=for-the-badge
[issues-url]: https://github.com/SheCodesAus/layer_8_victory_backend_bris_2023/issues
[product-screenshot]: https://raw.githubusercontent.com/SheCodesAus/layer_8_victory_frontend_bris_2023/main/public/1.png
[Django.com]: https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=Django&logoColor=WHITE&color=0B4B33
[Django-url]: https://www.djangoproject.com/
[front-end-repo]: https://github.com/SheCodesAus/layer_8_victory_frontend_bris_2023
