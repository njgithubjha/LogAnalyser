import re
from datetime import datetime

log_file = open("server.log", "r")  # Open the log file for reading
timestamp_list = []  # List to store timestamps

# Loop through each line in the log file
for line in log_file:
    # Use regular expressions to extract the timestamp from the log line
    timestamp_match = re.search(r'\[(.*?)\]', line)
    if timestamp_match:
        timestamp_str = timestamp_match.group(1)
        timestamp = datetime.strptime(timestamp_str, "%d/%b/%Y:%H:%M:%S %z")
        timestamp_list.append(timestamp)

# Sort the list of timestamps in ascending order
timestamp_list.sort() 

# for i in range(0, len(timestamp_list)):    
#     print(timestamp_list[i]); 

# Calculate the time range covered by the log file
start_time = timestamp_list[0]
end_time = timestamp_list[-1]
time_range = end_time - start_time
# print(time_range)

# Calculate the average time between requests
time_diffs = [(timestamp_list[i+1] - timestamp_list[i]).total_seconds() for i in range(len(timestamp_list)-1)]
avg_time_between_requests = sum(time_diffs) / len(time_diffs)
# print(avg_time_between_requests)

# Print the results
print("Start time:", start_time)
print("End time:", end_time)
print("Time range:", time_range)
print("Average time between requests:", avg_time_between_requests)

log_file.close()  # Close the log file when finished