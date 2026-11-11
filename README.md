# 🎬 MOVIEVERSE — Content-Based Movie Recommendation Engine

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![TMDb](https://img.shields.io/badge/TMDb-5000_Dataset-01B4E4?style=for-the-badge&logo=the-movie-database&logoColor=white)](https://www.themoviedb.org/)

> **MovieVerse** is an interactive, web-based film recommendation and discovery platform built with **Python**, **Scikit-Learn**, and **Streamlit**. Utilizing **Content-Based Vector Space Modeling** and **Cosine Similarity**, it analyzes over 4,100+ verified movies to deliver mathematically aligned recommendations with live match percentages and official HD movie posters.

---

## 📌 Project Overview

In modern digital streaming services, viewers often struggle with choice overload across catalogs containing thousands of titles. Traditional keyword searches only match exact names without capturing a film's artistic tone, directorial style, or thematic essence.

**MovieVerse** solves this by constructing a multi-dimensional vector space that quantifies the thematic and stylistic closeness between films.

### 🌟 Key Highlights
- **Curated Catalog:** 4,138 quality-verified titles filtered from the official **TMDb 5000 Movies Dataset** (pruned for low-vote noise).
- **Domain-Weighted Feature Soup:** Combines film genres, director, lead cast, thematic keywords, and plot synopsis with domain-informed importance weighting.
- **Vector Space Matching:** Computes pairwise **Cosine Similarity** across a 15,000-dimensional sparse vocabulary matrix.
- **Letterboxd / IMDb Dark Cinema Interface:** Minimalist dark aesthetic (deep slate, cinema gold, and Netflix scarlet accents) designed to feel like an authentic curation app rather than generic AI slop.
- **Dynamic Asset Streaming:** Directly streams high-resolution official movie posters via TMDb API with offline-resilient fallback cards.
- **Zero Cold-Start Lag:** Pre-indexed similarity cache delivers instant sub-millisecond recommendations.

---

## 📐 Mathematical Model & Architecture

### 1. Weighted Feature Soup Formulation
Director and genre alignment provide the strongest signals of viewer taste. To prevent lengthier plot synopses from overwhelming these critical attributes, attributes are weighted systematically:

$$\text{Feature Profile} = 3 \times (\text{Genres}) + 2 \times (\text{Director}) + 2 \times (\text{Keywords}) + 2 \times (\text{Cast}) + \text{Overview}$$

### 2. Entity Token Normalization
Director and performer names are normalized (e.g., `Christopher Nolan` $\rightarrow$ `ChristopherNolan`) so that actors sharing individual names (such as *Tom Hardy* vs. *Tom Cruise*) are never conflated as overlapping tokens.

### 3. Cosine Similarity Metric
Vector similarity is calculated using the cosine of the angle between two multi-dimensional feature vectors:

$$\text{Similarity}(\vec{A}, \vec{B}) = \cos(\theta) = \frac{\vec{A} \cdot \vec{B}}{\|\vec{A}\| \|\vec{B}\|} = \frac{\sum_{i=1}^{n} A_i B_i}{\sqrt{\sum_{i=1}^{n} A_i^2} \sqrt{\sum_{i=1}^{n} B_i^2}}$$

* **Why Cosine over Euclidean Distance?**  
  Cosine similarity evaluates angular orientation rather than vector magnitude, ensuring films with shorter plot summaries are not penalized when compared to verbose entries.

---

## 🧪 Verified Test Cases

| Input Movie | Top Recommendations | Match Score |
| :--- | :--- | :---: |
| **Inception** | *Interstellar*, *Memento*, *The Prestige*, *Paycheck* | **43.0% – 34.2%** |
| **The Dark Knight** | *The Dark Knight Rises*, *Batman Begins*, *Point Blank* | **64.2% – 36.3%** |
| **The Avengers** | *Avengers: Age of Ultron*, *Iron Man 2*, *Captain America: Civil War* | **80.6% – 51.9%** |
| **Toy Story** | *Toy Story 2*, *Toy Story 3*, *Cars 2* | **59.7% – 29.9%** |
| **Avatar** | *Guardians of the Galaxy*, *Aliens*, *Star Trek Beyond* | **40.0% – 39.2%** |

---

## 📂 Project Structure

```text
MovieVerse/
├── app.py                      # Main Streamlit web application
├── build_engine.py             # Feature extraction and similarity index builder
├── requirements.txt            # Production dependencies
├── Procfile                    # Web service process configuration (for Render)
├── .gitignore                  # Git tracking rules
├── run_movieverse.bat          # 1-click Windows desktop launcher
├── README.md                   # Project documentation
├── README_VIVA_GUIDE.md        # Comprehensive academic viva guide & defense points
├── MovieVerse_Presentation.pptx# Minimalist 16:9 PowerPoint presentation deck
└── data/
    ├── clean_movies.csv        # Preprocessed 4,138 quality film catalog
    └── recs_cache.pkl          # Precomputed similarity lookup dictionary
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/Mahfuz5634/MovieVerse.git
cd MovieVerse
```

### 2. Create and Activate Virtual Environment
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Web Application
```bash
streamlit run app.py
```
> The application will automatically open in your browser at `http://localhost:8501`.  
> *(On Windows, you can simply double-click `run_movieverse.bat` to launch instantly!)*

---

## 🌐 Cloud Deployment

### Deploying on Render (Free Web Service)
1. Fork or push this repository to your GitHub account.
2. In [Render.com](https://render.com), click **New +** $\rightarrow$ **Web Service**.
3. Select your `MovieVerse` repository.
4. Configure settings:
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`
5. Click **Deploy Web Service**.

### Deploying on Streamlit Community Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io).
2. Connect your GitHub repository: `Mahfuz5634/MovieVerse`.
3. Set main file path to `app.py` and click **Deploy**!

---

## 👨‍💻 Author

**Mahfuz**  
- GitHub: [@Mahfuz5634](https://github.com/Mahfuz5634)  
- Academic Project: *CSE 426 – Data Mining & Warehouse Lab*

---

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).
