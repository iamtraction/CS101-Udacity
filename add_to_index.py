# Define a procedure, add_to_index,
# that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]

index = []

def add_to_index(index, keyword, url):
    """Adds a keyword and an url to the index list"""
    for key in index:
        if keyword == key[0]:
            key[1].append(url)
            return
    index.append([keyword, [url]])

add_to_index(index, 'k3rn31p3nic', 'https://sankarsankampa.com')
add_to_index(index, 'k3rn31p3nic', 'https://www.sankarsankampa.com')
add_to_index(index, 'udacity', 'http://udacity.com')
add_to_index(index, 'computing', 'http://acm.org')
add_to_index(index, 'udacity', 'http://npr.org')
print index
