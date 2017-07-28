# Write Python code that prints all the links in the given page.

def get_next_target(page):
    start_link = page.find('href=')

    if start_link == -1:
        return None, 0

    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)

    url = page[start_quote + 1:end_quote]

    return url, end_quote

def print_all_links(page):
    while True:
        url, end_pos = get_next_target(page)
        if url:
            print url
            page = page[end_pos:]
        else:
            break

print_all_links('''<div id="top_bin"> <div id="top_content" class="width960">
   <div class="udacity float-left"> <a href="/">
   <div class="udacity float-right"> <a href="https://sankarsankampa.com">''')
