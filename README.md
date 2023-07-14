# pytest tips and tricks for a better testsuite

## Setup instructions

- We'll be using pytest on the commandline for the training.
- If you use PyCharm:
    - Open the `code/` folder as a project
    - Tell it to install `requirements.txt`
    - Open a terminal inside PyCharm and make sure things work by running
      `pytest --version`, you should see 7.4 ideally (7.0+ is ok)
- Manual setup:
    - [Create a virtualenv](https://chriswarrick.com/blog/2018/09/04/python-virtual-environments/) and activate it (or substitute tool paths below)
    - `pip install -r code/requirements.txt`
- Check everything works:
    - Check `python3 --version` (Windows: `py -3 --version`), make sure you run 3.8 or newer.
    - Check `pytest --version`, you should see 7.4 ideally (7.0+ is ok)
