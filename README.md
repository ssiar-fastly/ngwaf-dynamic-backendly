# NGWAF Dynamic Backendly

## Overview
The "NGWAF Dynamic Backendly" project is designed to interact with Fastly's API to manage backends dynamically. It provides a utility to list all backends for a specified service and version in Fastly, focusing specifically on checking the `ssl_check_cert` property for each backend. This is particularly useful for ensuring that each origin has the proper configuration before enabling dynamic backend features in network and web application firewall (NGWAF) environments.

## Requirements
- Python 3.x
- `fastly` Python package

## Installation
To set up your environment for running this script, you need to install the required Fastly Python package. You can install these packages using `pip`. Run the following command in your terminal:

```bash
pip install fastly
```

## Usage
To use this script, follow the steps below:

1. **Start the Script**:
   Open your command line interface and navigate to the directory containing the script `ngwaf-dynamic-backendly.py`.

2. **Run the Script**:
   Execute the script by running:
   ```bash
   python ngwaf-dynamic-backendly.py
   ```

3. **Enter Required Inputs**:
   When prompted, enter your Fastly API token, the service ID, and the version ID. These inputs are crucial for fetching the backend details.

   Example inputs:
   ```
   Enter your Fastly API token: your_fastly_api_token_here
   Enter the service ID: SU1Z0isxPaozGVKXdv0eY
   Enter the version ID: 1
   ```

4. **Output**:
   The script will output the `ssl_check_cert` status for each backend associated with the given service and version. This helps in verifying SSL/TLS certificate checks.

   Example output:
   ```
   Backend name: test-backend, SSL Check Cert: True
   ```

## Contributing
Contributions to "NGWAF Dynamic Backendly" are welcome! If you would like to contribute, please fork the repository and submit a pull request with your proposed changes.

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Contact
Sina Siar - [@ssiar](https://linkedin.com/in/ssiar) - ssiar@fastly.com
