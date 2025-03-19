telugu_mapping = {
    "zero": "సున్నా",
    "one": "ఒకటి",
    "two": "రెండు",
    "three": "మూడు",
    "four": "నాలుగు",
    "five": "అయిదు",
    "six": "ఆరు",
    "seven": "ఏడు",
    "eight": "ఎనిమిది",
    "nine": "తొమ్మిది",
    "o": "సున్నా"
}

def translate_actual_text(actual_file, output_file):
    with open(actual_file, 'r', encoding='utf-8') as f, open(output_file, 'w', encoding='utf-8') as out:
        for line in f:
            words = line.strip().split()  
            translated_words = [telugu_mapping.get(word, word) for word in words]  
            out.write(" ".join(translated_words) + "\n")  

actual_file = "/home/sricharan/Music/text_files/test_source.txt"  
output_file = "test_actual_telugu.txt"
translate_actual_text(actual_file, output_file)
