import os
import boto3

__author__ = "Valentin Bakin"

client = boto3.client('lambda')
layer_change_key = 'SOSW_LAYER_PLACEHOLDER'
test_layer_name = "sosw"
resource_types = ['AWS::Serverless::Function', 'AWS::Lambda::Function']


def main():
    try:
        response = get_lambda_layer_version(test_layer_name)
        print(response)
        if response:
            change_lambda_layer_version(response, layer_change_key, resource_types)
    except RuntimeError as r:
        raise RuntimeError(f"Something went wrong: {r}")


def get_lambda_layer_version(layer_name: str) -> dict:
    response = client.list_layer_versions(LayerName=layer_name)
    return response


def change_lambda_layer_version(response: dict, change_key: str, resources_to_change: list[str]):
    layer_version = response['LayerVersions'][0]['Version']
    print(f"Layer version: {layer_version}")
    print(f"Change key: {change_key}")

    for root, dirs, files in os.walk('.'): # Use it only if you need scan files in all repository
        for fname in files:
            if not fname.endswith('.yaml'):
                continue

            with open(fname, 'r') as f:
                data = f.read()
                if not contains_resource_type(data, resources_to_change):
                    print("Resource to change not found")
                    continue

            with open(fname, "w") as f:
                f.write(data.replace(change_key, str(layer_version)))


def contains_resource_type(data: str, resource_types_to_check: list[str]) -> bool:
    for resource_type in resource_types_to_check:
        if resource_type in data:
            print(f"Found resource type in line: {resource_type}")
            return True
    return False


if __name__ == "__main__":
    main()
