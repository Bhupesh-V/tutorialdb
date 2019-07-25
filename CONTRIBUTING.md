# Contributing to tutorialdb

:+1::tada: First off, thanks for taking the time to contribute! :tada::+1:

The following is a set of guidelines for contributing to tutorialdb. These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

## Table of Contents
1. [About the Project](#about-the-project)
2. [Getting Started](#getting-started)
3. [Submitting Pull Request](#submitting-pull-request)

# About the Project
- **tutorialdb** is a small scale search engine for programming/dev tutorials, it is meant to help anyone who is getting started to learn a new technology.
- The sole purpose of tutorialdb is to help people get to resoures which might help them learn new things for e.g sometimes there are tutorials on personal blogs which do not get indexed in google easily.
- All the content (tutorials) is owned by the respective authors/sites.
- tutorialdb maintains its own database saving the links to tutorials and some meta info.

# Getting Started
- Make sure you communicate using github issues while submitting a PR or reporting bugs.
- Feel free while asking doubts, just open an [issue](https://github.com/Bhupesh-V/tutorialdb/issues/new).

# Submitting Pull Request
Follow below steps while submitting a PR.

1. Create your own branch(never commit to master).
2. Follow the below steps to setup development environment.
	- Create virtual environment.

		**Linux/macOS**
		```bash
		virtualenv -p python3 venv && cd venv && source bin/activate
		```

		**Windows:**
		```batch
		python -m venv venv && venv\Scripts\activate.bat
		```

	- Clone the repository.
    ```bash
    git clone https://github.com/Bhupesh-V/tutorialdb.git
    ```

	- Install dependencies.
    ```bash
    pip install -r requirements.txt
    ```

	- Migrate tables.
    ```bash
    python manage.py migrate
    ```

	- Set up `SECRET_KEY`
		1. Run `python manage.py shell`
		2. Do 
		```python
		>>> from django.core.management.utils import get_random_secret_key
		>>> get_random_secret_key()
		'[GENERATED KEY]'
		```
		3. Set this key in your Virtual Environment Variables.

	- Run server.
    ```bash
    python manage.py runserver
    ```
3. Make your changes
4. Push your changes to the branch.