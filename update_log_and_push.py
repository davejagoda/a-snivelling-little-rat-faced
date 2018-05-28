#!/usr/bin/env python3

BRANCH_NAME = 'dulwich'
REPO_PATH = '.'
URL = 'git@github.com:davejagoda/a-snivelling-little-rat-faced.git'

from dulwich import porcelain
import datetime
import os

def pull_branch(branch_name):
    porcelain.pull(REPO_PATH, URL, branch_name.encode())
    porcelain.update_head(REPO_PATH, branch_name)

def update_branch(file_name):
    message = '{} from {}'.format(
        datetime.datetime.utcnow().replace(microsecond=0).isoformat()+'Z',
        os.uname().nodename)
    f = open(file_name, 'a')
    f.write('{}\n'.format(message))
    f.close()
    porcelain.add(REPO_PATH, [file_name])
    porcelain.commit(REPO_PATH, 'Commit at {}'.format(message))

def push_branch(branch_name):
    porcelain.push(REPO_PATH, URL, branch_name.encode())

if '__main__' == __name__:
    pull_branch(BRANCH_NAME)
    update_branch('{}.log'.format(BRANCH_NAME))
    push_branch(BRANCH_NAME)
