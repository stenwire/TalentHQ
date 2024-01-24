# 🔐 jWT Token Authentication in DRF and Blog

### ♨️API Docs:
[Go-to swagger docs](http://localhost:8000/swagger/)

## To run test:
  `make test`


### ⚒️ Tools:
- DRF
- Makefile
- Python pipenv

# ⚙️ Setup

```shell

- clone repo

git clone <link to repo>

- Go into the folder

cd :\\path\\to\\cloned_repo

- install pipenv

pip install pipenv

- activate pipenv

make shell

- install dependencies

make install
```
- Create a copy of `.env.example` and rename to `.env` then fill in the values

- Run Migrations with:
`make makemigrations`
`make migrate`

# 🏃 To run app:
```shell
make up

accessible through: http://127.0.0.1:8000/
```

- Create admin user with:
> whilst in project directory

`make py-shell`

Then:
```shell
>>> from authme.models import CustomUser

>>> CustomUser.objects.create_user(email="youremail@example.com",username="johnDoe707", password="strongpassword")
```
