import sacrebleu

with open('/home/sricharan/Music/text_files/test_actual_telugu.txt', 'r', encoding='utf-8') as ref_file:
    references = [line.strip() for line in ref_file if line.strip()]

with open('/home/sricharan/Music/text_files/test_predicted_telugu.txt', 'r', encoding='utf-8') as pred_file:
    predictions = [line.strip() for line in pred_file if line.strip()]

bleu = sacrebleu.corpus_bleu(predictions, [references])
print("BLEU score:", bleu.score)
