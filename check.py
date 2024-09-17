import os

def check_html_files(directory):
    # List to keep track of files where the condition is not met
    files_with_issue = []

    # Loop through each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            file_path = os.path.join(directory, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                    for i, line in enumerate(lines):
                        if "content begins" in line:
                            # Check the next line
                            next_line = lines[i + 1].strip() if (i + 1) < len(lines) else ""
                            while not next_line and (i + 1) < len(lines):
                                # Move to the next line if the current one is empty
                                i += 1
                                next_line = lines[i + 1].strip() if (i + 1) < len(lines) else ""
                            
                            if next_line != '<div style="text-align: center;">':
                                files_with_issue.append(filename)
                            break
            except Exception as e:
                print(f"Error processing file {filename}: {e}")

    return files_with_issue

# Specify the directory containing the HTML files
directory = '.'

# Call the function and get the list of files with issues
files_with_issue = check_html_files(directory)
print("Files with issues:", files_with_issue)
