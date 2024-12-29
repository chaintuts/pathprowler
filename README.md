## General
____________

### Author
* Josh McIntyre

### Website
* jmcintyre.net

### Overview
* PathProwler is a demo of a path traversal vulnerability

## Development
________________

### Git Workflow
* development for bugfixes and new features

### Building
* make build
Build the application
* make clean
Clean the build and data directories

### Features
* Takes a filename GET parameter at the /threatdatabase URL
* Legitimate filenames will display data about malware fingerprints and software vulnerabilities
* Malicious filenames will use path traversal to display the server's secret SSL/TLS key
* Takes compact JSON or CSV data and formats as HTML for easy viewing using Jinja templating

### Requirements
* Requires Python

### Platforms
* Windows
* Linux
* MacOSX

## Usage
____________

### Browser Usage
* Run the application using the built-in Flask server or another server configuration - ` python3 -m flask --app pathprowler run`
* Navigate to `/threatdatabase` URL with a GET parameter for filename `?filename=<filename>`
* Use `threatdata?filename=malwaredatabase.csv` or `threatdata?filename=vulndatabase.json` to display legitimate data
* Use `threatdata?filename=../../secret/cert.key` to trigger path traversal vulnerability, showing the server's secret SSL/TLS key
