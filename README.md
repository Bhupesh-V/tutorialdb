# tutorialdb
> A search engine for programming/dev tutorials.

## Installation

1. Clone the repository.

```bash
git clone https://github.com/Bhupesh-V/tutorialdb.git
```

2. Create virtual environment.

**Linux:**
```bash
virtualenv -p python3 venv && cd venv && source bin/activate
```

**Windows:**
```batch
python -m venv venv && venv\Scripts\activate.bat
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