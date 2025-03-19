![Build Badge](https://github.com/software-students-spring2025/3-python-package-jeff-bezos/actions/workflows/build.yml/badge.svg?event=pull_request)

# Code Procrastinator

**Code Procrastinator** is a Python package that humanizes your code by giving it the ability to procrastinate—just like you! :D 

Instead of executing tasks efficiently, it gets *distracted*, mindlessly browses the internet, or justifies its procrastination with excuses. 

---

## **Installation**
You can install **Code Procrastinator** from **PyPI** using `pip`:

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

### **Create a Virtual Environment**
Before committing anything, ensure your contributions pass the unit tests
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
| Argument    | Type | Description |
|------------|------|-------------|
| `max_time`  | `int`  | The maximum number of seconds for any delay. Must be greater than `0`. |
| `delay_count` | `int`  | The number of procrastination delays. Must be greater than `0`. |

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
