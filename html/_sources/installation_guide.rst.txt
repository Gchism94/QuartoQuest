.. _installation-guide:

Installation
==================

The JupyterQuest Autograder leverages GitHub Actions to automate the grading process, eliminating the need for manual installation of the tool in your local environment. This guide provides an overview of the prerequisites and steps to configure your GitHub repository to use the autograder.

Prerequisites
--------------

Before integrating the autograder with your GitHub repository, ensure you have:

- A GitHub account.
- Administrative access to the GitHub repository containing the assignments you wish to grade.
- Basic familiarity with GitHub Actions.

Repository Configuration
-------------------------

Make sure to configure your repository as described in the :ref:`repository configuration section <repo-configuration>` of the installation guide.

GitHub Actions Setup
---------------------

1. **Workflow File**: Navigate to the `.github/workflows` directory in your repository. If this directory does not exist, create it.

2. **Create Workflow**: Within the `.github/workflows` directory, create a new YAML file for the autograder workflow, such as `autograder.yml`.

3. **Workflow Content**: Copy the contents from the [Usage Instructions](link-to-usage-instructions) guide into your new `autograder.yml` file. Customize the workflow according to your specific grading requirements and repository structure.

4. **Commit Changes**: Commit the new `autograder.yml` file to your repository. This action enables the autograder workflow within your GitHub Actions.

Dependencies
-------------

The autograder installation process will automatically handle the installation of necessary dependencies when the GitHub Action runs. If your assignments require additional Python packages or dependencies, specify them in a `requirements.txt` file at the root of your repository.

Support
-------

For assistance with configuring your repository or troubleshooting the autograder workflow, please refer to the [FAQ](link-to-faq) or [submit an issue](link-to-github-issues) on the GitHub repository page.