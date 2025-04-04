![Build Badge](https://github.com/software-students-spring2025/3-python-package-jeff-bezos/actions/workflows/build.yml/badge.svg?event=pull_request)

# Code Procrastinator

**Code Procrastinator** is a Python package that humanizes your code by giving it the ability to procrastinate—just like you! :D

Instead of executing tasks efficiently, it gets _distracted_, mindlessly browses the internet, or justifies its procrastination with excuses.

[PyPI Link](https://pypi.org/project/code-procrastinator/)

---

## Team Members

[Bryant To](https://github.com/bryantto08)
[Andrew Bao](https://github.com/andrew-bao)
[Jasmine Zhang](https://github.com/Jasminezhang666666)
[Imran Ahmed](https://github.com/mxa5251)

---

## **Installation**

You can install **Code Procrastinator** from **PyPI** using `pip`:
This package requires Python 3.7 or higher

```sh
pip install code-procrastinator
```

## **Contributing**

Want to improve **Code Procrastinator?** Follow these steps to set up your development environment!

### **Clone Repository**

```sh
git clone https://github.com/software-students-spring2025/3-python-package-jeff-bezos.git
cd 3-python-package-jeff-bezos
```

### **Create a Virtual Environment**

```sh
pip install pipenv
pipenv shell
```

### **Building**

We automatically upload our package to PyPi using twine.\
Before merging anything, ensure your contributions pass the unit tests

Important: PyPI will not let you upload a duplicate version, make sure to increment your version in your pyproject.toml file before pushing any changes. (Ex: 0.1.6 -> 0.1.7)

```sh
pytest procrastinator.py
```

## **Procrastinate()**

The `procrastinate` function simulates what a human might do when procrastinating—whether it's scrolling the web, making excuses, or delaying execution.

### **Usage**

To use Code Procrastinator in your own Python projects, simply import and call the procrastinate function:

```python
from code_procrastinator import procrastinate

# Make your program procrastinate for up to 10 seconds, with 3 random delays
procrastinate(10, 3)
```

### **Function Behavior**

- Randomly selects a number of **unique delays** between `0` and `max_time`.
- After each delay, it executes a **random procrastination action**.
- Available actions include:
  - Printing **excuses for procrastination**.
  - Opening a **fun website** for distraction.

### **Arguments**

| Argument      | Type  | Description                                                            |
| ------------- | ----- | ---------------------------------------------------------------------- |
| `max_time`    | `int` | The maximum number of seconds for any delay. Must be greater than `0`. |
| `delay_count` | `int` | The number of procrastination delays. Must be greater than `0`.        |

### **Exceptions**

- **`ValueError`**: Raised if `max_time` or `delay_count` is less than or equal to `0`.

### **Return Value**

- **`set`**: A set of unique delay times used during procrastination.

---

## **Example Usage**

```python
>>> procrastinate(10, 3)
Procrastinating...
Let's take an internet break! :D https://en.wikipedia.org/wiki/Special:Random
Procrastinating...
Wow, this 4-hour video essay looks interesting...
Procrastinating...
I'll do it tomorrow
```

## **excuse_wrapper()**

The `excuse_wrapper` function will also procrasinate on providing correct output, will relay an excuse, and has a chance to completely fail on the task.

### **Usage**

Import excuse_wrapper, and use it as a decorator for the original function

```python
from code_procrastinator import excuse_wrapper
@procrastinator.excuse_wrapper
def add(x, y):
    return x + y
add(1, 2)
```

## **Example Usage**

```python
>>> add(1. 2)
Optimizing best possible answer
Processing... 25% done.
Still thinking... 50% done.
Someone just deleted my work... I need to start over again...
TBH... forget this I'll do it tomorrow.
```

## **reaffirm_program()**

The `reaffirm_program` function checks if the input message contains any positive keywords. When it detects encouragement, it prints a motivational message and confirms that the program is ready to continue running. This function is useful when you want your application to "get back on track" after a period of procrastination.

**Example Usage**

```python
from code_procrastinator import reaffirm_program

# Provide a message with positive keywords to trigger the function
result = reaffirm_program("You're awesome and brilliant!")
print(result)  # Expected output: "Program is now running! Let's do this!"
```
### **Function Behavior**
- **Positive Check**: Scans the input message for predefined positive keywords (e.g., "awesome", "fantastic", "great").
- **Encouragement**: If a positive keyword is found, it prints a random motivational message from a set of positive responses.
- **Confirmation**: Returns the string "Program is now running! Let's do this!" to signal that the program can proceed.
- **Default Behavior**: If no positive keywords are detected, it prints a default message requesting encouragement and returns None.

### **Arguments**

| Argument      | Type  | Description                                                            |
| ------------- | ----- | ---------------------------------------------------------------------- |
| `message`     | `str`  | The input message which is checked for positive keywords.             |

### **Return Value**
- **`str`**: Returns "Program is now running! Let's do this!" if the input contains positive keywords.
- **`None`**:Returns None if no positive keywords are found.


## **random_fail_wrapper()**

The `random_fail_wrapper` function decorator randomly determines whether the decorated function will execute normally or fail by raising an `IllDoItLaterException`. In both cases, a randomly chosen message prints to the console

### **Usage**

Import `random_fail_wrapper` from **Code Procrastinator**

```python
from code_procrastinator import random_fail_wrapper

@random_fail_wrapper
def compute_sum(a, b):
    return a + b

compute_sum(3, 4)
```

### **Function Behavior**

- **Random Check**: Generates a random number between 1 and 100.
- **Failure Path**: If the number is less than 50, it raises an IllDoItLaterException with a randomly selected excuse.
- **Success Path**: Otherwise, it prints a message from RUN_MESSAGE and executes the function, returning its result.

### **Exceptions**

- **`IllDoItLaterException`**: Raised if the randomly generated number is between 1 and 50.

### **Return Value**

- **`wrapper`**: A wrapper of the original function with the additional random failure "functionality"

---

## **Example Output**

- **Successful Execution**

```python
>>> compute_sum(3, 4)
Ugh, I guess I'll run this now.
7
```

- **Failure (Exception Raised)**

```python
>>> compute_sum(3, 4)
IllDoItLaterException: Oh wait, I left my oven running. Sorry, but I cant run this code right now, I have to go...
```
