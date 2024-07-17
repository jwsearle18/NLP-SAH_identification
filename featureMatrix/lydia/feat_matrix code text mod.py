import pandas as pd
import numpy as np
import re
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from tqdm import tqdm
nltk.download('punkt')


# Load the text notes from a DataFrame column
df = pd.read_csv('/Users/lepetersen/info/data_jun03_half.csv')  # Replace with your actual DataFrame file path
text_notes = df['note_txt'].tolist()  # Replace 'note_txt' with the actual column name

# Load the keywords from a text file
with open('/Users/lepetersen/info/KW_feat_matrix_620.txt', 'r') as file:  # Replace with your actual keywords file path
    keywords = file.read().splitlines()

# Initialize stemmer
stemmer = PorterStemmer()

# Stem keywords
stemmed_keywords = [' '.join(stemmer.stem(word) for word in keyword.split()) for keyword in keywords]

# Function to preprocess and stem text
def preprocess_text(text):
    text = text.lower()
    tokens = word_tokenize(text)
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return ' '.join(stemmed_tokens)

# Preprocess all text notes
stemmed_text_notes = [preprocess_text(note) for note in tqdm(text_notes, desc="Preprocessing Text Notes")]

# Create keyword features (including multi-word terms)
keyword_vectorizer = CountVectorizer(vocabulary=stemmed_keywords, binary=False, ngram_range=(1, 6))
keyword_features = keyword_vectorizer.transform(stemmed_text_notes).toarray()

# Function to create contextual features and count occurrences
def count_context_features(text, target_words, context_words, window_size=15):
    tokens = text.split()
    near_count = 0
    far_count = 0
    for i, token in enumerate(tokens):
        if token in target_words:
            left_context = tokens[max(0, i - window_size):i]
            right_context = tokens[i + 1:i + 1 + window_size]
            context = left_context + right_context
            if any(context_word in context for context_word in context_words):
                near_count += 1
            else:
                far_count += 1
    return near_count, far_count

# Define target words and their corresponding context words
target_context_pairs = {
    'meningioma_anti': {###REVIEW###
        'target': 'meningioma',
        'contexts': ['no evidence'] #,'no','not','family','brother','sister','mother','father']
    },
#    'meningioma_pro': {
#        'target': 'meningioma',
#        'contexts': []
#    },
    'adenoma_pro': {
        'target': 'adenoma',
        'contexts': ['pituitary']
    },
#    'adenoma_anti': {
#        'target': 'adenoma',
#        'contexts': []
#    },
    'neoplasm_anti': {
        'target': 'neoplasm',
        'contexts': ['no evidence', 'no','r/o','spine','gastric','carcinoid','rectal','parotid','spouse','sister','mother',
                     'father','brother','family history','breast','bladder','eye','buttock','wilms','not','thigh','lung',
                     'renal','shoulder','liver','biliary','skin','prostate','salivary','bladder','testis','tongue','colon',
                     'parotid','papillary','oropharyngeal','breast','neck']
    },
 #   'neoplasm_pro': {
 #       'target': 'neoplasm',
 #       'contexts': []
 #   },
    'tumor_anti': {
        'target': 'tumor',
        'contexts': ['no evidence', 'no','r/o','spine','gastric','carcinoid','rectal','parotid','spouse','sister','mother',
                     'father','brother','family history','breast','bladder','eye','buttock','wilms','not','thigh','lung',
                     'renal','shoulder','liver','biliary','skin','prostate','salivary','bladder','testis','tongue','colon',
                     'parotid','papillary','oropharyngeal','breast','neck']
    },
#    'tumor_pro': {
#        'target': 'tumor',
#        'contexts': []
#    },
    # Add more target words and context words as needed
}

