
# Molecular Descriptors Calculation Script

This script calculates a full list of molecular descriptors for chemical compounds represented in SMILES notation. It uses RDKit, a collection of cheminformatics and machine learning tools, and pandas, a data manipulation and analysis library.

## Prerequisites

- Python 3.x
- pip (Python package manager)
- Access to command-line interface (CLI)

## Setup and Installation

1.**Setting Up a Virtual Environment:**

   It's recommended to use a virtual environment to avoid conflicts with other Python projects or system-wide packages. To set up a virtual environment, navigate to the project directory and run the following commands:

```sh

python -m venv venv

```

   This command creates a new directory `venv` where the virtual environment files are stored. To activate the virtual environment, use:

- On Windows:

  ```sh

  ```

 venv\Scripts\activate

    ```

- On macOS and Linux:

  ```sh

  ```

 source venv/bin/activate

    ```

2.**Installing Dependencies:**

   Once the virtual environment is activated, install the required packages (RDKit and pandas) using pip:

```sh

pip install -r requirements.txt

conda install -c conda-forge rdkit

```

   Note: RDKit might have specific installation instructions based on your operating system. Refer to [RDKit Documentation](https://www.rdkit.org/docs/Install.html) for detailed installation guidelines.

## Running the Script

1.**Preparing Your Data:**

   Ensure your Excel file (`111.xlsx`) is in the same directory as the script. The file should contain SMILES notations in the second column.

2.**Executing the Script:**

   Run the script using the following command:

```sh

python descriptors.py

```

3.**Output:**

   The script will generate a new Excel file `output_with_descriptors.xlsx` containing the original data along with calculated molecular descriptors in separate columns.

## Deactivating the Virtual Environment

After running the script, you can deactivate the virtual environment by executing:

```sh

deactivate

```

This command will return you to your global Python environment.

---
