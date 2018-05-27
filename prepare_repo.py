#!/usr/bin/env python3

BRANCH_NAME = 'dulwich'
REPO_PATH = '.'

from dulwich import porcelain

def branch_exists(branch_name):
    if branch_name.encode() in porcelain.branch_list(REPO_PATH):
        return True
    return False

def create_branch(branch_name):
    porcelain.branch_create(REPO_PATH, BRANCH_NAME)
    print('branch {} created'.format(BRANCH_NAME))

if '__main__' == __name__:
    if branch_exists(BRANCH_NAME):
        print('branch {} found'.format(BRANCH_NAME))
    else:
        create_branch(BRANCH_NAME)
