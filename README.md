# CourseLoader
This is an application used to scrap and load course information (course code, title - "CPSC110", "Computational Thinking") onto the the [CourseHub](https://github.com/aaronNgu/CourseHub) project.

## How to use this?
This assumes you have Python installed on your machine. 
1. clone repository.
2. go into the cloned repository `cd <repo name>`.
2. create a virtual environment `python -m venv env` or `python3 -m venv env`.
3. run `pip install requirements.txt`
4. run `python main.py`

## What courses does it scrap?
This can be specified in the `coursestoscrap.csv`.
Create a new line and enter the coursecode(APSC160) of the course that you want to scrap

## Some other features
You can specify words that you want to filter out in the title in `filters.csv`.

For example:
I don't want courses with title that contains that word 'Food'.
To do so, create a new line and type in the word 'Food' (without quotes) then save.
