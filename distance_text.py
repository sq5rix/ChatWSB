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
def main():
# Text inputs
    text1 = "Example text one."
    text2 = "Example text two."

# Convert texts to vectors
    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)

# Check if vectors were python -m spacy downloadcreated
    if vector1 is not None and vector2 is not None:
        # Calculate Euclidean distance
        distance = euclidean(vector1, vector2)
        print("Euclidean Distance:", distance)
    else:
        print("One of the texts did not produce a vector. Check the texts for enough content or out-of-vocabulary issues.")

if __name__ == "__main__":
    main()

