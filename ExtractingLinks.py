# Write Python code that extracts all the links in the given page.

def get_next_target(page):
    """Returns the next target in the (seed) page."""
    start_link = page.find('href=')

    if start_link == -1:
        return None, 0

    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)

    url = page[start_quote + 1:end_quote]

    return url, end_quote

def get_all_links(page):
    """Returns all the links in the given (seed) page."""
    links = []
    while True:
        url, end_pos = get_next_target(page)
        if url:
            links.append(url)
            page = page[end_pos:]
        else:
            break
    return links

print get_all_links('''<div id="top_bin"> <div id="top_content" class="width960">
   <div class="udacity float-left"> <a href="/">
   <div class="udacity float-right"> <a href="https://sankarsankampa.com">''')
