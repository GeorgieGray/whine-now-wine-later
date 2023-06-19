# Whine now, Wine later

[Whine now, Wine later](https://wnwl-4c7773784ff4.herokuapp.com/) is a female only gym.

Female fitness enthusiasts of any age are given the opportunity to join a female led gym and join a community of like minded women. Users of the website can purchase memberships which can be used to attend personal , semi personal and strength training classes. A time and day can be selected for the class once logged in. 

The web application frontend has four high-level views:
- User login/registration
- Memberships
- Sessions
- Mailing list

The website is hosted using Heroku, see it here:  
https://wnwl-4c7773784ff4.herokuapp.com/

## Target Demographic
- Women looking to get fit in a comfortable environment 
- Women who are fed up of men hogging the squat racks in regular gyms
- Women looking to join a community and make friends
- People who are interested in newsletters relating to fitness, healthy eating and wellbeing suggestions
- Women who would usually feel out of their depth in a non training gym
- Women who are looking for advice on a healthy lifestyle

## Project planning
This section discusses my approach to thinking about and designing the system. The diagrams I created are mostly accurate to the final system, some small changes were made as I made further discoveries during development.

## Project management
- See [Github Project](https://github.com/GeorgieGray?tab=projects)

## Features
### Landing view
The welcome view. This is the start of the users journey.

Once the user has registered and is logged in, they're no longer shown the registration controls.

### User registration
A form to collect the users information and allow them to create an account. Once they've successfully submit the form they're automatically logged in and taken to the membership view.

### User login
A form to allow the user to log in if they already have an account. On successful login they're given the option to plan sessions and see upcoming sessions. 

### Mailing List
Users are given the option to opt in or out of a newsletter subscripton. 

### View memberships
Users of the site can view what memberships are available to purchase.

### Checkout
Users can purchase a selected membership which will direct them through a checkout process. 

### View upcoming classes
See your planned workout sessions, or create one.

### Edit/cancel a class
Make amendments to your previously planned sessions.

## Technology

- Python 3
- Green Unicorn
- Python DotEnv
- Bootstrap 5
- PostgreSQL

## Local Development

Install dependencies
> pip install -r requirements.txt

Run django app
> python manage.py runserver

## Testing
During development I performed a smoke test using the following steps, it touches on all major parts of the application.

- Register
- Log in
- Go to newsletter
- Submit newsletter subscription
- Unsubscribe from newsletter
- Go to session planner
- Create session
- Edit session
- Delete session
- Go to memberships
- Choose plan
- BUY NOW
- Navigate to stripe
- Complete form
    - email: any (no email is sent)
    - card number: `4242 4242 4242 4242`
    - card expiry: any date in the future
    - card cvc: any three digit number
    - Name on card: any name
- Pay
- See navigate to success view
- Log out
- See that logged in/logged out only content is available depending on login state
- Check cannot see other users planned sessions
- Check that cannot access views which require login

## Deployment
The app is deployed to Heroku.

Here are some instructions so you can do it yourself:
1. Create an account on Heroku
2. "New" in the top right corner of dashboard > create new app
3. Install the [heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
4. Authenticate with the CLI: `heroku login`
5. Follow the [Deploying with Git](https://devcenter.heroku.com/articles/git) instructions to setup your git repo correctly to speak with Heroku.
6. Set the env variables: settings > config vars (See: `env.example` in src code)
6. When you're ready to deploy: `git push heroku main`