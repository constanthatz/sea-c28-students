def safe_input(prompt="What?: "):
    """Return user imput or exiting program when KeyboardInterrupt or EOFError
    is caught"""
    try:
        input = raw_input(prompt)
    except (EOFError, KeyboardInterrupt):
        return None
    else:
        return input
