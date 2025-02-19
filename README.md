This README has been created based on a machine running on Mac, so some of the Windows instructions may be lacking, please fill in any gaps found.

# Required Installation

Get terraform installed, see [Terraform CLI Installation](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli#install-terraform) for more instructions.

Python

# Pre-commits

To ensure that only properly linted and security-aligned code has been pushed, pre-commits have been added that checks over codes for linting and checks security over the terraform code. To make sure these run on your machine, install [ruff](https://docs.astral.sh/ruff/installation/), [tflint](https://aquasecurity.github.io/tfsec/v0.63.1/getting-started/installation/) and [tfsec](https://aquasecurity.github.io/tfsec/v0.63.1/getting-started/installation/). When you commit files, these checks will run against the code, please ensure you save and re-add any altered files via `git add`.

# Virtual Environments

Virtual environments are useful as they allow you to have several indepedent python versions running on your machine and it allows you to select which version you like for your repository. By having an isolated virtual environment with the same packages, you and any other developer working on the project should have the same setup.

MacOS or Linux users should look into using [pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation), Windows users should look into using [venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#create-and-use-virtual-environments). Instructions are given below for MacOS/Linux and Windows. Follow the steps below to create and activate the the virtual environments according to your OS, then move onto the Getting Started section.

## MacOS/Linux - pyenv

If you are using Mac/Linux and do not already have virtualenv installed, do so now.

`pip3 install virtualenv`

For this repo, we will be using python version 3.11.9, it is important we use the same version to ensure everything works for the same regardless of the machine it is running on.

`pyenv install 3.11.9`

Once we have the python version installed, we can now create a profile for our repo, we will call it 'poc_tf_aws' and it will use version 3.11.9.

`pyenv virtualenv 3.11.9 poc_tf_aws`

Now that the profile has been created, we can enter the virtual environment using the activate command and stating which profile we wish to activate.

`pyenv activate poc_tf_aws`

## Windows - venv

Start by going into the parent working directory which is the project folder. Then run the command below to create the .venv folder with all the required files. This will isolate your virtual environment, so long as you pick the activate file from this directory.

`py -m venv .venv`

After the `.venv` folder and the files have been created, you can then activate the env using the command:

`.venv\Scripts\activate`

# Getting started

Now that we have activated a virtual environment, we can begin our python commands, we will start by installing all the necessary packages that are listed out in the requirements.txt file.

`pip3 install -r requirements.txt`

To get terraform up and running on your local machine, terraform must be initialised which involves installing providers, in this case, terraform itself and AWS.

`terraform init`

Before any further terraform commands can be ran, terraform needs to know what to compare against. The plan/apply/destroy steps involve look at what is in the code against what resources currently exist. To know what currently exists, we need to pass credentials through so terraform can look at out AWS account. 

GloudGuru will provide several log in details, some include logging into the UI (link, username, and password), and the information we are interested in for connecting up our repository which is the `AWS_ACCESS_KEY_ID` and the `AWS_SECRET_ACCESS_KEY`. As the sandbox is constantly being recreated, we will not save a profile instead typing this out every time into the terminal.

Paste the variables into the terminal and enter the required keys, according to your [machine](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html), below is Mac:

`export AWS_ACCESS_KEY_ID="key"`

`export AWS_SECRET_ACCESS_KEY="secret_key"`

This next step compares the differences between the code and what exists in the account. If the code has S3 section removed and it exists in the AWS account, terraform will show a plan that will mention that the S3 bucket will be destroyed. The plan shows all the changes, including any small changes, creations, and destructions.

`terraform plan`

Once you're happy with the plan, you can then apply the changes using the command below. This step also includes the plan but best to use the commands separetly to be safe, it will ask you to confirm the changes after displaying the plan.

`terraform apply`

Once the infrastructure has been applied, you can confirm this by logging onto AWS or using the command `terraform state list`, you can also use `terraform state [resource.reference_name]` to show you the specifics of a single resource.

Now that the infrastructure is set up, you can now use python against the infrastrcuture such as running tests. Pytest is a package installed earlier and the command below runs pytest against the tests subfolder. If the tests succeed, a coverage report is also created - this shows how much of the code is covered by tests, aiming for 100%. 

`pytest tests && pytest --cov`

If you need to run any scripts, as no infrastructure has been set up to run them just yet you can use the command `python [filename].py`, ideally within the virtual environment. 

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
