import pickle
import pandas as pd

# Load the existing large files
with open('movies_dict.pkl', 'rb') as f:
    movies_dict = pickle.load(f)
movies = pd.DataFrame(movies_dict)

with open('similarity.pkl', 'rb') as f:
    similarity = pickle.load(f)

# Step 1: Limit to top 3500 movies
num_movies = 1800
movies_small = movies.iloc[:num_movies].reset_index(drop=True)
similarity_small = similarity[:num_movies, :num_movies]

# Step 2: Save the smaller versions
with open('movies_dict_small2.pkl', 'wb') as f:
    pickle.dump(movies_small.to_dict(), f)

with open('similarity_small.pkl', 'wb') as f:
    pickle.dump(similarity_small, f)

print("✅ Successfully reduced to 2500 movies!")
