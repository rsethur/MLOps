# Code for auto generating a recipe (azure devops YAML template) based on the CLI Spec
# Instructions for usage:
# 1. Copy the CLI spec from the docs (e.g. https://docs.microsoft.com/en-us/cli/azure/ext/azure-cli-ml/ml/model?view=azure-cli-latest#ext-azure-cli-ml-az-ml-model-register)
#    Format it like this in a file e.g. cli_spec.txt
#    az ml model register
#    --name
#    --asset-path
#    --cc
#   Note:
#       (a) remove the square brackets and tab from the cli spec
#       (b) the first paramter "--name" is in second line (in the cli spec it is in the first line itself)
#       (c) remove the last parameter -v (this program generates parameters with double dash i.e. --).
#
# 2. Run this program by passing two parameters (clispec and output yaml template):
# example: --input_file private/yaml/IaC/ProvisionAMLCompute/cli_spec.txt --output_file private/yaml/IaC/ProvisionAMLCompute/out.yml
#
# 3. Edit the yaml file (change job name etc).
from ruamel.yaml import YAML
import argparse
import sys

YML_TEMPLATE_PATH = "models/utils/devops/template.yml"

def parseCLISpec(input_file_path):
    firstLine = True

    with open(input_file_path, 'r') as f:
        cli_cmd = ""
        params =[]
        for line in f:
            line = line.strip()
            if firstLine:
                cli_cmd = line
                firstLine = False
            else:
                if line[0:2] != "--":
                    print("Warning: ignoring parameter since it does not start with two leading hypens: ",line)
                line = line[2:]
                #replace hypen by underscore. Since there are problems with how azure devops handles this: https://stackoverflow.com/questions/57586664/using-dash-as-part-of-key-name-in-paramters-azure-pipelines
                #line = line.replace("-","_")
                params.append(line)

    return cli_cmd, params

def main():
    input_file_path, output_file_path = getRuntimeArgs()
    yaml_parser = YAML()

    #parse the cli command and the parameters
    cli_cmd, params = parseCLISpec(input_file_path)
    print(cli_cmd)
    print(params)

    # load yml base template
    with open(YML_TEMPLATE_PATH, 'r') as yml_template_stream:
        yml = yaml_parser.load(yml_template_stream)

    # Update the base yaml with new cli spec
    updateYMLWithCLISpec(yaml_parser, cli_cmd, params, yml)

    # write it out
    yaml_parser.dump(yml, sys.stdout)
    with open(output_file_path, 'w') as output_stream:
        yaml_parser.dump(yml, output_stream)

def updateYMLWithCLISpec(yaml_parser, cli_cmd, params, yml):
    #insert the parameters
    for param in params:
        yml["parameters"][param] = None

    #update the cli command
    yml["jobs"][0]["variables"]["cli-cmd"] = cli_cmd

    #construct the complete cli
    cli_input = "${{ variables['cli-cmd'] }}"
    for param in params:
        cli_input += "${{{{ variables['{}-cli'] }}}}".format(param)

    yml["jobs"][0]["variables"]["cli-input"] = cli_input
    #yml["jobs"][param] = None

def getRuntimeArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', type=str)
    parser.add_argument('--output_file', type=str)
    args = parser.parse_args()
    return args.input_file, args.output_file

if __name__ == "__main__":
    main()