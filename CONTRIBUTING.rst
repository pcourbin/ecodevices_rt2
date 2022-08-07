.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/pcourbin/ecodevices_rt2/issues.

If you are reporting a bug, please include:

* Your version of the custom_component and your configuration.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

ecodevices_rt2 could always use more documentation, whether as part of the
official pyecodevices_rt2 docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/pcourbin/ecodevices_rt2/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `ecodevices_rt2` for local development.

1. Fork the `ecodevices_rt2` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/ecodevices_rt2.git

3. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

4. This work is using `Visual Studio Code + devcontainer`_ environement:

 a. Open the repository using Visual Studio code.
 b. When you open this repository with Visual Studio code,
    you are asked to "Reopen in Container", this will start the build of the container.
 c. 'Terminal > Run Task... > Run Home Assistant on port 9123'

5. Configure your tests and pre-commit environnement::

    $ pip install -r requirements_dev.txt
    $ pre-commit install

6. When you're done making changes, check that your changes pass lint and the
   tests, including testing other Python versions with tox::

    $ make lint
    .. $ python setup.py test or pytest
    .. $ tox

7. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

8. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.

.. 3. The pull request should work for Python 3.5, 3.6, 3.7 and 3.8, and for PyPy. Check
   https://travis-ci.com/pcourbin/pyecodevices_rt2/pull_requests
   and make sure that the tests pass for all supported Python versions.

.. Tips
.. ----

.. To run a subset of tests::

.. $ pytest tests.test_ecodevices_rt2


Deploying
---------

A reminder for the maintainers on how to deploy.
Make sure all your changes are committed (including an entry in HISTORY.rst).
Then run::

$ bump2version patch # possible: major / minor / patch
$ git push
$ git push --tags

.. _`Visual Studio Code + devcontainer`: https://developers.home-assistant.io/docs/development_environment/
