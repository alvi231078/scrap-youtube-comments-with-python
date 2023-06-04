class Comment:
    def __init__(self, number, commenter_name, comment):
        self.number = number
        self.commenter_name = commenter_name
        self.comment = comment

    def display(self):
        print(f"Comment #{self.number}")
        print(f"Commenter Name: {self.commenter_name}")
        print(f"Comment: {self.comment}")
        print()


def parse_comments(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
#lines er moddhe eigula load koira store korsii
    comments = []
    comment_data = {}
    for line in lines:
        if line.startswith("Comment:"):
            comment_data['comment'] = line.split("Comment:")[1].strip()
        elif line.startswith("Commenter Name:"):
            comment_data['commenter_name'] = line.split("Commenter Name:")[1].strip()
        elif line.strip() == '':
            if comment_data:
                comment = Comment(len(comments) + 1, comment_data['commenter_name'], comment_data['comment'])
                comments.append(comment)
                comment_data = {}

    return comments



def search_comments(comments, keyword):
    found_comments = []
    for comment in comments:
        if keyword.lower() in comment.comment.lower():
            found_comments.append(comment)
    return found_comments


def main():
    filename = 'youtube_comments.txt'
    comments = parse_comments(filename)

    while True:
        keyword = input("Enter a keyword to search for (or 'exit' to quit): ")
        if keyword.lower() == 'exit':
            break

        found_comments = search_comments(comments, keyword)
        if found_comments:
            print(f"Found {len(found_comments)} comment(s) matching the keyword '{keyword}':")
            for comment in found_comments:
                comment.display()
        else:
            print(f"No comments found matching the keyword '{keyword}'.")

if __name__ == '__main__':
    main()
