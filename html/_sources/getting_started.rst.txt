.. _usage-instructions:

Usage Instructions
===================

The JupyterQuest Autograder is designed to automate the grading of coding assignments using GitHub Actions. This document provides step-by-step instructions on how to set up and use the autograder for your projects.

Prerequisites
--------------

Before setting up the autograder, ensure you have:

- A GitHub account.
- A repository with coding assignments you wish to grade.
- Basic understanding of GitHub Actions.

GitHub Repository Structure
---------------------------

.. _repo-configuration:

For the JupyterQuest Autograder to work effectively, your GitHub repository should adhere to a specific structure. This structure ensures the autograder can locate and process your Jupyter notebooks, associated data, images, and any additional files necessary for grading.

Below is an example structure of a well-organized GitHub repository:

.. code-block:: text

    .
    ├── .github
    │   └── workflows
    │       └── autograder.yml      # GitHub Actions workflow for the autograder
    ├── data                        # Directory for datasets used in assignments
    ├── images                      # Directory for images used in notebooks or documentation
    ├── docs                        # Directory for project documentation and reports
    ├── assignment.ipynb            # Targey Jupyter notebook (.ipynb files)
    ├── requirements.txt            # Python dependencies required for the notebooks
    ├── LICENSE                     # The license file (not required)
    └── README.md                   # The project readme with an overview of the repository

Ensure you adjust the repository structure according to the specific needs of your assignments or projects. The directories and files listed above are recommended for a typical use case but can be customized as necessary.

- The `.github/workflows/autograder.yml` file contains the GitHub Actions workflow configuration for running the autograder.
- The `data` and `images` directories should contain any datasets and images referenced by your Jupyter notebooks, respectively.
- The `docs` directory is intended for any generated reports or additional documentation you wish to include.
- The `notebooks` directory should contain all Jupyter notebooks (.ipynb files) that will be graded.
- The `requirements.txt` file specifies all Python packages required to run the notebooks successfully. This file is used by the autograder to install dependencies in its execution environment.
- The `LICENSE` and `README.md` files provide important information about the project's license and an overview of the repository, respectively.

By organizing your repository according to these guidelines, you ensure that the autograder can efficiently locate and process the necessary files for grading your Jupyter notebooks.



Setting Up GitHub Actions
-------------------------

1. Navigate to your repository on GitHub.
2. Click on the **Actions** tab.
3. Create a new workflow by choosing **set up a workflow yourself** or use an existing `.yml` file in the `.github/workflows` directory.
4. Copy the contents of the provided `autograder.yml` into your new workflow file.

Configuring the Autograder Action
----------------------------------

- **Workflow File**: The `autograder.yml` file defines the steps to set up the environment, install dependencies, and execute the autograder.
- **Example Configuration**:

.. code-block:: yaml

    name: Use Autograder Package
    on: [push]

    jobs:
      run-autograder:
        runs-on: ubuntu-latest
        permissions:
          contents: write
        steps:
          - uses: actions/checkout@v2
            with:
              token: ${{ secrets.GITHUB_TOKEN }}
              fetch-depth: 0
              ref: main

          # Add additional setup steps if necessary
          - name: Set up Python
            uses: actions/setup-python@v2
            with:
              python-version: '3.8'

          # Install the autograder package
          - name: Install Dependencies
            run: |
              python -m pip install --upgrade pip
              pip install git+https://github.com/Gchism94/jupyterquest.git

          # Run the autograder
          - name: Run Autograder
            run: python -m jupyterquest.autograder

          # Additional steps to handle autograder report

Triggering the Autograder
-------------------------

The autograder is configured to run on every `push` to the `main` branch. You can adjust the trigger as needed, using events like `pull_request`, `workflow_dispatch`, or others.

Viewing Results
----------------

After the autograder runs, the results are committed and pushed to the `gh-pages` branch under the `docs` folder as `index.html`. You can view the graded report by navigating to the GitHub Pages URL of your repository.

Advanced Configuration
-----------------------

For more advanced usage, including custom grading scripts or additional dependencies, modify the `autograder.yml` file accordingly. Refer to the GitHub Actions documentation for more details on custom workflows.

Support
-------

If you encounter issues or have questions about setting up or using the autograder, please refer to the [GitHub repository](https://github.com/Gchism94/jupyterquest) or submit an issue.

