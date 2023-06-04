path = 'youtube_comments.txt'

comments = {}  # Initialize the comments dictionary
current_comment_id = 1

with open(path, 'r') as comments_file:
    comment_lines = comments_file.readlines()

    line_index = 0
    while line_index < len(comment_lines):
        line = comment_lines[line_index].strip()

        if line.startswith('Commenter Name:'):
            commenter_name = line[len('Commenter Name:'):].strip()

            # Find the start and end index of the comment
            start_index = line_index
            end_index = line_index + 2
            while end_index < len(comment_lines) and not comment_lines[end_index].startswith('Commenter Name:'):
                end_index += 1

            # Extract the comment lines and join them
            comment_lines_extracted = comment_lines[start_index:end_index]
            comment = ' '.join(line.strip() for line in comment_lines_extracted)

            comments[current_comment_id] = {'Commenter Name': commenter_name, 'Comment': comment}
            current_comment_id += 1

            # Move the line index to the end of the current comment
            line_index = end_index

        line_index += 1

# Search by commenter name or comment content
search_term = input("Enter the commenter's name or a keyword from the comment: ")
found_comments = [(comment_id, comment) for comment_id, comment in comments.items() if
                  search_term.lower() in comment['Commenter Name'].lower() or
                  search_term.lower() in comment['Comment'].lower()]

if found_comments:
    for comment_id, comment in found_comments:
        print(f"Comment {comment_id}:")
        print(f"Commenter Name: {comment['Commenter Name']}")
        print(f"Comment: {comment['Comment']}")
        print()
else:
    print("No matching comments found.")
