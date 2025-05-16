#!/usr/bin/env python
import os
from chibi_command import Command
from chibi_github import Github_api
from chibi_git import Git


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':
    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')
        remove_file('docs/authors.rst')

    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        cli_file = os.path.join('{{ cookiecutter.project_slug }}', 'cli.py')
        remove_file(cli_file)

    github_private = False
    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')
        github_private = True

    Command( 'virtualenv', 'venv' ).run()
    Command( 'venv/bin/pip', 'install', '-e', '.' ).run()
    Command( 'venv/bin/pip', 'install', '-r', 'requirements_dev.txt' ).run()

    if '{{ cookiecutter.reate_github_repo }}' == 'y':
        api = Github_api()
        api.login()
        response = api.me.repos.create(
            name='{{ cookiecutter.project_slug }}',
            description=(
                '{{ cookiecutter.project_short_description }}' ),
            private=github_private,
        )
        if not response.ok:
            import pdb
            pdb.set_trace()
            raise NotImplementedError(
                "no esta implementado el manejo de error de github" )
        ssh_url = response.native.ssh_url

        repo = Git( PROJECT_DIRECTORY )
        repo.init()
        for file in repo.status.untrack:
            file.add()
        repo.commit( "iniciando repo {{ cookiecutter.project_name }}" )
        repo.remote.append( 'origin', ssh_url )
        repo.push( 'origin', 'master', set_upstream=True )
