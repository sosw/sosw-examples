import os
import boto3

client = boto3.client('lambda')
layer_change_key = 'SOSW_LAYER_PLACEHOLDER'
curr_runtime = 'python3.11'
test_layer_name = "sosw"
resource_types = ['AWS::Serverless::Function', 'AWS::Lambda::Function']


def main():
    try:
        response = get_lambda_layer_version(curr_runtime, test_layer_name)
        print(response)
        if response:
            change_lambda_layer_version(response, layer_change_key,resource_types)
    except RuntimeError as r:
        raise RuntimeError(f"Something went wrong: {r}")


def get_lambda_layer_version(runtime: str, layer_name: str) -> dict:
    response = client.list_layer_versions(CompatibleRuntime=runtime, LayerName=layer_name)
    return response


def change_lambda_layer_version(response: dict, change_key: str, resource_types_to_change: list[str]):
    layer_version = response['LayerVersions'][0]['Version']
    print(f"Layer version: {layer_version}")
    print(change_key)
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.yaml'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    if contains_resource_type(f, resource_types_to_change):
                        lines = f.readlines()
                        lines = [line.replace(change_key, str(layer_version)) for line in lines]
                        with open(file_path, "w") as fw:
                            fw.writelines(lines)


def contains_resource_type(file_handle, resource_types_to_check: list[str]) -> bool:
    for line in file_handle:
        if 'Type' in line and any(resource_type in line for resource_type in resource_types_to_check):
            return True
    return False


if __name__ == "__main__":
    main()
