# pyenv and pipenv

__virtualenv__ is a very popular tool that creates isolated Python environments for Python libraries.
It works by installing a bunch of files in a directory (eg: env/), and then modifying the PATH environment variable to prefix it with a custom bin directory (eg: env/bin/).
An exact copy of the python or python3 binary is placed in this directory, but Python is programmed to look for libraries relative to its path first, in the environment directory.
It's not part of Python's standard library, but is officially blessed by the PyPA (Python Packaging Authority).
Once activated, you can install packages in the virtual environment using pip.

__pyenv__ is used to isolate Python versions.
For example, you may want to test your code against Python 2.6, 2.7, 3.3, 3.4 and 3.5, so you'll need a way to switch between them.
Once activated, it prefixes the PATH environment variable with ~/.pyenv/shims, where there are special files matching the Python commands (python, pip).
These are not copies of the Python-shipped commands; they are special scripts that decide on the fly which version of Python to run based on the PYENV_VERSION environment variable, or the .python-version file, or the ~/.pyenv/version file. pyenv also makes the process of downloading and installing multiple Python versions easier, using the command pyenv install.

__pipenv__, by Kenneth Reitz (the author of requests), is the newest project in this list.
It aims to combine Pipfile, pip and virtualenv into one command on the command-line.
The virtualenv directory typically gets placed in ~/.local/share/virtualenvs/XXX, with XXX being a hash of the path of the project directory.
This is different from virtualenv, where the directory is typically in the current working directory.
pipenv is the officially recommended way of managing project dependencies.
Instead of having a requirements.txt file in your project, and managing virtualenvs, you'll now have a Pipfile in your project that does all this stuff automatically.


## pyenv

Install pyenv
```
sudo apt-get install build-essential git libreadline-dev zlib1g-dev libssl-dev libbz2-dev libsqlite3-dev libffi-dev
curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
```

Add to ~/.bashrc
```
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

To check which versions are available:
```
pyenv install --list
```

To install 3.7.2
```
pyenv install 3.7.2
```

To check which Python versions are available:
```
pyenv versions
```

Now, you can change your global interpreter:
```
python --version
pyenv which python
pyenv global 3.7.2
python --version
pyenv which python
```

To return to the system interpreter, run:
```
pyenv global system
python --version
```

pyenv allows you to install different versions for single directory:
```
pyenv versions
mkdir project 
cd project
python --version
pyenv local 3.7.2
python --version
pyenv versions
```

Now whenever you are in project, you’ll automatically use the Python 3.7.0 interpreter.


## pipenv

Install pipenv with pip.  You have to do this for every version of python you install with pyenv.
```
pyenv shell 3.7.2
pip instll pyenv
```

Allow pipenv to use pyenv.
It’s better for pipenv to discover pyenv python versions to allow for seamless interoperability.
```
export PATH="$HOME/.pyenv/bin:$PATH"
echo 'export PIPENV_PYTHON="$PYENV_ROOT/shims/python"' >> ~/.bashrc
```

Verify pyenv and pipenv work:
```
pipenv
```

To activate the virtual environment:
```
pipenv shell
exit
```

To execute a command inside the venv:
```
pipenv run python command_line.py
```

Use pipenv:
```
cd test
pipenv shell
pipenv install flask
```

Show a graph of installed dependencies:
```
pipenv graph
pipenv graph --reverse
```

Use a lower-level pip command:
```
pipenv run pip freeze
```

