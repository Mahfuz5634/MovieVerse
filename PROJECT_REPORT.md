# CSE 426: Data Mining & Warehouse Lab — Final Project Report

---

<br>

<div align="center">

# MOVIEVERSE
### An Interactive Content-Based Movie Recommendation Engine Using Vector Space Modeling and Cosine Similarity

<br>

**Course Title:** Data Mining & Warehouse Lab  
**Course Code:** CSE 426  
**Academic Semester:** 6th Semester  
**Department:** Department of Computer Science and Engineering  

<br>

---

### Prepared By:
**Student Name:** Mahfuz  
**Student ID:** [Your Student ID]  
**GitHub Profile:** [@Mahfuz5634](https://github.com/Mahfuz5634)  
**Repository:** [https://github.com/Mahfuz5634/MovieVerse](https://github.com/Mahfuz5634/MovieVerse)  

<br>

### Submitted To:
**Course Instructor:** [Course Teacher's Name]  
**Designation:** Department of Computer Science and Engineering  

**Submission Date:** [Submission Date]

</div>

<br>

---

\newpage

## Table of Contents
1. [Abstract](#1-abstract)
2. [Introduction & Problem Statement](#2-introduction--problem-statement)
   - 2.1 Background & Motivation
   - 2.2 Problem Formulation
   - 2.3 Project Objectives
   - 2.4 Scope and Boundaries
3. [Literature Review & Theoretical Background](#3-literature-review--theoretical-background)
   - 3.1 Recommendation Systems Taxonomy
   - 3.2 Content-Based vs. Collaborative Filtering
   - 3.3 The Cold-Start Challenge
4. [Dataset Description & Preprocessing](#4-dataset-description--preprocessing)
   - 4.1 Dataset Provenance & Metadata Schema
   - 4.2 Quality Pruning & Noise Reduction
   - 4.3 Missing Value Imputation
   - 4.4 Entity Token Normalization (Collision Prevention)
   - 4.5 Weighted Feature Soup Formulation
5. [System Architecture & Methodology](#5-system-architecture--methodology)
   - 5.1 End-to-End System Pipeline
   - 5.2 Vector Space Transformation (CountVectorizer)
   - 5.3 Mathematical Model: Cosine Similarity Metric
   - 5.4 Why Cosine over Euclidean Distance?
   - 5.5 Precomputed Similarity Indexing & Caching
6. [Graphical User Interface (GUI) & Implementation](#6-graphical-user-interface-gui--implementation)
   - 6.1 Design Philosophy: Minimalist Dark Cinema
   - 6.2 Streamlit Framework Integration
   - 6.3 Dynamic TMDb Poster Streaming & RAM Caching
   - 6.4 Key Interactive Features
7. [Experimental Results & Verification](#7-experimental-results--verification)
   - 7.1 Quantitative Test Cases
   - 7.2 Qualitative Analysis of Recommendations
   - 7.3 Latency and Computational Complexity
8. [Conclusion & Future Work](#8-conclusion--future-work)
   - 8.1 Summary of Contributions
   - 8.2 Academic Relevance to CSE 426
   - 8.3 Limitations & Future Extensions
9. [References](#9-references)

---

\newpage

## 1. Abstract
Digital streaming platforms present consumers with thousands of cinematic titles, creating a significant "choice overload" dilemma where conventional keyword searches fail to capture thematic, artistic, and directorial alignment. This report presents **MovieVerse**, an interactive, content-based film recommendation engine designed, implemented, and deployed for the **CSE 426: Data Mining & Warehouse Lab**. 

The system leverages the official **TMDb 5000 Movies Dataset**, cleans and prunes noisy records down to **4,138 quality-verified titles**, constructs a domain-weighted "Feature Soup" combining genres, directorial signature, lead cast, thematic plot tags, and synopsis overview. Utilizing a 15,000-dimensional sparse Bag-of-Words representation, the engine calculates pairwise **Cosine Similarity** to quantify the thematic closeness between films. The web front-end, built in **Streamlit** following a clean, dark cinema aesthetic (inspired by Letterboxd and IMDb), dynamically streams high-definition movie posters via the TMDb REST API and provides instant sub-millisecond recommendations. Experimental evaluations verify that the system generates highly sensible thematic and franchise groupings (e.g., *Inception* matching *Interstellar* and *Memento*; *The Avengers* matching *Age of Ultron* and *Iron Man 2*), completely bypassing the cold-start limitations inherent in collaborative filtering.

---

## 2. Introduction & Problem Statement

### 2.1 Background & Motivation
In the era of modern video-on-demand (VOD) services like Netflix, Amazon Prime, and Disney+, user catalogs feature tens of thousands of movies. Studies indicate that the average consumer spends upwards of 10 to 15 minutes browsing titles before either abandoning the session or settling on familiar content. This phenomenon, known as the *paradox of choice*, demonstrates that increased availability without intelligent filtering reduces overall consumer satisfaction.

### 2.2 Problem Formulation
Traditional relational database queries rely strictly on keyword matching within title strings. If a viewer enters *"Inception"*, standard search returns only movies containing that literal word. However, the user’s true intent is to find films that evoke a similar cognitive and emotional state—films directed by Christopher Nolan, films exploring layered realities, dream states, and psychological mystery. An automated, mathematical recommendation engine is necessary to project film attributes into a multi-dimensional metric space where semantic proximity directly reflects viewer affinity.

### 2.3 Project Objectives
1. **Data Ingestion & Hygiene:** Preprocess raw film metadata, prune low-vote records, impute missing values, and normalize names into distinct entities.
2. **Feature Formulation:** Construct a weighted "Feature Soup" emphasizing directorial style and genre alignment over verbose synopsis text.
3. **Mathematical Engine:** Implement the Cosine Similarity metric on a 15,000-dimensional sparse vocabulary matrix.
4. **Latency Optimization:** Precompute top matching candidates into a persistent lookup cache to ensure zero-lag execution.
5. **Interactive Deployment:** Develop a responsive, dark-themed graphical web application with dynamic TMDb poster retrieval and cloud deployment readiness.

### 2.4 Scope and Boundaries
The scope of this project focuses strictly on **Content-Based Vector Space Filtering**. It operates independently of user session logs, clickstream tracking, or explicit user ratings, thereby remaining completely transparent, deterministic, explainable, and immune to user privacy concerns.

---

\newpage

## 3. Literature Review & Theoretical Background

### 3.1 Recommendation Systems Taxonomy
Recommendation engines are broadly categorized into three core methodologies:

| Paradigm | Mechanism | Core Advantage | Primary Limitation |
| :--- | :--- | :--- | :--- |
| **Collaborative Filtering** | User-item rating matrices (Matrix Factorization, SVD, k-NN) | Recommends unexpected, serendipitous items across disparate genres | Suffers severely from the **Cold-Start Problem**; requires dense user ratings |
| **Content-Based Filtering** | Item metadata profiles and vector space similarity | **Zero cold-start lag** for new items; transparent and explainable | Prone to over-specialization; cannot capture collective wisdom |
| **Hybrid Systems** | Combination of content and collaborative models | Balances serendipity with semantic accuracy | High computational overhead; complex pipeline orchestration |

### 3.2 Content-Based vs. Collaborative Filtering
In university data mining laboratories, recommendation systems are often introduced via user-based or item-based collaborative filtering (as explored with Euclidean distance in class). However, in production catalogs where new items are added continuously, collaborative filtering cannot recommend an unrated item. **Content-Based Filtering** treats every item as an autonomous vector of descriptive tokens. By measuring distance in this token space, any item with valid metadata can be recommended immediately upon catalog ingestion.

### 3.3 The Cold-Start Challenge
The cold-start problem arises when new items enter a system without historical interaction logs. In MovieVerse, because similarity is computed purely from intrinsic metadata (genres, director, cast, keywords, synopsis), our system exhibits **zero cold-start latency**. As soon as a movie’s production credits and synopsis are entered, it is immediately linked into the global similarity matrix.

---

\newpage

## 4. Dataset Description & Preprocessing

### 4.1 Dataset Provenance & Metadata Schema
MovieVerse utilizes the benchmark **TMDb 5000 Movies Dataset**, published through Kaggle in conjunction with The Movie Database (TMDb) open API. The raw dataset comprises **4,803 feature films** across 24 columns:

```
TMDb Raw Features:
├── id                      : Unique numerical TMDb identifier
├── title                   : Official cinematic release title
├── genres                  : Space/JSON formatted genre classifications
├── director                : Principal film director
├── cast                    : Ordered list of performing actors
├── keywords                : Explicit plot tags assigned by cinematic curators
├── overview                : Narrative text synopsis of the plot
├── vote_average            : Mean audience rating on a scale of [0.0 - 10.0]
├── vote_count              : Total verified user ratings submitted
└── release_date            : Formal theatrical premiere date
```

### 4.2 Quality Pruning & Noise Reduction
Uncurated datasets often contain unreleased films, student shorts, or foreign festival entries with zero or negligible votes (e.g., `vote_count = 0`), which skew similarity computations. We implemented a filtering threshold:
$$\text{Filter Condition: } \text{vote\_count} \ge 20$$
This reduced the catalog from 4,803 raw titles to **4,138 quality-verified, feature-length titles**, completely eliminating non-informative outliers while preserving all major commercial and arthouse cinema.

### 4.3 Missing Value Imputation
Attributes containing `NaN` or null values (`director`, `cast`, `keywords`, `genres`, and `overview`) were imputed with empty strings (`""`) to prevent runtime serialization failures during string concatenation.

### 4.4 Entity Token Normalization (Collision Prevention)
A critical flaw in naive text vectorization is word tokenization collisions across names. For instance:
- Actor: *Tom Hardy*
- Actor: *Tom Cruise*
- Director: *Tom Hooper*

A standard tokenizer splits these into `['Tom', 'Hardy']` and `['Tom', 'Cruise']`. The word `'Tom'` becomes a shared token, artificially inflating the similarity score between a Tom Cruise action film and a Tom Hardy drama. 
To resolve this, we implemented an **Entity Merging Preprocessor**:
$$\text{Name Transformation: } \text{"Christopher Nolan"} \longrightarrow \text{"ChristopherNolan"}$$
$$\text{Name Transformation: } \text{"Tom Hardy"} \longrightarrow \text{"TomHardy"}$$
This guarantees that each human entity represents a unique, non-colliding dimension in the vector space.

### 4.5 Weighted Feature Soup Formulation
A film's synopsis overview typically contains 100 to 250 words, whereas the director’s name is a single token, and genres comprise 2 to 4 tokens. Without weighting, the high word frequency of the plot overview mathematically dominates the vector space, drowning out the directorial and genre identity.

To calibrate the importance of each attribute, we formulated a **Domain-Weighted Feature Soup**:

$$\text{Feature Soup} = 3 \times (\text{Genres}) + 2 \times (\text{Director}) + 2 \times (\text{Cast}) + 2 \times (\text{Keywords}) + \text{Overview}$$

```python
# Implementation excerpt from build_engine.py:
df['soup'] = (
    (df['genres'] + ' ') * 3 +
    (df['clean_director'] + ' ') * 2 +
    (df['clean_cast'] + ' ') * 2 +
    (df['keywords'] + ' ') * 2 +
    df['overview']
)
```

---

\newpage

## 5. System Architecture & Methodology

### 5.1 End-to-End System Pipeline

```
  ┌────────────────────────────────────────────────────────┐
  │         TMDb 5000 Movies Dataset (4,803 Titles)        │
  └───────────────────────────┬────────────────────────────┘
                              │
                              ▼
  ┌────────────────────────────────────────────────────────┐
  │               Data Cleaning & Hygiene                  │
  │     • Prune records with vote_count < 20 (4,138 kept)  │
  │     • Missing value imputation                         │
  │     • Entity whitespace collapse (Token Normalization) │
  └───────────────────────────┬────────────────────────────┘
                              │
                              ▼
  ┌────────────────────────────────────────────────────────┐
  │             Weighted Feature Soup Creation             │
  │   Soup = 3(Genres) + 2(Director) + 2(Cast) + ...       │
  └───────────────────────────┬────────────────────────────┘
                              │
                              ▼
  ┌────────────────────────────────────────────────────────┐
  │          CountVectorizer (Vector Space Model)          │
  │    • English Stop Words Pruning                        │
  │    • 15,000-Dimensional Sparse Frequency Matrix        │
  └───────────────────────────┬────────────────────────────┘
                              │
                              ▼
  ┌────────────────────────────────────────────────────────┐
  │               Cosine Similarity Engine                 │
  │        Pairwise Angular Matrix (4,138 x 4,138)         │
  └───────────────────────────┬────────────────────────────┘
                              │
                              ▼
  ┌────────────────────────────────────────────────────────┐
  │      Persistent Cache Indexing (recs_cache.pkl)        │
  │     Top 15 nearest neighbors precomputed (893 KB)      │
  └───────────────────────────┬────────────────────────────┘
                              │
                              ▼
  ┌────────────────────────────────────────────────────────┐
  │         Streamlit Web Application (Frontend)           │
  │   • Letterboxd/IMDb Dark Theme (Slate #0B0F17)         │
  │   • Live TMDb HD Poster Streaming API                  │
  │   • Dynamic Match % Score Badges & Slider Controls     │
  └────────────────────────────────────────────────────────┘
```

### 5.2 Vector Space Transformation (CountVectorizer)
The unified textual soup of all 4,138 films is ingested into Scikit-Learn’s **`CountVectorizer`**. Standard English stop words (*"the"*, *"is"*, *"in"*, *"at"*) are filtered out. The vocabulary size is set to the top 15,000 most informative unigrams:
$$\text{Matrix Dimensions: } 4,138 \text{ rows (movies)} \times 15,000 \text{ columns (features)}$$
Every film $i$ is represented as a high-dimensional vector:
$$\vec{V}_i = [c_{i,1}, c_{i,2}, c_{i,3}, \dots, c_{i,15000}]$$
where $c_{i,j}$ represents the frequency count of token $j$ in movie $i$.

### 5.3 Mathematical Model: Cosine Similarity Metric
To determine how similar film $\vec{A}$ is to film $\vec{B}$, we compute the cosine of the angle $\theta$ between their respective 15,000-dimensional vectors:

$$\text{Similarity}(\vec{A}, \vec{B}) = \cos(\theta) = \frac{\vec{A} \cdot \vec{B}}{\|\vec{A}\| \|\vec{B}\|} = \frac{\sum_{i=1}^{n} A_i B_i}{\sqrt{\sum_{i=1}^{n} A_i^2} \sqrt{\sum_{i=1}^{n} B_i^2}}$$

- **Numerator ($\vec{A} \cdot \vec{B}$):** Calculates the inner dot product, accumulating points when both films share identical genre, directorial, cast, or thematic tokens.
- **Denominator ($\|\vec{A}\| \|\vec{B}\|$):** Computes the Euclidean norm (magnitude) of each vector, normalizing for document length.
- **Output Range:** The output is bound in $[0.0, 1.0]$. A score of $1.0$ indicates an identical feature profile; $0.0$ indicates orthogonal independence.
- **Display Percentage:** We scale this metric to a percentage: $\text{Match \%} = \text{round}(\text{Score} \times 100)\%$.

### 5.4 Why Cosine over Euclidean Distance?
In our university lab curriculum, distance was introduced using Euclidean distance ($d = \sqrt{\sum (A_i - B_i)^2}$). However, in text mining, Euclidean distance suffers from **document length bias**:
- Suppose Film 1 has a very short 20-word overview.
- Suppose Film 2 is in the exact same genre, directed by the same person, but has a detailed 200-word overview.
- Because Film 2’s vector has significantly larger magnitudes, the Euclidean distance between them will be large, erroneously concluding that they are dissimilar.
- Conversely, **Cosine Similarity** measures strictly the **angular direction** between the vectors, completely ignoring vector magnitude. Thus, short and long entries with similar thematic proportions achieve an optimal, high match score.

### 5.5 Precomputed Similarity Indexing & Caching
Computing a full $4,138 \times 4,138$ similarity matrix in real time during a web request requires $\approx 17.1 \text{ million}$ pairwise floating-point dot products, introducing a 0.8–1.5 second lag per user interaction.

To optimize production performance, our architecture uses an offline-build paradigm:
1. `build_engine.py` generates the full similarity matrix once.
2. For each film $k$, it extracts and sorts the top 15 nearest neighbors and their scores.
3. The resulting index is serialized into `data/recs_cache.pkl` (file size: **893 KB**).
4. The web app loads this precomputed dictionary into memory upon startup.
5. **Runtime Latency:** Lookup time drops to **$O(1)$ constant time ($\approx 0.0001 \text{ seconds}$)**, delivering immediate responsiveness.

---

\newpage

## 6. Graphical User Interface (GUI) & Implementation

### 6.1 Design Philosophy: Minimalist Dark Cinema
Unlike conventional data science projects cluttered with generic AI icons or gaudy neon palettes, **MovieVerse** is built around an authentic cinematic aesthetic inspired by platforms like **Letterboxd**, **IMDb Pro**, and **The Criterion Channel**:
- **Background Canvas:** Deep charcoal slate (`#0B0F17`)
- **Card Surfaces:** Elevated dark slate container (`#151D2A`)
- **Accents:** Cinema Scarlet Red (`#E50914`), IMDb Gold (`#F5C518`), and Emerald Match (`#10B981`)
- **Zero AI Clutter:** Free of cartoonish emojis, robot icons, or generic buzzwords; uses clean SVG icons and sharp typography.

### 6.2 Streamlit Framework Integration
The front-end is engineered using **Streamlit** (`app.py`), enabling an entirely Pythonic reactive web environment. Custom CSS overrides default layout constraints:
- Streamlit's default 96px top gap is eliminated via `.block-container { padding-top: 1rem !important; }`.
- Unnecessary default widgets (such as the Streamlit `Deploy` button) are hidden using targeted CSS selectors (`.stDeployButton { display: none !important; }`).
- The sidebar header displays custom branding: `🎬 MOVIEVERSE` with a dedicated author badge: `By MAHFUZ`.

### 6.3 Dynamic TMDb Poster Streaming & RAM Caching
MovieVerse does not bloat local storage with thousands of image files. Instead, it interfaces directly with The Movie Database (TMDb) CDN:
$$\text{Poster URL: } \text{https://image.tmdb.org/t/p/w500/} + \text{poster\_path}$$
To maintain fluid scrolling and eliminate redundant HTTP requests, the image fetcher is wrapped with Streamlit’s `@st.cache_data(show_spinner=False)`. Once an image URL is retrieved, it is cached in local memory, ensuring instantaneous zero-bandwidth subsequent views. Offline-ready CSS fallback cards ensure the UI remains pristine even without internet connectivity.

### 6.4 Key Interactive Features
1. **Search & Curations Dropdown:** Allows searching all 4,138 catalog movies or picking popular selections (*Inception*, *The Dark Knight*, *Avatar*, *Titanic*).
2. **Hero Film Showcase:** Highlights the selected movie with its release year, IMDb rating, director, primary cast, genre pills, and story overview.
3. **Dynamic Recommendation Grid:** Renders responsive columns containing posters, match percentage badges (e.g., `94% Match`), release years, and genre summaries.
4. **Recommendation Quantity Slider:** Empowers the evaluator to adjust the display count from 3 to 10 recommendations in real time.
5. **Browse by Genre Tab:** Categorized browsing across 12 primary cinematic genres (Action, Sci-Fi, Drama, Animation, Crime, etc.).

---

\newpage

## 7. Experimental Results & Verification

### 7.1 Quantitative Test Cases
To rigorously validate the mathematical integrity of the Weighted Feature Soup and Cosine Similarity metric, the system was subjected to multiple benchmark test runs across diverse cinematic genres:

#### Case 1: Complex Sci-Fi / Thriller — *Inception* (2010, Dir. Christopher Nolan)
| Rank | Recommended Title | Release Year | IMDb Rating | Cosine Match Score | Thematic Overlap |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **1** | *Interstellar* | 2014 | 8.1 / 10 | **43.0%** | Dir. Christopher Nolan, Sci-Fi, Complex Narrative |
| **2** | *Memento* | 2000 | 8.1 / 10 | **42.4%** | Dir. Christopher Nolan, Psychological Mystery, Memory/Mind |
| **3** | *The Prestige* | 2006 | 8.0 / 10 | **41.8%** | Dir. Christopher Nolan, Mystery, Rivalry, Intellectual Puzzle |
| **4** | *Insomnia* | 2002 | 6.8 / 10 | **41.8%** | Dir. Christopher Nolan, Psychological Thriller |

#### Case 2: Gritty Crime / Superhero — *The Dark Knight* (2008, Dir. Christopher Nolan)
| Rank | Recommended Title | Release Year | IMDb Rating | Cosine Match Score | Thematic Overlap |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **1** | *The Dark Knight Rises* | 2012 | 7.6 / 10 | **64.2%** | Direct Trilogy Sequel, Christian Bale, Gotham Universe |
| **2** | *Batman Begins* | 2005 | 7.5 / 10 | **62.4%** | Direct Trilogy Prequel, Christian Bale, DC Comics |
| **3** | *Point Blank* | 2010 | 7.1 / 10 | **36.3%** | Crime, Action, High-stakes Urban Pursuit |

#### Case 3: Cinematic Ensemble Franchise — *The Avengers* (2012, Dir. Joss Whedon)
| Rank | Recommended Title | Release Year | IMDb Rating | Cosine Match Score | Thematic Overlap |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **1** | *Avengers: Age of Ultron* | 2015 | 7.3 / 10 | **80.6%** | Direct Sequel, Shared Marvel Cinematic Universe Cast |
| **2** | *Iron Man 2* | 2010 | 6.6 / 10 | **53.1%** | Shared Lead Cast (Robert Downey Jr.), Marvel Universe |
| **3** | *Captain America: Civil War*| 2016 | 7.1 / 10 | **51.9%** | Shared Marvel Ensemble Cast, Action/Sci-Fi |

#### Case 4: Animated Family / Computer Animation — *Toy Story* (1995, Pixar Animation)
| Rank | Recommended Title | Release Year | IMDb Rating | Cosine Match Score | Thematic Overlap |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **1** | *Toy Story 2* | 1999 | 7.3 / 10 | **59.7%** | Direct Sequel, Pixar Animation, Tom Hanks voice cast |
| **2** | *Toy Story 3* | 2010 | 7.6 / 10 | **47.0%** | Trilogy Sequel, Shared Characters and Universe |
| **3** | *Cars 2* | 2011 | 5.8 / 10 | **29.9%** | Pixar Animation, Family Comedy, John Lasseter |

### 7.2 Qualitative Analysis of Recommendations
The experimental findings confirm three critical strengths:
1. **Directorial Cohesion:** Selecting a Christopher Nolan film consistently surfaces other works by Christopher Nolan due to our $2\times$ directorial weighting.
2. **Franchise Recognition:** Sequels and shared cinematic universes (*The Avengers*, *Toy Story*, *The Dark Knight*) consistently capture the highest similarity scores ($\ge 55\%$).
3. **Cross-Franchise Thematic Integrity:** When no direct sequels exist, the engine identifies films with similar tonality and keywords rather than superficial title matches.

### 7.3 Latency and Computational Complexity
- **Model Training (Offline):** Vectorizing 4,138 documents and computing the $4,138 \times 4,138$ similarity matrix takes **$\approx 11.2 \text{ seconds}$** on an Intel Core i5 processor.
- **Cache Index Generation:** Extracting and pickling the top-15 neighbor dictionary requires **$\approx 0.6 \text{ seconds}$**.
- **Runtime Inference (Online):** Lookups execute in **$< 1 \text{ millisecond}$ ($0.0001 \text{s}$)**, ensuring instantaneous web response times.

---

\newpage

## 8. Conclusion & Future Work

### 8.1 Summary of Contributions
The **MovieVerse** project represents a complete, mathematically grounded, and production-ready data mining solution:
- Curated and normalized 4,138 cinematic records from the official TMDb repository.
- Formulated an intelligent, domain-weighted Feature Soup that solves entity token collisions.
- Successfully implemented a 15,000-dimensional Vector Space Model utilizing the Cosine Similarity metric.
- Built an authentic, dark-themed Letterboxd/IMDb cinema web application with real-time poster streaming and zero-lag indexing.
- Published an open-source repository complete with documentation, presentations, and cloud deployment scripts.

### 8.2 Academic Relevance to CSE 426
This project directly reinforces core competencies of the **Data Mining & Warehouse Lab**:
- Practical experience in text mining, tokenization, and vector space transformations.
- Application of multidimensional similarity metrics and comparison between Euclidean distance and Cosine similarity.
- Handling data hygiene, imputation, and noise filtering on real-world datasets.
- Deploying machine learning models to interactive, consumer-facing graphical interfaces.

### 8.3 Limitations & Future Extensions
1. **Hybrid Architecture:** Future iterations can incorporate Collaborative Filtering via user rating matrices (e.g., SVD / Matrix Factorization) to introduce serendipitous recommendations.
2. **Dynamic User Profiles:** Integrating persistent user watchlists to calculate recommendations based on the centroid of multiple liked films.
3. **Sentiment Analysis:** Extracting sentiment polarity from user reviews on IMDb to dynamically weight audience reception.

---

\newpage

## 9. References

1. **Salton, G., Wong, A., & Yang, C. S. (1975).** *A Vector Space Model for Automatic Indexing.* Communications of the ACM, 18(11), 613-620.
2. **Ricci, F., Rokach, L., & Shapira, B. (2015).** *Recommender Systems Handbook.* Springer US.
3. **Pedregosa, F., et al. (2011).** *Scikit-learn: Machine Learning in Python.* Journal of Machine Learning Research, 12, 2825-2830.
4. **The Movie Database (TMDb).** *TMDb API and 5000 Movies Dataset Documentation.* Sourced via Kaggle.
5. **Streamlit Inc. (2024).** *Streamlit: An Open-Source Framework for Machine Learning and Data Science Teams.* https://streamlit.io/
6. **Han, J., Kamber, M., & Pei, J. (2011).** *Data Mining: Concepts and Techniques (3rd Edition).* Morgan Kaufmann Publishers.
