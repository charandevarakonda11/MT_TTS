import jiwer
import numpy as np

with open('/home/sricharan/Music/text_files/test_actual_telugu.txt', 'r', encoding='utf-8') as ref_file:
    references = [line.strip() for line in ref_file if line.strip()]

with open('/home/sricharan/Music/text_files/test_predicted_telugu.txt', 'r', encoding='utf-8') as pred_file:
    predictions = [line.strip() for line in pred_file if line.strip()]

# Option 1: Compute corpus-level WER (treating entire files as one text)
reference_text = "\n".join(references)
predicted_text = "\n".join(predictions)
corpus_wer = jiwer.wer(reference_text, predicted_text)
print("Corpus-level WER:", corpus_wer)


