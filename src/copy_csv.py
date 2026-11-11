# Import shutil for copying files
import shutil
# Import Path for clean, cross-platform file paths
from pathlib import Path
# Import yaml to read params.yaml
import yaml


# Define the main function that does the work
def main():
    # Open the parameters file
    with open("params.yaml") as f:
        # Parse YAML into a Python dict and take the "copy" section
        params = yaml.safe_load(f)["copy"]

    # Build the source path
    source = Path(params["source"])
    # Build the destination path
    destination = Path(params["destination"])

    # Stop with a clear error if the source file is missing
    if not source.exists():
        # Raise an error explaining what is wrong
        raise FileNotFoundError(f"Source CSV not found: {source}")

    # Create the destination folder if it does not exist
    destination.parent.mkdir(parents=True, exist_ok=True)
    # Copy the CSV file from source to destination
    shutil.copy(source, destination)
    # Print a confirmation message (visible in GitHub Actions logs)
    print(f"Copied {source} -> {destination}")


# Run main() only when the script is executed directly
if __name__ == "__main__":
    # Call the main function
    main()
