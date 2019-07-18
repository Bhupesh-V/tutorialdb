# tutorialdb
> A search engine for programming/dev tutorials.

## Installation

### Linux

1. Clone the repository.

```bash
git clone https://github.com/Bhupesh-V/tutorialdb.git
```

2. Create virtual environment.

```bash
virtualenv -p python3 venv && cd venv && source bin/activate
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

### Windows

1. Clone the repository.

```batch
git clone https://github.com/Bhupesh-V/tutorialdb.git
```

2. Create virtual environment.

```batch
python -m venv venv && venv\Scripts\activate.bat
```

3. Install dependencies.

```batch
pip install -r requirements.txt
```

4. Migrate tables.

```batch
python manage.py migrate
```

5. Run server

```batch
python manage.py runserver
```