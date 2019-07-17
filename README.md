# tutorialdb
> A search engine for programming/dev tutorials.

## Installation
1. Create virtual environment.
```bash
virtualenv -p python3 venv && cd venv && source bin/activate
```
2. Clone the repository.
```bash
git clone https://github.com/Bhupesh-V/tutorialdb.git
```
3. Install Dependencies.
```bash
pip install -r requirements.txt
```
4. Migrate tables.
```bash
python migrate
```
5. Run Server.
```bash
python manage.py runserver
```