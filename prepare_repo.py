#!/usr/bin/env python3

BRANCH_NAME = 'dulwich'
REPO_PATH = '.'
URL = 'git@github.com:davejagoda/a-snivelling-little-rat-faced.git'

from dulwich import porcelain

def branch_exists(branch_name):
    if branch_name.encode() in porcelain.branch_list(REPO_PATH):
        return True
    return False

def create_branch(branch_name):
    porcelain.branch_create(REPO_PATH, branch_name)
    print('branch {} created'.format(branch_name))
    porcelain.push(REPO_PATH, URL, branch_name.encode())
    print('branch {} pushed'.format(branch_name))

if '__main__' == __name__:
    if branch_exists(BRANCH_NAME):
        print('branch {} found'.format(BRANCH_NAME))
    else:
        create_branch(BRANCH_NAME)
