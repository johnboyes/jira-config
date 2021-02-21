# How to contribute

Firstly thanks for thinking of contributing - the project is [open source](https://opensource.guide/how-to-contribute/)
and all contributions are very welcome :slightly_smiling_face: :boom: :thumbsup:

[How to make a contribution](#how-to-make-a-contribution)

[Local development](#local-development)

* [Visual Studio Code](#visual-studio-code)
* [Codespaces](#codespaces)
* [Tools and technologies](#tools-and-technologies)

## How to make a contribution

* [Create a pull request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests).
The project uses the _[fork and pull model](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-collaborative-development-models)_:
  * [Fork the project](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/working-with-forks)
  * Make your changes on your fork
  * Write a [good commit message(s)](https://chris.beams.io/posts/git-commit/) for your changes
  * [Create the pull request for your changes](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/proposing-changes-to-your-work-with-pull-requests)

## Local development

### Visual Studio Code

The easiest way to set up your development environment (unless you have [Codespaces](#codespaces), which is even easier)
is to use [Visual Studio Code](https://code.visualstudio.com/)'s [Remote Containers](https://code.visualstudio.com/docs/remote/containers)
functionality:

* [System requirements](https://code.visualstudio.com/docs/remote/containers#_system-requirements)
* [Fork the project](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/working-with-forks)
* [Open the local project folder in a container](https://code.visualstudio.com/docs/remote/containers#_quick-start-open-an-existing-folder-in-a-container)
* Everything will then be setup for you.

### Codespaces

If you have access to [GitHub Codespaces](https://github.com/features/codespaces/) (which allows full remote
development from within your browser) then all you need to do is [fork the project](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/working-with-forks)
and open it in Codespaces - easy!

### Tools and technologies

* [Gauge](https://gauge.org)
* [Python](https://www.python.org/)
  * [Black](https://github.com/psf/black) for Python formatting
  * [Flake8](https://flake8.pycqa.org/) for Python style checks
* [GitHub Actions](https://docs.github.com/en/actions) for CI

## Updating dependencies

See the [DEPENDENCIES.md](.github/DEPENDENCIES.md)
