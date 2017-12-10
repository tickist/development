#!/usr/bin/python3
import os
import shutil
import subprocess

should_pull_git_repositories = False
BACKEND_REPOSITORY_URL = 'git@github.com:tickist/backend.git'
FRONTEND_REPOSITORY_URL = 'git@github.com:tickist/frontend.git'
DOCKERCOMPOSE = 'docker-compose'
DOCKERCOMPOSESNAP = 'docker.compose'


def create_ssh_key():
    os.system('ssh-keyscan github.com >> ~/.ssh/known_hosts')

def is_git_enabled():
    return shutil.which('git')


def is_docker_enabled():
    return shutil.which('docker')


def get_docker_compose_command():
    if shutil.which(DOCKERCOMPOSE):
        return DOCKERCOMPOSE

    if shutil.which(DOCKERCOMPOSESNAP):
        return DOCKERCOMPOSESNAP


def check_dependencies():
    if not is_docker_enabled():
        raise RuntimeError("Please install docker and docker-compose ")
    if not is_git_enabled():
        raise RuntimeError("Please install git")


def check_folder_structure():
    should_pull_git_repositories = True


def download_backend_repository():

    process = subprocess.Popen(["git", "clone", BACKEND_REPOSITORY_URL], stdout=subprocess.PIPE)
    output = process.communicate()[0]

def download_frontend_repository():
    process = subprocess.Popen(["git", "clone", FRONTEND_REPOSITORY_URL], stdout=subprocess.PIPE)
    output = process.communicate()[0]


if __name__ == "__main__":
    current_docker_compose = get_docker_compose_command()
    create_ssh_key()
    check_dependencies()
    check_folder_structure()
    if not should_pull_git_repositories:
        download_backend_repository()
        download_frontend_repository()
