def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]

# Example usage
word = "A man, a plan, a canal: Panama"
print(f"'{word}' is a palindrome: {is_palindrome(word)}")