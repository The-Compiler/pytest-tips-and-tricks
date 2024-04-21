# pytest tips and tricks for a better testsuite

## Note

The code in `code/` is still WIP until Monday ~noon, unfortunately a few minor
last-minute changes are expected. Slides will be added around that time as well.

The provided code is for 3 days of training, so we're not going to use all of
it. If you want to prepare, take a look at `rpncalc/` (especially `rpn_v2.py`
and `utils.py`), which is a small example project we'll use in the training.

## Setup instructions

- We'll be using pytest on the commandline for the training.
- If you use PyCharm:
    - Open the `code/` folder as a project
    - Tell it to install `requirements.txt`
    - Open a terminal inside PyCharm and make sure things work by running
      `pytest --version`, you should see 8.1.x ideally (7.0+ is ok)
- Manual setup:
    - [Create a virtualenv](https://chriswarrick.com/blog/2018/09/04/python-virtual-environments/) and activate it (or substitute tool paths below)
    - `pip install -r code/requirements.txt`
- Check everything works:
    - Check `python3 --version` (Windows: `py -3 --version`), make sure you run 3.8 or newer.
    - Check `pytest --version`, you should see 7.4 ideally (7.0+ is ok)
- In case of trouble/questions, please feel free to ask! Any of these will work fine:
    - [`@thecompiler` on Telegram](https://telegram.me/thecompiler)
    - [`florian@bruhin.software`](mailto:florian@bruhin.software)
    - IRC: `The-Compiler` on [Libera Chat](https://libera.chat/)
    - [`@the_compiler` on Discord](https://discord.com/users/329364263896481802) (e.g. Python Discord or PyConDE)
    - [`@the_compiler` on Twitter/X](https://twitter.com/the_compiler)
