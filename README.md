# Python.GitHub.RepoCreate
Python script for creating GitHub Repositories through the GitHub api

usage: GitHub.Repo.Create.py [-h] [-t TOKEN] [-u URL] [-p PRIVATE] [-i ISSUES]
                             [-w WIKI] [-d DOWNLOADS] [-m TEAMID]
                             [-a AUTOINIT] [-g GITIGNORE] [-l LICENSE]
                             name description

positional arguments:
  name                  The name of the new GitHub Repository.
  description           A description for the new GitHub Repository.

optional arguments:
  -h, --help            show this help message and exit
  -t TOKEN, --token TOKEN 
                        The GitHub User's Token. If no token is provided then
                        an attempt at pulling the value from the user's
                        environment variables is made.
  -u URL, --url URL     The URL with more info about the repository.
  -p PRIVATE, --private PRIVATE
                        True to create repository as private. Default is
                        false.
  -i ISSUES, --issues ISSUES
                        True to enable issues in repository. Default is true.
  -w WIKI, --wiki WIKI  True to enable a wiki for the repository. Default is
                        true.
  -d DOWNLOADS, --downloads DOWNLOADS
                        True to enable repository downloads. Default is true.
  -m TEAMID, --teamid TEAMID
                        Id of the team that is granted access to the
                        repository. Only valid when creating repo in an
                        organization.
  -a AUTOINIT, --autoinit AUTOINIT
                        True to create an initial commit with an empty README.
                        Default is false.
  -g GITIGNORE, --gitignore GITIGNORE
                        The language or platform of the .gitignore template to
                        apply. Use name of the template without extension.
  -l LICENSE, --license LICENSE
                        The license template to apply to repository. Use the
                        name fo the license template without the extension.
