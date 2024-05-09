import spacy
from scipy.spatial.distance import euclidean

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


def policz_odleglosc(text1, text2):
# Convert texts to vectors
    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)

    if vector1 is not None and vector2 is not None:
        # Calculate Euclidean distance
        distance = euclidean(vector1, vector2)
        return distance


def main():
    # Text inputs
    text1 = "Example text one."
    text2 = "Example text two."
    dist = policz_odleglosc(text1, text2)
    print('dist : ', dist )

if __name__ == "__main__":
    main()

