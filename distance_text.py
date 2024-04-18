import spacy
from scipy.spatial.distance import euclidean

# Load the medium English model
nlp = spacy.load('en_core_web_md')

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

# Text inputs
text1 = "Example text one."
text2 = "Example text two."

# Convert texts to vectors
vector1 = text_to_vector(text1)
vector2 = text_to_vector(text2)

# Check if vectors were created
if vector1 is not None and vector2 is not None:
    # Calculate Euclidean distance
    distance = euclidean(vector1, vector2)
    print("Euclidean Distance:", distance)
else:
    print("One of the texts did not produce a vector. Check the texts for enough content or out-of-vocabulary issues.")
