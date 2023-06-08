class CommentProto:
    def __init__(self, number, commentName, commentData):
        self.number = number
        self.commentName = commentName
        self.commentData = commentData


class FileHandling:
    def __init__(self, source):
        self.source = source

    def coreFunc(self):
        with open(self.source, 'r') as srcFile:
            lines = srcFile.readlines()
            i = 0
            li = []
            commenter_name = ''
            while i < len(lines):
                if lines[i].startswith('Commenter Name'):
                    commenter_name = lines[i].split(':', 1)[1].strip()
                    i += 1
                    comment_holder = ''
                    while i < len(lines) and not lines[i].startswith('Commenter Name'):
                        if lines[i].startswith('Comment'):
                            comment_holder = lines[i].split(':', 1)[1].strip()
                            i += 1
                        else:
                            comment_holder += lines[i]
                            i += 1
                    carry = CommentProto(len(li), commenter_name, comment_holder)
                    li.append(carry)
                else:
                    i += 1
            return li


def search_func(key, database):
    li2 = []
    for item in database:
        if key.lower() in item.commentName.lower() or key.lower() in item.commentData.lower():
            li2.append(item)

    return li2


while True:
    print("Comment Searcher v1.0 | Created By Alvi \n type 'stop' to end this process!")
    inputOfSearch = input('Enter any Keyword for search: ')
    if inputOfSearch.lower() == 'stop':
        break
    dataSourceMain = 'youtube_comments.txt'
    n = FileHandling(dataSourceMain)
    sortedList = n.coreFunc()
    resultofsearch = search_func(inputOfSearch, sortedList)
    for item in resultofsearch:
        print(f'#Comment No: {item.number}')
        print(f'#Commenter Name: {item.commentName}')
        print(f'#Comment: {item.commentData}')
        print('-----------------------------------------')
    print(f" This many results found for your query '{inputOfSearch}' - ({len(resultofsearch)})")
