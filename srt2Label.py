import os
import re

def srt_to_audacity_label():
    # Prompt user to enter the path of the SRT file
    srt_file_path = input("Enter the path of the SRT file: ")
    
    # Extract the directory path and filename
    directory_path = "/".join(srt_file_path.split("/")[:-1])
    filename = srt_file_path.split("/")[-1]
    
    # Generate the path for the Audacity label file in the same directory as the SRT file
    ###audacity_label_file_path = f"{directory_path}/{filename.split('.')[0]}.txt"
    ###audacity_label_file_path = os.path.join(output_dir, os.path.splitext(os.path.basename(srt_file_path))[0] + '.txt')
    audacity_label_file_path = os.path.join(directory_path, f"{filename.split('.')[0]}.txt")


    
    with open(srt_file_path, 'r') as srt_file:
        srt_content = srt_file.read()
    
    # Use regular expressions to extract subtitle information
    subtitle_regex = r"(\d+)\n(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})\n(.+?)(?=\n\d|\Z)"
    subtitle_matches = re.findall(subtitle_regex, srt_content, re.DOTALL)
    
    # Convert subtitle information to Audacity label format
    audacity_label_content = ""
    for match in subtitle_matches:
        start_time = convert_timestamp_to_seconds(match[1])
        end_time = convert_timestamp_to_seconds(match[2])
        subtitle_text = match[3].replace('\n', ' ')
        audacity_label_content += f"{start_time:.6f}\t{end_time:.6f}\t{subtitle_text}\n"
    
    # Write Audacity label content to file
    with open(audacity_label_file_path, 'w') as audacity_label_file:
        audacity_label_file.write(audacity_label_content)

def convert_timestamp_to_seconds(timestamp):
    hours, minutes, seconds_milliseconds = timestamp.split(':')
    seconds, milliseconds = seconds_milliseconds.split(',')
    return int(hours) * 3600 + int(minutes) * 60 + int(seconds) + int(milliseconds) / 1000

srt_to_audacity_label()
