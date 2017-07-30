# Define a procedure, lookup,
# that takes two inputs:

# - an index
# - keyword

# The procedure should return a list
# of the urls associated
# with the keyword. If the keyword
# is not in the index, the procedure
# should return an empty list.

index = [['udacity', ['http://udacity.com', 'http://npr.org']],
         ['computing', ['http://acm.org']]]

def lookup(index, keyword):
    """Lookups an index for the given keyword and returns the URLs
        that contain the keyword."""
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return []

print lookup(index, 'udacity')
print lookup(index, 'k3rn31p3nic')
