# Contributing to tutorialdb

👍 🎉 First off, thanks for taking the time to contribute! 👍 🎉

The following is a set of guidelines for contributing to tutorialdb. These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Submitting Pull Requests](#submitting-pull-requests)

### Getting Started

- Make sure you communicate using GitHub issues while submitting a PR or reporting bugs.
- You can use an appropriate label to label the issue.
- Feel free while asking doubts, just open an [issue](https://github.com/Bhupesh-V/tutorialdb/issues/new).

### Submitting Pull Requests

**Before submitting a Pull Request, please make sure there is a corresponding issue.  If not, please provide a clear description and title for your PR**

Follow the steps below while submitting a PR.

1. Create your own branch (never commit to master).
2. Setup the development environment by following the [Installation](README.md#installation-) instructions.
3. Run the development server.

```bash
python manage.py runserver
```

4. Make your changes.
5. Run Tests.

```bash
python manage.py test
```

6. Push your changes to your branch. Make sure to comment the `SECRET_KEY` and `LOCAL_HOST` variables.
7. Create a Pull Request against the `master` branch.
