# jupyterquest: The Advanced .ipynb Autograder

| Category | Badges |
| --- | --- |
| Website | [![Netlify Status](https://api.netlify.com/api/v1/badges/602d0b5c-737a-4742-8e0b-8487cc3165aa/deploy-status)](https://app.netlify.com/sites/jupyterquest/deploys) |
| Testing | [![GitHub Workflow test status badge](https://img.shields.io/github/actions/workflow/status/Gchism94/jupyterquest/python-tests.yml?logo=github&logoColor=white)](https://github.com/Gchism94/jupyterquest/actions/workflows/autograder.yml) |
| License | [![License badge](https://img.shields.io/badge/License-MIT-yellow?logo=opensourceinitiative&logoColor=white)](https://github.com/Gchism94/jupyterquest/blob/main/LICENSE)
| Version | [![PyPI version badge](https://img.shields.io/pypi/v/jupyterquest?logo=python&logoColor=white&color=orange)](https://test.pypi.org/project/jupyterquest/)
 |


## Overview
**jupyterquest** is a comprehensive autograding tool designed to elevate the standard of Jupyter Notebook (.ipynb) submissions. Seamlessly integrated with GitHub Actions, it provides an automated evaluation process that spans across code style, structure, commit history, security vulnerabilities, and dependency checks. This tool is invaluable for educators, mentors, and development teams aiming to uphold best practices in code quality, security, and project organization.

## Features
- **Code Style and Formatting Checks**: Enforces best practices and consistency in coding styles.
- **Code Structure Analysis**: Assesses the organization and readability of code for maintainability.
- **Commit Message Quality**: Evaluates the clarity and conformity of commit messages to best practices.
- **Repository Structure Validation**: Ensures a logical and standardized file organization within repositories.
- **Security Vulnerability Scans**: Identifies known vulnerabilities in project dependencies to ensure code safety.
- **Dependency Analysis**: Checks for outdated or insecure dependencies that might compromise the project.
- **Extensible and Automated**: Designed for easy integration with CI/CD workflows, offering customizable options to meet various grading and analysis needs.

## Getting Started
### Prerequisites
- A GitHub account and a basic understanding of GitHub Actions.
- Knowledge of Jupyter Notebooks and the `.ipynb` file format.

### Installation
1. **Fork or Clone This Repository**: 
   Start by forking this repository to your account or cloning it directly to your local environment.

2. **Configure GitHub Actions**:
   In your repository on GitHub, navigate to the 'Actions' tab. Set up a new workflow with the provided `autograder.yml` workflow file.

3. **Customize the Autograder** (Optional):
   Adjust the `autograder.py` and other relevant scripts to fine-tune the grading criteria and checks according to your project or course requirements.

### Usage
- **Automatic Execution**: jupyterquest runs automatically with each push to the repository, thanks to GitHub Actions integration.
- **Reports**: The autograder generates detailed Markdown reports, offering actionable insights on code improvements and highlighting commendable practices.

## Contribution
We encourage contributions! If you're interested in enhancing jupyterquest or adding new features, please consult our contributing guidelines for more information on how to get started.

## License
jupyterquest is made available under the MIT License. For more details, see the [LICENSE](LICENSE) file.

## Support and Contact
Need help or have questions? Feel free to [open an issue](https://github.com/Gchism94/jupyterquest/issues) in this repository for support and inquiries.
