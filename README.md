This README has been created based on a machine running on Mac, so some of the Windows instructions may be lacking, please fill in any gaps found.

# Required Installation

Get terraform installed, see [Terraform CLI Installation](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli#install-terraform) for more instructions.

Python

# Pre-commits

To ensure that only properly linted and security-aligned code has been pushed, pre-commits have been added that checks over codes for linting and checks security over the terraform code. To make sure these run on your machine, install [ruff](https://docs.astral.sh/ruff/installation/), [tflint](https://aquasecurity.github.io/tfsec/v0.63.1/getting-started/installation/) and [tfsec](https://aquasecurity.github.io/tfsec/v0.63.1/getting-started/installation/). When you commit files, these checks will run against the code, please ensure you save and re-add any altered files via `git add`.

# Virtual Environments

Virtual environments are useful as they allow you to have several indepedent python versions running on your machine and it allows you to select which version you like for your repository. By having an isolated virtual environment with the same packages, you and any other developer working on the project should have the same setup.

Users should look into using UV which is a modern project manager which includes pip and virtual enviornments. Instructions are given below for MacOS/Linux and Windows. Follow the steps below to create and activate the the virtual environments according to your OS, then move onto the Getting Started section.

## Installing UV

If you are using Mac/Linux and do not already have UV installed, do so now using any of the following commands. More methods can be found in the [documentation](https://docs.astral.sh/uv/getting-started/installation/).

Just need to use one of these, whichever works first:

Linux/Mac:

`brew install uv`

`curl -LsSf https://astral.sh/uv/install.sh | sh`

`pip install uv`

Windows:

`brew install uv`

`powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`

`pip install uv`

Note: this project has already been initialised with `uv init` and commited so this command can be skipped.

## Activating virtual environments

For this repo, we will be using python version 3.11.9, it is important we use the same version to ensure everything works for the same regardless of the machine it is running on. As the UV package is quite a powerful tool, the version doesn't need to be stated, it will be picked up by the pyproject.toml file. Use the command below to create the virtual environment.

`uv venv`

Note: there are a lot more methods for handling venv, including naming them and having multiple venvs (would require adding to the .gitignore) but not necessary for this project.

Now that the [.venv](.venv/) folder has been created, it is time to active it using the following commands.

Linux/Mac: `source .venv/bin/activate`

Windows: `.venv\Scripts\activate`

Note: you can check if you're in the virtual environment by running `which python` in Linux/Mac or `where python` in Windows, if it is active, it should point at the python installation in the .venv folder.

You can exit the virtual environment with the `deactivate` command but if this is your first time going through this readme then there are still additional steps to set up.

## Python packages

Now that we have activated a virtual environment, we can begin our python commands, we will start by installing all the necessary packages that are listed out in the pyproject.toml file by syncing the package requirements to the venv.

`uv sync`

Note: in case you do any specific pip installations ensure that commands begin with `uv` otherwise pip commands will be installed in your main python path, not your virtual environment.

You can also add new packages using `uv add with various [parameters](https://docs.astral.sh/uv/guides/projects/#managing-dependencies):

`uv add --dev "pytest>=8.3.2"`

Note: similarly to remove packages, just replace `add` with `remove`. If you manually add/remove a package to/from the pyproject.toml file, remember to run the command `uv sync` to ensure that the uv.lock file also gets synced. The uv.lock file contains all the package config and should not be manually altered.

That is it in terms of setting up and running in UV venvs. In case you want to run any scripts try the `uv run <script_name>.py` command. UV is still quite new to a lot of developers so take the time to read the docs.

# Pytest

Now that the virtual environment is set up, you can now use python such as running tests. Pytest is a package installed earlier and the command below runs pytest against the tests subfolder. If the tests succeed, a coverage report is also created - this shows how much of the code is covered by tests, aiming for 100%.

`uv run -m pytest tests && uv run coverage report -m`

If the cover is less than 100%, the report will output the lines where code isn't covered. Parameters can be added to test specifix scripts or even specific functions. Ex: `uv run -m pytest tests/test_file_uploads.py::test_get_filenames`

If you need to run any scripts, as no infrastructure has been set up to run them just yet you can use the command `uv run <script_name>.py`.


To get terraform up and running on your local machine, terraform must be initialised which involves installing providers, in this case, terraform itself and AWS.

# Terraform

`terraform init`

Before any further terraform commands can be ran, terraform needs to know what to compare against. The plan/apply/destroy steps involve look at what is in the code against what resources currently exist. To know what currently exists, we need to pass credentials through so terraform can look at out AWS account. 

GloudGuru will provide several log in details, some include logging into the UI (url, username, and password), and also the information we are interested in for connecting up our repository which is the `AWS_ACCESS_KEY_ID` and the `AWS_SECRET_ACCESS_KEY`. As the sandbox is constantly being recreated, we will not save a profile instead typing this out every time into the terminal. Once a permanent account is created, then some profiles can be made and stored locally.

Paste the variables into the terminal and enter the required keys, according to your [machine](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html), below is Mac:

`export AWS_ACCESS_KEY_ID="key"`

`export AWS_SECRET_ACCESS_KEY="secret_key"`

This next step compares the differences between the code and what exists in the account. If the code has S3 section removed and it exists in the AWS account, terraform will show a plan that will mention that the S3 bucket will be destroyed. The plan shows all the changes, including any small changes, creations, and destructions.

`terraform plan`

Once you're happy with the plan, you can then apply the changes using the command below. This step also includes the plan but best to use the commands separetly to be safe, it will ask you to confirm the changes after displaying the plan.

`terraform apply`

Once the infrastructure has been applied, you can confirm this by logging onto AWS or using the command `terraform state list`, you can also use `terraform state [resource.reference_name]` to show you the specifics of a single resource.

When the resources are no longer required, you can use the command below. This is useful from both a cost and green perspective as you don't want to spin up resources longer than what is required.

`terraform destroy`

When you are done working, you can exit the virtual environment using the command below.

`source deactivate`

# Useful extensions

If you are using Visual Studio Code, look into the following extensions:

Python

Hashicorp Terraform

Gitlens

Rainbow CSV

Live Share

[Terraform docs](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources)
