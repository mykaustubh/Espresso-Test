import os
import subprocess
import yaml

# Load configuration from YAML file
def load_yaml_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Check if device is connected
def check_device_connected(device_id):
    output = subprocess.check_output(["adb", "devices"]).decode("utf-8")
    if device_id not in output:
        print(f"Device '{device_id}' is not connected.")
        return False
    return True

# Run test for a specific test class
def run_test(device_id, test_class, package, test_runner):
    command = f"adb -s {device_id} shell am instrument -w -r -e class {test_class} {package}.test/{test_runner}"
    print(f"Running command: {command}")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"Test class '{test_class}' completed successfully.")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Test class '{test_class}' failed to run.")
        print(e.stderr)

# Main function to run all tests
def run_all_tests():
    config = load_yaml_config("config.yaml")

    package = config.get("package", "")
    test_runner = config.get("test_runner", "")
    device = config.get("device", "")
    test_classes = config.get("class", [])

    if not check_device_connected(device):
        return

    for test_class in test_classes:
        run_test(device, test_class, package, test_runner)

if __name__ == "__main__":
    run_all_tests()
