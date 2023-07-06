# MyFirstAPI
This repository contains the necessary files to create lamba function and payload to test the functionality.

# Contents of this repository
- `lambda_function.py`: Contains the logic that gets the input string, search and replace the word.
- `sample_payload.json`: Sample payload with required inputs.

# API's URL
https://w9b0z71aq7.execute-api.eu-west-1.amazonaws.com/dev/testing

- Note: Only the POST method is allowed for this API endpoint. Ensure that you use the correct method while making the request.

# Request Payload:
The Lambda function expects a JSON payload with the following keys:

- `input_string` (string): The original string that needs to be modified.
- `word_to_replace` (string): The word that should be replaced within the input string.
- `replacement_word` (string): The word that will replace the `word_to_replace` within the input string.