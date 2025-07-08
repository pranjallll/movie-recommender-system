import pickle
import bz2

# Load the original similarity.pkl
with open('similarity.pkl', 'rb') as f_in:
    similarity = pickle.load(f_in)

# Save it as a compressed .bz2 file
with bz2.BZ2File('similarity.pkl.bz2', 'wb') as f_out:
    pickle.dump(similarity, f_out)

print("Compression complete: similarity.pkl.bz2 created.")
