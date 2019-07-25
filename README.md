# tutorialdb
> A search engine for programming/dev tutorials.

[![CodeFactor](https://www.codefactor.io/repository/github/bhupesh-v/tutorialdb/badge)](https://www.codefactor.io/repository/github/bhupesh-v/tutorialdb)

## Installation 🔮

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

4. Migrate tables.

```bash
python manage.py migrate
```

5. Run server.

```bash
python manage.py runserver
```


## 📝 License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE) file for details.

## Author

👥 **Bhupesh Varshney**

- Twitter: [@bhupeshimself](https://twitter.com/bhupeshimself)
- Github: [@Bhupesh-V](https://github.com/Bhupesh-V)

## 👋 Contributing

Please read the [CONTRIBUTING](CONTRIBUTING.md) for the process for submitting pull requests to us.
