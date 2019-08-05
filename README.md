# tutorialdb

> A search engine for programming/dev tutorials.

[![CodeFactor](https://www.codefactor.io/repository/github/bhupesh-v/tutorialdb/badge)](https://www.codefactor.io/repository/github/bhupesh-v/tutorialdb)

## Table of Contents

1. [About the Project](#about-the-project)
2. [Installation](#installation-)
3. [License](#-license)
4. [Author](#author)
5. [Contributing](#-contributing)

# About the Project

- **tutorialdb** is a small scale search engine for programming/dev tutorials, it is meant to help anyone who is getting started to learn a new technology.
- The sole purpose of tutorialdb is to help people get to resoures which might help them learn new things for e.g sometimes there are tutorials on personal blogs which do not get indexed by Google easily.
- All the content (tutorials) is owned by the respective authors/sites.
- tutorialdb maintains its own database saving the links to tutorials and some meta info.

# Installation 🔮

1. Create virtual environment.

**Linux:**
```bash
virtualenv -p python3 venv && cd venv && source bin/activate
```

**Windows:**
```batch
python -m venv venv && venv\Scripts\activate.bat
```

2. Clone the repository.

```bash
git clone https://github.com/Bhupesh-V/tutorialdb.git
```    

3. Install dependencies.

```bash
pip install -r requirements.txt
```

4. Set-up virtual environment variables.

	1. Run `python manage.py shell`
	2. Do 
	```python
	>>> from django.core.management.utils import get_random_secret_key
	>>> get_random_secret_key()
	'[GENERATED KEY]'
	```
	3. Create a file named only `.env` in the same directory as `manage.py` and put the `[GENERATED_KEY]` as your `SECRET_KEY`.
	4. You may also put your local machine's IP address as the `LOCAL_HOST` in the `.env` file.
	5. Uncomment the appropriate variables in the `manage.py` file.

	__Note:__ Put both the virtual environment variables as strings (ie within quotes).

4. Migrate tables.

```bash
python manage.py migrate
```

5. Run the development server.

```bash
python manage.py runserver
```

# 📝 License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE) file for details.

# Author

👥 **Bhupesh Varshney**

- Twitter: [@bhupeshimself](https://twitter.com/bhupeshimself)
- Github: [@Bhupesh-V](https://github.com/Bhupesh-V)

# 👋 Contributing

Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for the process of submitting pull requests to us.