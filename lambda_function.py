import string
import secrets

headers = {
    'Access-Control-Allow-Origin': '*',  # Replace '*' with your frontend domain if known
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Allow-Methods': 'OPTIONS,POST'
}

def generate_password(length, use_uppercase, use_lowercase, use_special_chars, use_numbers, exclude_chars):
    characters = ''

    if use_uppercase:
        characters += string.ascii_uppercase

    if use_lowercase:
        characters += string.ascii_lowercase

    if use_special_chars:
        characters += string.punctuation

    if use_numbers:
        characters += string.digits

    if exclude_chars:
        characters = characters.translate(str.maketrans('', '', exclude_chars))

    if not characters:
        return "Error: You must select at least one character type."

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def lambda_handler(event, context):
    # Extract parameters from the event object (input from API Gateway)
    length = int(event['length'])
    use_uppercase = event['use_uppercase']
    use_lowercase = event['use_lowercase']
    use_special_chars = event['use_special_chars']
    use_numbers = event['use_numbers']
    exclude_chars = event['exclude_chars']

    # Call the password generation function with the extracted parameters
    password = generate_password(length, use_uppercase, use_lowercase, use_special_chars, use_numbers, exclude_chars)

    # Return the generated password as the response
    return {
        'statusCode': 200,
        'body': {
            'password': password
        },
        'headers': {
            'Content-Type': 'application/json'
        }
    }
