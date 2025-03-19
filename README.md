![build badge](https://github.com/software-students-spring2025/3-python-package-jeff-bezos/actions/workflows/build.yml/badge.svg?event=pull_request)

# Code Procrastinator

This package includes a variety of functions that humanizes your code by giving it the ability to procrastinate just like you :D

# Procrastinate()
The procrastinate function makes your program simulate what a human might do when they procrastinate like mindlessly scrolling the web or justifying their procrastination in their head.

This function:
- Randomly selects a number of unique delays between 0 and `max_time`.
- After each delay, it executes a randomly chosen procrastination action.
- Available actions include printing excuses and opening a fun website.

Args:
    max_time (int): The maximum number of seconds for any delay.
        Must be greater than 0.
    delay_count (int): The number of procrastination delays.
        Must be greater than 0.

Raises:
    ValueError: If `max_time` or `delay_count` is less than or equal to 0.

Returns:
    set: A set of unique delay times used during procrastination.

Example Usage:
    >>> procrastinate(10, 3)
    Procrastinating...
    Let's take an internet break! :D https://en.wikipedia.org/wiki/Special:Random
    Procrastinating...
    Wow this 4 hour video essay looks interesting...
    Procrastinating...
    I'll do it tomorrow
