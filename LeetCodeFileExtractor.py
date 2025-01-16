import requests
import zipfile
import os
import re

# Define paths in a platform-independent way
uploaded_file_path = (
    r"E:\LeetCode_Problems.zip"  # Use raw string for Windows-style path
)
extracted_folder_path = os.path.join(
    os.getcwd(), "LeetCode_Problems"
)  # Extract to current working directory

# Extract the zip file to a folder
with zipfile.ZipFile(uploaded_file_path, "r") as zip_ref:
    zip_ref.extractall(extracted_folder_path)

# Verify extracted files
extracted_files = os.listdir(extracted_folder_path)
# print("Extracted Files:", extracted_files)

# Define the folder containing the problems
problem_folder_path = os.path.join(extracted_folder_path, "LeetCode_Problems")
inner_files = os.listdir(problem_folder_path)
# print("Problem Files:", inner_files)

# Extract problem numbers
problem_files = [f for f in inner_files if re.search(r"_\d+\.", f)]
problem_numbers = sorted(
    set(int(re.search(r"_(\d+)\.", f).group(1)) for f in problem_files)
)

# Display results
# print("First 10 Problem Numbers:", problem_numbers[:10])
# print("Total Problem Numbers:", len(problem_numbers))


# Fetch the problem data from LeetCode's API
response = requests.get("https://leetcode.com/api/problems/all/")
data = response.json()

# Extract the list of problems
problems = data["stat_status_pairs"]

# Create a mapping from problem number to difficulty
difficulty_map = {}
for problem in problems:
    problem_id = problem["stat"]["frontend_question_id"]
    difficulty_level = problem["difficulty"]["level"]
    # Map difficulty level to its string representation
    if difficulty_level == 1:
        difficulty = "Easy"
    elif difficulty_level == 2:
        difficulty = "Medium"
    elif difficulty_level == 3:
        difficulty = "Hard"
    difficulty_map[problem_id] = difficulty

# Your list of problem numbers
# problem_numbers = [6, 26, 128, 179, 214, 241, 386, 432, 440, 494]

# Classify your problems
classified_problems = {
    num: difficulty_map.get(num, "Unknown") for num in problem_numbers
}

# Print the classified problems
cnt = 0
for num, difficulty in classified_problems.items():
    if difficulty == "Hard":
        cnt += 1
        print(f"Problem {num}: {difficulty}")
print(cnt)

