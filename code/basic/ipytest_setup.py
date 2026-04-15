import ipytest

ipytest.autoconfig(addopts=["--color=yes", "--no-header"])
print("You can now use %%ipytest to run pytest on a cell's contents.")
