# MaksRecon

MaksRecon is a simple recon tool designed to identify subdomains of a given domain and check their reachability. The tool utilizes Sublist3r for subdomain enumeration and Python's `requests` library for HTTP requests.

## Features

- Enumerates subdomains using Sublist3r
- Checks the reachability of each subdomain
- Outputs results in a formatted manner
- Saves reachable subdomains to a text file

## Prerequisites

Before running the tool, ensure you have the following installed:

- Python 3.x
- pip (Python package installer)

## Installation

1. **Clone the repository** (or download the files):
   ```bash
   git clone <repository_url>
   cd maksrecon
2. **Install required dependencies**
3. **Install Sublist3r**

## Usage

Run the tool from the terminal by providing a domain as a command-line argument:

python3 maksrecon.py <domain>

## Contributing

Contributions are welcome! If you have suggestions for improvements or bug fixes, please create an issue or submit a pull request.

## Acknowledgments

Sublist3r for subdomain enumeration.
