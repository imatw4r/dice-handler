# Introduction

Your new D&D game just arrived!

You have opened a box, take out everything and there is no dice included, what the heck is going on...

No worries. As an `experienced software developer` you can design your own dice roller, right?

Of course, to be more useable it should be `web based`, in form of `browsable REST API`.

Let's get to work.

---

## Models

Dice roller should be simple but functional.
For sure we need a `Dice` and `DiceHandle` to roll a set of dice.

### Dice

`Dice` should have some number of `faces` and `name`. When we `roll` that `dice` it should return `value` between `1` and the numeber of `faces`.

In terms of REST API what is expected:


    GET /dice/

    {
        "count": 3,
        "next": "http://0.0.0.0/dice/?page=2",
        "previous": null,
        "results": [
            {
                "created": "2020-12-09T23:21:45.849271Z",
                "faces": 6,
                "name": "D6",
                "roll": 3,
                "updated": "2020-12-09T23:21:45.849315Z",
                "url": "http://0.0.0.0/dice/5/"
            },
            {
                "created": "2020-12-10T10:58:22.271070Z",
                "faces": 6,
                "name": "D6",
                "roll": 4,
                "updated": "2020-12-10T10:58:22.271144Z",
                "url": "http://0.0.0.0/dice/6/"
            }
        ]
    }


and for individual `dice`


    GET /dice/5/

    {
        "created": "2020-12-09T23:21:45.849271Z",
        "faces": 6,
        "name": "D6",
        "roll": 5,
        "updated": "2020-12-09T23:21:45.849315Z",
        "url": "http://0.0.0.0/dice/5/"
    }


---

### Dice handle

`DiceHandle` should have some number of `dice` and `name`. When we `roll` that `dicehandle` it should return `value` representing a sum of rolls of each `dice` in that `dicehandle`.

In terms of REST API what is expected:


    GET /dicehandle/

    {
        "count": 2,
        "next": null,
        "previous": null,
        "results": [
            {
                "created": "2020-12-09T23:24:55.783012Z",
                "dice": [
                    "http://0.0.0.0/dice/5/",
                    "http://0.0.0.0/dice/2/"
                ],
                "name": "Dice handle D6 + D10",
                "roll": 4,
                "updated": "2020-12-09T23:25:25.222438Z",
                "url": "http://0.0.0.0/dicehandle/1/"
            },
            {
                "created": "2020-12-10T14:08:24.740813Z",
                "dice": [],
                "name": "Dice handle",
                "roll": 0,
                "updated": "2020-12-10T14:08:24.740873Z",
                "url": "http://0.0.0.0/dicehandle/2/"
            }
        ]
    }


and for individual `dice handle`


    GET /dicehandle/1/

    {
        "created": "2020-12-09T23:24:55.783012Z",
        "dice": [
            "http://0.0.0.0/dice/5/",
            "http://0.0.0.0/dice/2/"
        ],
        "name": "Dice handle D6 + D10",
        "roll": 11,
        "updated": "2020-12-09T23:25:25.222438Z",
        "url": "http://0.0.0.0/dicehandle/1/"
    }


---

# Outro

After a few hours your new shiny `dice roller` is ready and you can start palying. Yay!!!

What is more important, now we can play with your `dice roller`, too ;)

---

# Guidelines

 - use `Python 3.8` or newer
 - use `Django` & `DRF` - don't reinvent a wheel ;)
 - if you think that another framework is perfect tool for this job - use it
 - follow Python standards and good practices
 - remember to implement `unit` and `integration tests` for any code you write (`pytest` is recommended)
 - check your code with `flake8` before submitting the solution
 - include a `README.md` file with instructions for running the application and its tests
 - please use `Docker` and `docker-compose`
 - if you can point us to your solution deployed directly from git repository to one of cloud services it will be awsome


---
# E2E tests

 Check if your solution meets our basic expectations of correctness with included `docker-compose.yml` file.
 Just put your solution in expected folder or provide Docker image build by you.
 E2E test results will land in `./results` folder.

 Start E2E test with
    
    docker-compose up --build

