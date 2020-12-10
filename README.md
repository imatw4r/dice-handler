# Introduction

Your new D&D game just arrived!

You have opened a box, take out everything and there is no dice included, what a boomer...

No worries. As an `experienced software developer` you can design your own dice manager, right?

Of course, to be more useable it should be `web based`, in form of `REST API`.

Let's get to work.

---

## Models

Dice manager should be simple but functional.
For sure we need a `Dice` and `Handle` to roll a set of dice.

### Dice

`Dice` should have some number of `faces` and `name`. When we `roll` that `dice` it should return `value` between `1` and the numeber of `faces`.

In terms of REST API what is expected:

```
POST /dice
{
    "name": "D6",
    "faces": 6
}

ANSWER:
{
    "id" : "id-of-a-dice"
}
```

```
GET /dice/%id

ANSWER:
{
    "name": "D6",
    "faces": 6,
    "roll": 4
}
```

```
GET /dice

ANSWER:
{
    dice: [
        {
            "id": 1,
            "name": "D6",
            "faces": 6
        },
        {
            "id": 2,
            "name": "D4",
            "faces": 4
        }
    ]
}
```

```
DELETE /dice/%id
```

---

### Handle

`Handle` should have some number of `dice` and `name`. When we `roll` that `handle` it should return `value` representing a sum of rolls of each `dice` in that `handle`.

In terms of REST API what is expected:


```
POST /handle
{
    "name": "D&D",
    "set": [
        "id-of-dice",
        "another-id-of-dice",
        "id-of-not-existing-dice"
    ]
}

ANSWER:
{
    "id" : "id-of-a-handle"
}
```

```
GET /handle/%id

ANSWER:
{
    "name": "D&D",
    "roll": 4,
    "set": [
        "id-of-dice",
        "another-id-of-dice"
    ]
}
```

```
GET /handle

ANSWER:
{
    handle: [
        {
            "id": 1,
            "name": "D&D"
        },
        {
            "id": 2,
            "name": "Another handle name"
        }
    ]
}
```

```
DELETE /handle/%id
```

---

# Outro

After a few hours your new shiny `dice manager` is ready and you can start palying. Yay!!!

What is more important, now we can play with your `dice manager`, too ;)

---

# Guidelines

 - use `Python 3.8` or newer
 - use `Django` & `DRF` - don't reinvent wheel ;)
 - follow Python standards and good practices
 - remember to implement `unit` and `integration tests` for any code you write (`pytest` is recommended)
 - check your code with `flake8` before submitting the solution
 - include a `README.md` file with instructions for running the application and its tests
 - please use `Docker` and `docker-compose`
 - check if your solution meets our basic expectations of correctness with included `e2e-docker-compose.yaml` file
