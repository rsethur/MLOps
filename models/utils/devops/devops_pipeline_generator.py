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