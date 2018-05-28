# a-snivelling-little-rat-faced

An experiment with dulwich and code pushing itself.

## Getting started

```
git clone git@github.com:davejagoda/a-snivelling-little-rat-faced.git
cd a-snivelling-little-rat-faced/
vagrant up
```

## Using the guest

```
vagrant ssh
cd a-snivelling-little-rat-faced/
pipenv run ./hello_dulwich.py
pipenv run ./prepare_repo.py
pipenv run ./update_log_and_push.py
```
