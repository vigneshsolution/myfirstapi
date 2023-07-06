def lambda_handler(event, context):
    input_string = event['input_string']
    word_to_replace = event['word_to_replace']
    replacement_word = event['replacement_word']
    
    if not word_to_replace:
        return {
            'error': 'word_to_replace cannot be empty'
        }
        
    if word_to_replace not in input_string:
        return {
            'error': 'word_to_replace does not exist in the input_string'
        }
    
    modified_string = input_string.replace(word_to_replace, replacement_word)

    return {
        'modified_string': modified_string
    }