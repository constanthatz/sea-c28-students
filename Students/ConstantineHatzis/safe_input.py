def safe_input(prompt="What?: "):
    try:
        input = raw_input(prompt)
    except (EOFError, KeyboardInterrupt):
        return None
    else:
        return input
