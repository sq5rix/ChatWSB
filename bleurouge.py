import nltk
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from rouge_score import rouge_scorer

# Ensure necessary nltk resources are downloaded
nltk.download('punkt')

def calculate_bleu(reference, candidate):
    reference_tokens = [nltk.word_tokenize(reference)]
    candidate_tokens = nltk.word_tokenize(candidate)
    smoothing_function = SmoothingFunction().method1
    bleu_score = sentence_bleu(reference_tokens, candidate_tokens, smoothing_function=smoothing_function)
    return bleu_score

def calculate_rouge(reference, candidate):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    scores = scorer.score(reference, candidate)
    return scores

def main():
# Sample reference and candidate strings
    reference_text = "The quick brown fox jumps over the lazy dog."
    candidate_text = "The fast brown fox leaps over the lazy dog."

# Calculate BLEU score
    bleu = calculate_bleu(reference_text, candidate_text)
    print(f"BLEU Score: {bleu}")

# Calculate ROUGE scores
    rouge = calculate_rouge(reference_text, candidate_text)
    print(f"ROUGE Scores: {rouge}")

if __name__ == "__main__":
    #all = read_all_files()
    main()
