# Chelone

The word **Chelone** is Ancient Greek for *Tortoise*, and has been used as a basis for the words *Chelonii* and *Chelonia*, historical alternative names for the [*Testudines*](https://en.wikipedia.org/wiki/Turtle) biological order (turtles, tortoises and terrapins).
Since [ROS](https://www.ros.org/) often uses various turtles as mascots, it is fitting for a variability analysis tool to use a name that encompasses all kinds of turtles.

## Tooling

This package sets up various `tox` environments for purposes such as static checks, testing, building and publishing.
It is also configured with `pre-commit` hooks to perform static checks and automatic formatting.

If you do not use `tox`, you can build the package with `build` and install a development version with `pip`.

Assume `cd` into the repository's root.

To install the `pre-commit` hooks:

```bash
pre-commit install
```

To run type checking:

```bash
tox -e typecheck
```

To run linting tools:

```bash
tox -e lint
```

To run automatic formatting:

```bash
tox -e format
```

To run tests:

```bash
tox
```

To build the package:

```bash
tox -e build
```

To build the package (with `build`):

```bash
python -m build
```

To clean the previous build files:

```bash
tox -e clean
```

To test package publication (publish to *Test PyPI*):

```bash
tox -e publish
```

To publish the package to PyPI:

```bash
tox -e publish -- --repository pypi
```

To install an editable version:

```bash
pip install -e .
```

## Package Structure

Package structure was inspired by various templates and recommended best practices, such as:

- https://github.com/TezRomacH/python-package-template
- https://github.com/pyscaffold/pyscaffold
- https://github.com/f4str/python-package-template
- https://github.com/audreyfeldroy/cookiecutter-pypackage
- https://github.com/ionelmc/python-nameless
