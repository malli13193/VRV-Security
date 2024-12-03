import re
import csv
from collections import Counter, defaultdict

# File name
log_file = "sample.log"

# Parse the log file
def parse_log(file_path):
    with open(file_path, 'r') as file:
        logs = file.readlines()
    return logs

# Count requests per IP address
def count_requests_by_ip(logs):
    ip_pattern = r"^(\d+\.\d+\.\d+\.\d+)"
    ip_counter = Counter(re.match(ip_pattern, log).group(1) for log in logs)
    return ip_counter

# Identify the most frequently accessed endpoint
def most_frequent_endpoint(logs):
    endpoint_pattern = r"\"[A-Z]+ (/\S*)"
    endpoint_counter = Counter(re.search(endpoint_pattern, log).group(1) for log in logs if re.search(endpoint_pattern, log))
    most_common = endpoint_counter.most_common(1)
    return most_common[0] if most_common else ("None", 0)

# Detect suspicious activity
def detect_suspicious_activity(logs, threshold=10):
    failed_login_pattern = r" (\d{3}) .+\"Invalid credentials\""
    ip_pattern = r"^(\d+\.\d+\.\d+\.\d+)"
    failed_attempts = defaultdict(int)

    for log in logs:
        if re.search(failed_login_pattern, log) and re.search(ip_pattern, log):
            ip = re.match(ip_pattern, log).group(1)
            failed_attempts[ip] += 1

    suspicious_ips = {ip: count for ip, count in failed_attempts.items() if count > threshold}
    return suspicious_ips

# Save results to a CSV
def save_to_csv(results, filename):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        # Requests per IP
        writer.writerow(["Requests per IP"])
        writer.writerow(["IP Address", "Request Count"])
        writer.writerows(results['requests_by_ip'].items())

        # Most accessed endpoint
        writer.writerow([])
        writer.writerow(["Most Accessed Endpoint"])
        writer.writerow(["Endpoint", "Access Count"])
        writer.writerow(results['most_accessed_endpoint'])

        # Suspicious activity
        writer.writerow([])
        writer.writerow(["Suspicious Activity"])
        writer.writerow(["IP Address", "Failed Login Count"])
        writer.writerows(results['suspicious_activity'].items())

# Main script
if __name__ == "__main__":
    logs = parse_log(log_file)
    
    # Count requests by IP
    requests_by_ip = count_requests_by_ip(logs)

    # Most frequently accessed endpoint
    most_accessed_endpoint = most_frequent_endpoint(logs)

    # Detect suspicious activity
    suspicious_activity = detect_suspicious_activity(logs)

    # Print results
    print("Requests per IP:")
    for ip, count in requests_by_ip.items():
        print(f"{ip:<20}{count}")

    print("\nMost Frequently Accessed Endpoint:")
    print(f"{most_accessed_endpoint[0]} (Accessed {most_accessed_endpoint[1]} times)")

    print("\nSuspicious Activity Detected:")
    for ip, count in suspicious_activity.items():
        print(f"{ip:<20}{count}")

    # Save to CSV
    results = {
        "requests_by_ip": requests_by_ip,
        "most_accessed_endpoint": most_accessed_endpoint,
        "suspicious_activity": suspicious_activity
    }
    save_to_csv(results, "log_analysis_results.csv")
