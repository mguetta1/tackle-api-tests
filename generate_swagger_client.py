import os
import shutil
import tempfile

import yaml
from github import Github


def download_swagger_yaml(temp_dir, branch_name):
    repo_name = "tackle2-hub"
    repo_owner = "konveyor"

    # Initialize the PyGithub client
    g = Github()

    try:
        # Get the repository
        repo = g.get_repo(f"{repo_owner}/{repo_name}")

        # Get the contents of the Swagger YAML file from the provided branch
        file_contents = repo.get_contents(path="docs/swagger.yaml", ref=branch_name)

        # Download the Swagger YAML file to the temporary directory
        download_url = file_contents.download_url
        file_path = os.path.join(temp_dir, "swagger.yaml")
        os.system(f"wget {download_url} -O {file_path}")
        print(f"Swagger YAML file downloaded to {file_path} successfully!")

        #
        # Edit swagger.yaml file with info and security sections
        #
        data_to_add = {
            "info": {"version": branch_name},
            "securityDefinitions": {"bearerAuth": {"type": "apiKey", "in": "header", "name": "Authorization"}},
            # To apply Basic auth to the whole API:
            "security": [{"bearerAuth": []}],
        }

        # Load the existing YAML data from the file
        with open(file_path, "r") as file:
            existing_data = yaml.safe_load(file)

        # Modify the data by adding more rows
        for key, value in data_to_add.items():
            existing_data[key] = value

        # Save the modified data back to the YAML file
        with open(file_path, "w") as file:
            yaml.dump(existing_data, file, default_flow_style=False)
        print("Rows added successfully.")

        return file_path

    except Exception as e:
        print(f"Error: {e}")


def generate_swagger_client_library(temp_dir):
    try:
        # Save the current working directory
        cwd = os.getcwd()

        # Change the current working directory
        os.chdir(temp_dir)

        # Download swagger-codegen-cli tool
        print("Downloading swagger-codegen-cli tool...")
        tool_path = os.path.join(temp_dir, "swagger-codegen-cli.jar")
        url = "https://repo1.maven.org/maven2/io/swagger/swagger-codegen-cli/2.4.32/swagger-codegen-cli-2.4.32.jar"
        os.system(f"wget {url} -O {tool_path} >/dev/null 2>&1")
        print(f"swagger-codegen-cli tool downloaded to {tool_path} successfully!")

        # Generate a Python client library
        print("Generating the client library...")
        os.system("java -jar swagger-codegen-cli.jar generate -i swagger.yaml -l python >/dev/null 2>&1")
        print("The client library was generated successfully!")

        # Set swagger_client.configuration.verify_ssl = False
        search_line = "self.verify_ssl = True\n"
        replace_line = "self.verify_ssl = False\n"
        conf_file = "swagger_client/configuration.py"
        with open(conf_file, "r") as file:
            lines = file.readlines()
        found = False
        for i, line in enumerate(lines):
            if search_line in line:
                lines[i] = replace_line
                found = True
                break
        if not found:
            print(f"Line '{search_line}' not found in the file.")
            return

        # Write the modified content back to the file
        with open(conf_file, "w") as file:
            file.writelines(lines)

        os.chdir(cwd)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmpdirname:
        branch_name = input("Enter the branch name: ")
        swagger_file = download_swagger_yaml(tmpdirname, branch_name)
        generate_swagger_client_library(tmpdirname)
        cliend_dir = "swagger_client"
        source_dir = os.path.join(tmpdirname, cliend_dir)
        destination_dir = os.path.join(os.getcwd(), cliend_dir)
        # Remove existing swagger_client directory
        shutil.rmtree(destination_dir, ignore_errors=True)
        shutil.copytree(source_dir, destination_dir)
