# Purpose of This Repository

This repository is created for implementing a generic `Logging Structure` for my Python projects.

# Conda Environment

The conda environment is created by following command line: 

```bash
conda create -n logger python=3.9
```

Lastly, the environment for development of the logger project is extracted as follows:

```bash
conda env export > environment.yml
```

In order to use my development environment, run the following command line on your cli:

For active environment:
```bash
conda env create -f environment.yml
```

For the environment that is not activated:
```bash
conda env update --name envname--file environment.yml
```

# Resources
- https://signoz.io/guides/python-logging-create-log-if-not-exists-or-open-and-continue-logging-if-it-does/

- https://docs.python.org/3/howto/logging.html#logging-basic-tutorial


Feel free to reach out for improving my code. Thanks!
