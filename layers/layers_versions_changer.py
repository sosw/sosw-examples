import os
import boto3
import yaml
from yaml import Loader, SafeLoader


def sub_constructor(loader, node):
    value = loader.construct_scalar(node)
    return {"Fn::Sub": value}


Loader.add_constructor('!Sub', sub_constructor)
SafeLoader.add_constructor('!Sub', sub_constructor)


client = boto3.client('lambda')
layer_change_key = 'SOSW_LAYER'
curr_runtime = 'python3.11'
test_layer_name = "sosw"


def main():
    try:
        response = get_lambda_layer_version(curr_runtime, test_layer_name)
        print(response)
        if response:
            change_lambda_layer_version(response, layer_change_key)
    except RuntimeError as r:
        raise RuntimeError(f"Something went wrong: {r}")


def get_lambda_layer_version(runtime: str, layer_name: str) -> dict:
    response = client.list_layer_versions(CompatibleRuntime=runtime, LayerName=layer_name)
    return response


def change_lambda_layer_version(response: dict, change_key: str):
    layer_version = response['LayerVersions'][0]['Version']
    print(f"Layer version: {layer_version}")
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.yaml'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    yaml_data = yaml.safe_load(f)
                    if change_key in yaml_data:
                        yaml_data[change_key] = layer_version
                        with open(file_path, 'w') as fw:
                            yaml.dump(yaml_data, fw)


if __name__ == "__main__":
    main()
