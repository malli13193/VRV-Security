# VRV-Security
VRV Security’s to Detect Suspicious Activity of different web addresses.
# Log File Analyzer

## Description

The **Log File Analyzer** is a Python script designed to process and analyze log files, extracting key insights such as request counts, popular endpoints, and detecting suspicious activities. This tool is tailored for cybersecurity-related tasks, leveraging file handling, string manipulation, and data analysis.

---

## Features

1. **Count Requests per IP Address**  
   - Parses the log file to extract IP addresses.  
   - Counts the number of requests made by each IP.  
   - Displays results sorted in descending order of request count.  

2. **Identify the Most Frequently Accessed Endpoint**  
   - Extracts endpoints (URLs or resource paths) from the log file.  
   - Identifies the most frequently accessed endpoint.  

3. **Detect Suspicious Activity**  
   - Searches for failed login attempts (e.g., HTTP 401 errors or "Invalid credentials").  
   - Flags IP addresses with failed login attempts exceeding a configurable threshold (default: 10).  

4. **Output Results**  
   - Displays results in the terminal for quick viewing.  
   - Saves results to a CSV file named `log_analysis_results.csv`.  

---

## Example Outputs

### Terminal Output
Requests per IP: 192.168.1.1 6 203.0.113.5 8 10.0.0.2 5 198.51.100.23 7

Most Frequently Accessed Endpoint: /home (Accessed 5 times)

Suspicious Activity Detected: 203.0.113.5 8 192.168.1.100 12

### CSV Output
The results are saved in the following structure:
- **Requests per IP**: IP Address, Request Count  
- **Most Accessed Endpoint**: Endpoint, Access Count  
- **Suspicious Activity**: IP Address, Failed Login Count  

---

## Installation and Usage

### Prerequisites
- Python 3.x installed on your machine.

### Steps
1. Clone this repository to your local machine:
   ```bash
  [ git clone https://github.com/your-username/log-file-analyzer.git](https://github.com/malli13193/VRV-Security.git)
   cd log-file-analyzer
Place your log file in the same directory as the script. Ensure the file is named sample.log or adjust the script accordingly.
Run the script:

python log_analysis.py

View the output in the terminal and check the CSV file log_analysis_results.csv for detailed results.

Configuration
The threshold for detecting suspicious activities (failed login attempts) can be customized:

Open log_analysis.py.
Locate the detect_suspicious_activity function.
Adjust the threshold parameter as needed (default is 10).



Here’s a README.md file you can use for your GitHub repository:

markdown
Copy code
# Log File Analyzer

## Description

The **Log File Analyzer** is a Python script designed to process and analyze log files, extracting key insights such as request counts, popular endpoints, and detecting suspicious activities. This tool is tailored for cybersecurity-related tasks, leveraging file handling, string manipulation, and data analysis.

---

## Features

1. **Count Requests per IP Address**  
   - Parses the log file to extract IP addresses.  
   - Counts the number of requests made by each IP.  
   - Displays results sorted in descending order of request count.  

2. **Identify the Most Frequently Accessed Endpoint**  
   - Extracts endpoints (URLs or resource paths) from the log file.  
   - Identifies the most frequently accessed endpoint.  

3. **Detect Suspicious Activity**  
   - Searches for failed login attempts (e.g., HTTP 401 errors or "Invalid credentials").  
   - Flags IP addresses with failed login attempts exceeding a configurable threshold (default: 10).  

4. **Output Results**  
   - Displays results in the terminal for quick viewing.  
   - Saves results to a CSV file named `log_analysis_results.csv`.  

---

## Example Outputs

### Terminal Output
Requests per IP: 192.168.1.1 6 203.0.113.5 8 10.0.0.2 5 198.51.100.23 7

Most Frequently Accessed Endpoint: /home (Accessed 5 times)

Suspicious Activity Detected: 203.0.113.5 8 192.168.1.100 12

yaml
Copy code

### CSV Output
The results are saved in the following structure:
- **Requests per IP**: IP Address, Request Count  
- **Most Accessed Endpoint**: Endpoint, Access Count  
- **Suspicious Activity**: IP Address, Failed Login Count  

---



## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
This project is developed to demonstrate Python's file handling and data analysis capabilities, emphasizing real-world use cases in cybersecurity.



Replace `"malli13193"` in the repository URL with your GitHub username to customize it 