# Create contextual features
contextual_features = []
contextual_feature_names = []
for context_id, context_data in target_context_pairs.items():
    target_word = context_data['target']
    context_words = context_data['contexts']
    near_context_feature = []
    far_context_feature = []
    for text in tqdm(stemmed_text_notes, desc=f"Creating Contextual Features for {context_id}"):
        near_count, far_count = count_context_features(text, [stemmer.stem(word) for word in target_word.split()], [stemmer.stem(word) for word in context_words])
        near_context_feature.append(near_count)
        far_context_feature.append(far_count)
    near_context_feature = np.array(near_context_feature).reshape(-1, 1)
    far_context_feature = np.array(far_context_feature).reshape(-1, 1)
    contextual_features.append(near_context_feature)
    contextual_features.append(far_context_feature)
    contextual_feature_names.append(f'contextual_{context_id}_near')
    contextual_feature_names.append(f'contextual_{context_id}_abs')

# Combine all contextual features into a single array
contextual_features = np.hstack(contextual_features)

# Combine all features into a feature matrix
feature_matrix = np.hstack((keyword_features, contextual_features))

# Convert to DataFrame for better readability
feature_names = keyword_vectorizer.get_feature_names_out().tolist() + contextual_feature_names
feature_df = pd.DataFrame(feature_matrix, columns=feature_names)

# Display the feature matrix
print(feature_df.head())


x=1
feature_df.to_csv('/Users/lepetersen/model/half data/feat_mat.csv')

x=1














































##  CREATE A BINARY MATRIX (ONLY 1'S AND 0'S)   ##

# # Load the text notes from a DataFrame column
# df = pd.read_csv('/Users/lepetersen/info/data_jun03.csv')  # Replace with your actual DataFrame file path
# text_notes = df['note_txt'].tolist()  # Replace 'text_notes' with the actual column name

# # Load the keywords from a text file
# with open('/Users/lepetersen/info/KW_bt_updated620.txt', 'r') as file:  # Replace with your actual keywords file path
#     keywords = file.read().splitlines()

# # Initialize stemmer
# stemmer = PorterStemmer()

# # Stem keywords
# stemmed_keywords = [' '.join(stemmer.stem(word) for word in keyword.split()) for keyword in keywords]

# # Function to preprocess and stem text
# def preprocess_text(text):
#     text = text.lower()
#     tokens = word_tokenize(text)
#     stemmed_tokens = [stemmer.stem(token) for token in tokens]
#     return ' '.join(stemmed_tokens)

# # Preprocess all text notes
# stemmed_text_notes = [preprocess_text(note) for note in tqdm(text_notes, desc="Preprocessing Text Notes")]

# # Create keyword features (including multi-word terms)
# keyword_vectorizer = CountVectorizer(vocabulary=stemmed_keywords, binary=True, ngram_range=(1, 6))
# keyword_features = keyword_vectorizer.transform(stemmed_text_notes).toarray()


# # Function to create contextual features
# def find_context_features(text, target_words, context_words, window_size=5):
#     tokens = text.split()
#     feature = 0
#     for i, token in enumerate(tokens):
#         if token in target_words:
#             left_context = tokens[max(0, i - window_size):i]
#             right_context = tokens[i + 1:i + 1 + window_size]
#             context = left_context + right_context
#             if any(context_word in context for context_word in context_words):
#                 feature = 1
#                 break
#     return feature

# # Define target words and their corresponding context words
# target_context_pairs = {
#     'meningioma': ['suspect', 'likely', 'could, favored'],
#     'family': ['brain', 'tumor'],
#     # Add more target words and context words as needed
# }

# # Create contextual features
# contextual_features = []
# for target_word, context_words in target_context_pairs.items():
#     context_feature = np.array([
#         find_context_features(text, [stemmer.stem(target_word) for word in target_word.split()], [stemmer.stem(word) for word in context_words]) 
#         for text in tqdm(stemmed_text_notes, desc=f"Creating Contextual Features for {target_word}")
#     ]).reshape(-1, 1)
#     contextual_features.append(context_feature)

# # Combine all contextual features into a single array
# contextual_features = np.hstack(contextual_features)

# # Combine all features into a feature matrix
# feature_matrix = np.hstack((keyword_features, contextual_features))

# # Convert to DataFrame for better readability
# feature_names = keyword_vectorizer.get_feature_names_out().tolist()
# for target_word in target_context_pairs.keys():
#     feature_names.append(f'contextual_{target_word}')
# feature_df = pd.DataFrame(feature_matrix, columns=feature_names)

# # Display the feature matrix
# print(feature_df.head())

# x=1