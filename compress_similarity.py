import pickle
import gzip

# Load your original similarity.pkl (this is your existing big file)
with open('similarity.pkl', 'rb') as f:
    similarity = pickle.load(f)

# Compress and save as similarity.pkl.gz
with gzip.open('similarity.pkl.gz', 'wb') as f:
    pickle.dump(similarity, f)

print("Compression complete: similarity.pkl.gz created.")
