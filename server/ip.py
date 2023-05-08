import re

log_file = open("server.log", "r")  # Open the log file for reading
timestamp_dict = {}  # Dictionary to store timestamps and their counts

# Loop through each line in the log file
for line in log_file:
    # Use regular expressions to extract the timestamp from the log line
    timestamp_match = re.search(r'\[(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2})', line)
    if timestamp_match:
        timestamp = timestamp_match.group(1)
        if timestamp in timestamp_dict:
            timestamp_dict[timestamp] += 1
        else:
            timestamp_dict[timestamp] = 1



# Print the number of unique timestamps and their counts
print("Number of unique timestamps:", len(timestamp_dict))
for timestamp, count in timestamp_dict.items():
    print(timestamp, count)

log_file.close()  # Close the log file when finished
