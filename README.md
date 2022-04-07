# DevOps Core Practical Project Specification

The aim of this project was to create a service-orientated architecture composed of at least 4 services that work together. These services include a front-end which renders a web page for users to interact with my application, that communicates with the other 3 services, and persists data in an SQL database. Service 2 and 3 produce randomly generated objects that are then used to create the final output for the user in service 4, which is subsequently displayed on the front end.


## Prize Generator:

My application generates a random letter combination within service 2, and a random 4 digit number within service 3 , which is then subsequently sent to service 4 by service 1, where service 4 then generates a 7 digit account number, as well as a prize generated upon certain rules. The rules that I have set is that individuals with an even number get no prize, whereas those with odd numbers do. The size of the prize is then determined by the letter combination that you received.

A screenshot of the application is shown below:


## Database:
<img width="274" alt="Table" src="https://user-images.githubusercontent.com/99325840/161989861-13b2f216-1eff-4f7c-ac4f-f6148affecbf.png">

My database had a single table, with three different fields:
-  Primary Key : which is a number which allow us to uniquely identify records from one another
-  Account Number
-  Prize

<img width="470" alt="Screenshot 2022-04-06 at 14 36 30" src="https://user-images.githubusercontent.com/99325840/161987468-f668736b-b922-42fd-85b8-dad29a634312.png">


## Planning:

On the first day of my project, I made a kanban style board on Jira software. This visually depicts my workload and allows me to keep track of what has already been done and what is to do. I have split my ToDos into several sections. The first were the minimum viable product requirements that were needed for me to pass the project. I wanted these separate as they were the most important tasks for me to consider. I also had User Stories, which helped me build my application by thinking in the eyes of the end user. I also had 'in progress' and 'done' sections for recording my progress as time went on.

# Day 1:

<img width="1411" alt="Jira NOT DONE" src="https://user-images.githubusercontent.com/99325840/161988535-c5addf3d-820e-40e3-8137-0826c06331e5.png">

# Final Day:
<img width="1440" alt="Jira Done" src="https://user-images.githubusercontent.com/99325840/162045968-47a345a5-4590-46ae-befb-a57916bb8a5a.png">



## Risk Assessment:

A risk assessment is where you identify and analyze potential events that may negatively impact users, the application, and/or the environment; and make a judgment on the risk level, the tolerability of the risk and potential prevention methods to combat this risk. Below is my risk assessment for my project:

<img width="608" alt="risk assessment" src="https://user-images.githubusercontent.com/99325840/161993129-546d99c9-f8b3-47b3-84a4-f9608b36d04c.png">

## CI/CD Pipeline:

Continuous Integration refers to the automated integration of code into a software project. It allowed me to generate and implement new functionality with ease as building and testing is handled through automation.
Some of the benefits of employing a CI pipeline to a production workflow are:
- It reduces the money and time that is spent by manually building, testing, and deploying code. 
- Using a VCS increases transparency between teams as all changes are easily trackable and attributable to the individual that made them. Teams are therefore more aware of each other's progress.
 
Continuous delivery is an extension CI that seeks to deliver new features to customers on a regular basis. So while CI integrates code regularly, continuous delivery delivers that code regularly.
-This allows for more user feedback as development teams can now show off new product features much more frequently, allowing them to adjust their product accordingly and thus producing better products for the consumers

In order to implement my pipeline, I used a CI server called Jenkins. The tasks that it automated for me were:
-Testing: All tests are carried out and reports archived for viewing. 
- Building and pushing images: Docker credentials are uploaded from Jenkins, which are then used to push the images of the services once they are built      - Deploy Stack: This starts NGINX, initializes the Docker Swarm and adds the managers and worker nodes. The stack is deployed with a Docker-Compose file. 

<img width="1269" alt="Screenshot 2022-04-06 at 17 38 47" src="https://user-images.githubusercontent.com/99325840/162024790-0af303ed-76aa-4d12-b27b-7dca5a804c7e.png">


## Technologies:

<img width="611" alt="pipeline" src="https://user-images.githubusercontent.com/99325840/162045822-7ee15cab-5ed8-42f3-bbf6-4330fbd7fc1f.png">


<img width="656" alt="Screenshot 2022-04-06 at 19 41 12" src="https://user-images.githubusercontent.com/99325840/162045793-96b42d2d-e423-479d-9e8d-c3035fe21320.png">

# Ansible:
Ansible is a software used to configure and spin up multiple nodes at any given time. Ansible was used to set up  environments with the necessary dependencies, such as python, NGINX and Docker by temporarily connecting remotely via SSH into virtual machines and running a set of predefined ‘plays’. Evidence of usage is shown below:

<img width="865" alt="Screenshot 2022-04-07 at 14 08 13" src="https://user-images.githubusercontent.com/99325840/162206142-14e1e4e3-39f8-4c70-83e8-7f92d8d857b8.png">

<img width="1440" alt="Screenshot 2022-04-05 at 17 33 04" src="https://user-images.githubusercontent.com/99325840/162205986-f5e69cb1-9402-4f27-8833-6243c034b795.png">

<img width="1142" alt="Screenshot 2022-04-06 at 14 37 42" src="https://user-images.githubusercontent.com/99325840/162206177-de200946-f607-42f3-a789-c10274174725.png">


## Testing:
Service1:
For my front-end tests, I wanted to ensure that a 7 digit account number is displayed on the homepage, alongside the corrosponding prize. This was high priority as the users must be able to see this information.
<img width="1111" alt="Screenshot 2022-04-07 at 14 17 06" src="https://user-images.githubusercontent.com/99325840/162208164-443db911-fc4f-45f7-92e1-d71f62a45947.png">

Service2:
For my letter generating service, I wanted to assert that a specific combination was within the response data. This was high priority as the letters generated determine whether a user wins a prize or not.

<img width="1093" alt="Screenshot 2022-04-07 at 14 17 46" src="https://user-images.githubusercontent.com/99325840/162208232-24839c22-d387-4bc2-88a0-8d02aecd55e0.png">

Service3:
For my number generating service, I wanted to assert that a certain random number between 1000 and 9999 was within the response data. This was high priority as the number generated determine how large the prize recieved is, on the condition that theyre eligible for one.

<img width="1073" alt="Screenshot 2022-04-07 at 14 18 15" src="https://user-images.githubusercontent.com/99325840/162208253-5738159e-d314-4de9-88a1-15d7be75f6f6.png">

Service4:
In my prize determining service, I tested every possible prize that could be won by a user was possible, along with one test case for a user who doesnt win a prize. Unfortunately, however, I could not recieve 100% coverage as certain conditionals wernt are never run in the tests. As this was also high priority to test, I have manually tested my app and have seen every possible prize that could be won by constantly refreshing the app. Once I saw every possible outcome, I knew that I had an issue with my test and not my application. 

<img width="1082" alt="Screenshot 2022-04-07 at 14 18 41" src="https://user-images.githubusercontent.com/99325840/162208273-e1955bc9-4727-48c6-8e62-ed35707040bd.png">






 



