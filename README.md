# Introduction

This repo serves as an example to get started with Flask.

# Getting started

1. Clone the repo on your local device: `git@github.com:chunloy/flask-workshop.git`
2. Navigate into `flask-workshop` directory and create a virtual environment: `cd flask-workshop && python -m venv .venv`
3. Activate the virtual environment: `source .venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Start the server in debugging mode: `flask run --debug`
6. Close the virtual environment when you're done: `deactivate`

> Note: See section below for things I forgot to mention during the workshop.

# Things not covered

1. The code may look slightly different from the recording due to small changes that I made, I'd recommend using this repo for reference. Changes involved returning data _as is_ because they are valid return types by default.

2. You can get away with running `flask run` _as is_ because the module is named `app.py`. If the module was named different, you'd have to specify the name in the command.

3. Making a request to get details for a single artist: `see lines 95-98 in app.py`

4. Making the `POST` request: `curl -X POST localhost:5000/artists -d '{"artist_name":"notaaron","song_title":"song","featured_artist":"null","album_name":"hello, world","song_length":"4:00 PM"}' -H 'Content-type: application/json'`

- `-X` specifies the type of request
- `-d` specifies the data in the request body
- `-H` specifies in the request header that the data is `json`

5. Try making a curl request with `GET`. This is my attempt at getting you all `CLI Certified`.

# Flask workshop notes

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
