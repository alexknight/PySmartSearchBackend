import re


def contains_chinese(text):
    pattern = re.compile(r'[\u4e00-\u9fa5]')
    return bool(pattern.search(text))


def perform_vector_matching(query, scraped_data):
    all_info = ""
    all_len = 0
    for item in scraped_data:
        all_len += len(item)
        all_info += item
    if all_len < 600:
        return all_info, None
    return scraped_data[0], None