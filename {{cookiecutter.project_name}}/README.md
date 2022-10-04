# {{ cookiecutter.project_name }}

[Latest files](https://flatgithub.com/<repo>/blob/<branch>/output/result.json?filename=<path>)

## Setup

1. Run `python -m .venv` to create a virtual environment.
2. Run `pip install -r requirements.txt` and `pip install -r requirements_local.txt` to install requirements.
3. Run `python main.py` to run the scraper.


## Using datamodel-code-generator to generate models from JSON

1. Download JSON file locally e.g. as `result.json`
2. Run ` make codegen path=<path_file>.json name=<model_name>` to create the model in `models`. 
3. Create a `request` to download the data and parse the response into the Model.