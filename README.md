# a-snivelling-little-rat-faced

An experiment with dulwich and code pushing itself.

## Getting started

### Clone the repo and enter the repo directory

```
git clone git@github.com:davejagoda/a-snivelling-little-rat-faced.git
cd a-snivelling-little-rat-faced/
```

### Generate a deploy key and upload it to Github

```
ssh-keygen -t rsa -b 4096 -C dulwich_deploy_key -f dulwich_deploy_key -N ''
GITHUB_TOKEN=*YOUR_GITHUB_TOKEN* ./upload_deploy_key.py dulwich_deploy_key.pub
```

## Running with a virtualbox guest

### Create and start the guest, then SSH on to it

```
vagrant up
vagrant ssh
```

### Using the guest

```
cd a-snivelling-little-rat-faced/
pipenv run ./hello_dulwich.py
pipenv run ./prepare_repo.py
pipenv run ./update_log_and_push.py
```
