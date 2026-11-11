"""
=============================================================================
MovieVerse - Recommendation Engine Builder
CSE 426: Data Mining & Warehouse Lab
=============================================================================
This script downloads, cleans, and builds the Vector Similarity model
from the official TMDb 5000 Movies Dataset.
=============================================================================
"""

import os
import ssl
import json
import pickle
import urllib.request
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def build():
    print("=" * 60)
    print("   MovieVerse Recommendation Engine Builder")
    print("=" * 60)

    os.makedirs('data', exist_ok=True)
    csv_path = 'data/movie_dataset.csv'

    if not os.path.exists(csv_path):
        print("\n[Step 1] Downloading TMDb 5000 movie dataset...")
        ctx = ssl._create_unverified_context()
        url = 'https://raw.githubusercontent.com/rashida048/Datasets/master/movie_dataset.csv'
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx) as r, open(csv_path, 'wb') as f:
            f.write(r.read())
        print(f"Downloaded! Saved to: {csv_path}")
    else:
        print(f"\n[Step 1] Found existing dataset: {csv_path}")

    print("\n[Step 2] Cleaning & Preprocessing metadata...")
    df = pd.read_csv(csv_path)
    print(f"Raw titles in catalog: {len(df)}")

    # Prune unrated / noisy records (vote_count >= 20)
    df = df[df['vote_count'] >= 20].copy().reset_index(drop=True)
    print(f"Verified quality titles retained: {len(df)}")

    # Fill missing values
    for col in ['genres', 'keywords', 'cast', 'director', 'overview']:
        df[col] = df[col].fillna('')

    # Clean director string into a single token repeated twice
    df['director_token'] = df['director'].apply(lambda x: (' '.join([''.join(x.split())] * 2)) if x else '')

    # Construct Weighted Feature Soup
    print("\n[Step 3] Constructing Weighted Feature Soup...")
    df['soup'] = (
        (df['genres'] + ' ') * 3 +
        (df['director_token'] + ' ') * 2 +
        (df['keywords'] + ' ') * 2 +
        (df['cast'] + ' ') * 2 +
        df['overview']
    )

    # Vectorization & Cosine Similarity Matrix
    print("\n[Step 4] Vectorizing with CountVectorizer (15,000 dimensions)...")
    cv = CountVectorizer(stop_words='english', max_features=15000)
    count_matrix = cv.fit_transform(df['soup'])

    print("[Step 5] Computing pairwise Cosine Similarity Matrix...")
    sim = cosine_similarity(count_matrix)

    # Precompute Top 15 Matches for instant zero-latency lookup
    print("\n[Step 6] Indexing top matches...")
    recs_dict = {}
    for idx in range(len(df)):
        scores = list(enumerate(sim[idx]))
        top_matches = sorted(scores, key=lambda x: x[1], reverse=True)[1:16]
        recs_dict[idx] = [(m_idx, float(score)) for m_idx, score in top_matches]

    # Save clean tables & cache
    save_cols = ['id', 'title', 'genres', 'director', 'cast', 'overview', 'vote_average', 'vote_count', 'release_date']
    clean_movies = df[save_cols].copy()
    clean_movies.to_csv('data/clean_movies.csv', index=False)

    with open('data/recs_cache.pkl', 'wb') as f:
        pickle.dump(recs_dict, f)

    print("\n" + "=" * 60)
    print("SUCCESS: Recommendation Engine & Clean Data built perfectly!")
    print(f"Total catalog titles: {len(clean_movies)}")
    print("=" * 60)

if __name__ == '__main__':
    build()
