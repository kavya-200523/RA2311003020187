# Vehicle Maintenance Scheduler
This back-end assignment schedules vehicle maintenance activities according to available mechanic hours.

This program retrieves vehicle maintenance information from the provided secure APIs. Every vehicle activity consists of a service duration and an impact factor. Here, our goal is to find the most optimal combination of vehicle activities with a maximum sum of impact factors without exceeding the mechanic hour availability.

## Approach
This particular problem can be solved using the Knapsack 0/1 algorithm.

- Mechanic hour availability becomes the capacity.
- The duration of each task becomes the weight.
- Impact factor becomes the value of the task.
- The program then picks tasks with maximum value.

## Files

- `scheduler.py` - main Python solution file

## How to run

Install requests:

```bash
pip install requests
```
Run the program:

```bash
python scheduler.py
```

Before running the file, replace the `TOKEN` value in `scheduler.py` with the access token generated from the Authorization API.