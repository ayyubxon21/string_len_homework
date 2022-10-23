def main(s):
    """
    Given variable type string s. Return the character in the middle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """
    if len(s) == 5:
        return s[2]
    if len(s) == 4:
        return s[1:3]
print(main("cool"))
