# tutorialdb <img src="https://raw.githubusercontent.com/Bhupesh-V/tutorialdb/master/app/static/app/TDB.png" height="20px">

> A search engine for programming/dev tutorials.

<p align="center">
<img src="https://raw.githubusercontent.com/Bhupesh-V/tutorialdb/master/app/static/app/tutorialdb.png">
</p>


![GitHub release](https://img.shields.io/github/release/Bhupesh-V/tutorialdb)
[![GitHub license](https://img.shields.io/github/license/Bhupesh-V/tutorialdb)](https://github.com/Bhupesh-V/tutorialdb/blob/master/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/Bhupesh-V/tutorialdb)](https://github.com/Bhupesh-V/tutorialdb/issues)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/af7df141776744a49435a876c7b87834)](https://app.codacy.com/app/Bhupesh-V/tutorialdb?utm_source=github.com&utm_medium=referral&utm_content=Bhupesh-V/tutorialdb&utm_campaign=Badge_Grade_Dashboard)
[![All Contributors](https://img.shields.io/badge/all_contributors-4-orange.svg?style=flat-square)](#contributors)
[![CodeFactor](https://www.codefactor.io/repository/github/bhupesh-v/tutorialdb/badge)](https://www.codefactor.io/repository/github/bhupesh-v/tutorialdb)
[![Maintainability](https://api.codeclimate.com/v1/badges/a4b8a52583b6706c0b3f/maintainability)](https://codeclimate.com/github/Bhupesh-V/tutorialdb/maintainability)

### About the Project 🔘

- **tutorialdb** is a small scale search engine for programming/dev tutorials, it is meant to help anyone who is getting started to learn a new technology.
- The sole purpose of tutorialdb is to help people get to resources which might help them learn new things for e.g sometimes there are tutorials on personal blogs which do not get indexed by Google easily.
- All the content (tutorials) is owned by the respective authors/sites.
- tutorialdb maintains its own database saving the links to tutorials and some meta info.

### Installation 🔮

1. Create virtual environment.

	**Linux/MacOS**
	```bash
	virtualenv -p python3 venv && cd venv && source bin/activate
	```
	**Windows**
	(*PowerShell*)
	```cmd
	py -m venv venv; .\venv\Scripts\activate;
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
	1. Create a file named `.env` in the root directory & add the following contents.
	
	```text
	SECRET_KEY = 'my-secret-key'
	LOCAL_HOST = 'my-local-ip'
	```
	2. For `SECRET_KEY` use [Django Secret Key Generator](https://www.miniwebtool.com/django-secret-key-generator/) or [Djecrety](https://djecrety.ir/).
	3. Adding `LOCAL_HOST` is optional.

5. Migrate tables.

```bash
python manage.py migrate
```

6. Run Tests.

```bash
python manage.py test
```

7. Run the development server.

```bash
python manage.py runserver
```

## 📝 License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE) file for details.

## 👋 Contributing

Please read the [CONTRIBUTING](CONTRIBUTING.md) file for the process of submitting pull requests to us.

## ✨ Contributors

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/Animesh-Ghosh"><img src="https://avatars3.githubusercontent.com/u/34956994?v=4" width="100px;" alt=""/><br /><sub><b>MaDDogx</b></sub></a><br /><a href="https://github.com/Bhupesh-V/tutorialdb/commits?author=Animesh-Ghosh" title="Code">💻</a> <a href="https://github.com/Bhupesh-V/tutorialdb/issues?q=author%3AAnimesh-Ghosh" title="Bug reports">🐛</a> <a href="#ideas-Animesh-Ghosh" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/Bhupesh-V/tutorialdb/pulls?q=is%3Apr+reviewed-by%3AAnimesh-Ghosh" title="Reviewed Pull Requests">👀</a> <a href="#userTesting-Animesh-Ghosh" title="User Testing">📓</a></td>
    <td align="center"><a href="https://github.com/liorbentov"><img src="https://avatars3.githubusercontent.com/u/8587019?v=4" width="100px;" alt=""/><br /><sub><b>Lior Shub</b></sub></a><br /><a href="https://github.com/Bhupesh-V/tutorialdb/commits?author=liorbentov" title="Code">💻</a> <a href="https://github.com/Bhupesh-V/tutorialdb/issues?q=author%3Aliorbentov" title="Bug reports">🐛</a> <a href="#design-liorbentov" title="Design">🎨</a></td>
    <td align="center"><a href="https://www.crowbar.com.br"><img src="https://avatars0.githubusercontent.com/u/22822110?v=4" width="100px;" alt=""/><br /><sub><b>José Gabriel Gruber</b></sub></a><br /><a href="https://github.com/Bhupesh-V/tutorialdb/commits?author=JGabrielGruber" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/Yegorov"><img src="https://avatars1.githubusercontent.com/u/2566462?v=4" width="100px;" alt=""/><br /><sub><b>Artem</b></sub></a><br /><a href="https://github.com/Bhupesh-V/tutorialdb/commits?author=Yegorov" title="Code">💻</a></td>
    <td align="center"><a href="https://svendborg-webdesign.dk/en"><img src="https://avatars3.githubusercontent.com/u/4233458?v=4" width="100px;" alt=""/><br /><sub><b>Viktor Strate Kløvedal</b></sub></a><br /><a href="https://github.com/Bhupesh-V/tutorialdb/commits?author=viktorstrate" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/chrisshyi"><img src="https://avatars1.githubusercontent.com/u/24416618?v=4" width="100px;" alt=""/><br /><sub><b>Chris Shyi</b></sub></a><br /><a href="https://github.com/Bhupesh-V/tutorialdb/commits?author=chrisshyi" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/vikneswaran20"><img src="https://avatars1.githubusercontent.com/u/8945535?v=4" width="100px;" alt=""/><br /><sub><b>vikneswaran</b></sub></a><br /><a href="https://github.com/Bhupesh-V/tutorialdb/commits?author=vikneswaran20" title="Code">💻</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/ObliviousParadigm"><img src="https://avatars0.githubusercontent.com/u/47667852?v=4" width="100px;" alt=""/><br /><sub><b>Adarsh Shetty</b></sub></a><br /><a href="https://github.com/Bhupesh-V/tutorialdb/commits?author=ObliviousParadigm" title="Documentation">📖</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
