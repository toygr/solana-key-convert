# What's this?

This is script to convert id.json file to base58-encoded private key string and vice versa.

# How to use?

- ## Establish virtual env

  - Create virtual environment

    ```
    python -m venv env
    ```

  - Activate virtual environment

    - Windows

      ```
      .\env\Scripts\activate
      ```

    - Linux

      ```
      source ./env/bin/activate
      ```

- ## Install dependencies

  ```
  pip install -r requirements.txt
  ```

- ## Use script

  ```
  python json2priv.py
  python priv2json.py
  ```

  In each script file, you should input id.json or private key string

  > secret_key_list = [] # UInt8[64]

  > private_key_in_bs58 = "" # Private key in base58 exported from wallet
