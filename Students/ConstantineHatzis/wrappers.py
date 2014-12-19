def p_wrapper(func):
    def paragraph_element(*args, **kwargs):
        tags = ('<p>', '</p>')
        return tags[0] + func(*args, **kwargs) + tags[1]
    return paragraph_element
