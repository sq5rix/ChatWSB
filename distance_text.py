import spacy
from bleurouge import calculate_bleu, calculate_rouge
from rouge_score import rouge_scorer

# Load the medium English model
nlp = spacy.load("pl_core_news_lg")

# Function to convert text to a vector
def text_to_vector(text):
    doc = nlp(text)
    # Use the average of word vectors as the text vector
    # Ignore words without vectors
    vectors = [token.vector for token in doc if token.has_vector]
    if vectors:
        return sum(vectors) / len(vectors)
    else:
        return None


def policz_odleglosc(text1, text2, fun):
    """
    Convert texts to vectors
    Measure distance using fun
    """
    if not text1:
        return None
    if not text2:
        return None
    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)
    if vector1 is not None and vector2 is not None:
        # Calculate Euclidean distance
        distance = fun(vector1, vector2)
        return round(distance, 4)

def policz_rouge(text1, text2):
    """
    Measure distance using rouge
    """
    if not text1:
        return None
    if not text2:
        return None
    distance = calculate_rouge(text1, text2)
    return distance

def calculate_rouge_explain(reference, candidate):
    if not reference:
        return None
    if not candidate:
        return None
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
    scores = scorer.score(reference, candidate)
    rouge_scores = calculate_rouge(reference, candidate)
    print(f"ROUGE-1 Score: {rouge_scores['rouge1'].fmeasure:.2f}")
    print(f"ROUGE-L Score: {rouge_scores['rougeL'].fmeasure:.2f}")

def main():
    # Text inputs
    text1 = "Example text one."
    text2 = "Example text two."

if __name__ == "__main__":
    main()

