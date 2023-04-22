# Flask Demo

## Agenda

1. Prerequisites: install pip, virtualenv
2. Setting up your project: activate & deactivate virtualenv
3. Live demo: Setup Flask server + routing
4. Q & A

## Prerequisites

These instructions assume you have Python 3.x installed.

### Installing pip

Run this command to install `pip`:

```zsh
cd ~
python3 -m pip install --user --upgrade pip
python3 -m pip --version
```

> Link installation docs: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

### Installing virtualenv

Run this command to install `virtualenv`:

```zsh
pip install virtualenv
```

> link to package description: https://pypi.org/project/virtualenv/

## Setting up your project

Why create a virtual environment? It installs packages only in the current directory. It's best to avoid installing packages globally to prevent version conflicts.

> Note: The following commands are only vaild for Mac. If you're on Windows, you'll need to use a different set of commands.

1. Create a virtual environment by running this command:

```zsh
python -m venv .venv
```

> Note: you should see a folder named `.venv` in your project's root directory

2. Activate the virtual environment:

```zsh
source .venv/bin/activate
```

> Note: Make sure you do this BEFORE installing packages!

3. Run this command to close the virtual environment:

```zsh
deactivate
```

### Tracking dependencies (optional, sort of)

After creating a project, you'll probably want to install and keep track of the packages you've installed. This will help other developers clone your project and install dependencies.

1. Create a text file in the project's root directory:

```szh
touch requirements.txt
```

2. Run this command to list your dependencies in the text file:

```zsh
pip freeze > requirements.txt
```

> Note: You'll want to run the above command every time you install new packages. Python doesn't keep track of them for you.

## Flask Demo

### -------------------- DON'T SHOW YOUR AWESOME SECRET CODE! --------------------
