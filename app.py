import streamlit as st
import pandas as pd
import numpy as np
import pickle
import urllib.request
import json
import ssl

# -----------------------------------------------------------------------------
# PAGE CONFIGURATION (Clean Cinema Theme - No AI Tropes)
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="MovieVerse | Film Discovery & Recommendation Engine",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# CUSTOM CSS (Sleek Dark Cinema / Letterboxd / IMDb Style)
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    /* Global Styles */
    .reportview-container, .main {
        background-color: #0B0F17;
        color: #E2E8F0;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }

    /* Minimize Default Streamlit Top Gap & Lift Content Up */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 2rem !important;
        padding-left: 2.5rem !important;
        padding-right: 2.5rem !important;
    }

    header[data-testid="stHeader"] {
        background: transparent !important;
        height: 1.5rem !important;
    }

    /* Completely Hide the Streamlit 'Deploy' Button */
    .stDeployButton,
    [data-testid="stAppDeployButton"],
    header .stDeployButton,
    header [data-testid="stAppDeployButton"],
    div[data-testid="stToolbar"] .stDeployButton {
        display: none !important;
        visibility: hidden !important;
    }

    /* Sidebar Top Padding Reduction */
    [data-testid="stSidebarHeader"] {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        min-height: 1.2rem !important;
    }
    
    section[data-testid="stSidebar"] .block-container {
        padding-top: 0rem !important;
    }
    
    [data-testid="stSidebarUserContent"] {
        padding-top: 0rem !important;
    }

    .sidebar-brand-box {
        margin-top: -36px;
        margin-bottom: 10px;
    }
    .sidebar-brand-title {
        font-size: 30px;
        font-weight: 800;
        color: #E50914;
        letter-spacing: -0.5px;
        line-height: 1.1;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .sidebar-brand-sub {
        color: #94A3B8;
        font-size: 13px;
        font-weight: 500;
        margin-top: 4px;
        margin-left: 2px;
    }

    /* Sidebar Clean Controls & Modern SVG Labels */
    .sidebar-label {
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 11.5px;
        font-weight: 700;
        letter-spacing: 0.6px;
        text-transform: uppercase;
        color: #CBD5E1;
        margin-bottom: 5px;
    }
    .sidebar-label svg {
        flex-shrink: 0;
    }

    /* Sleek Selectbox & Slider Styling */
    section[data-testid="stSidebar"] div[data-baseweb="select"] > div {
        background-color: #151D2A !important;
        border: 1px solid #283548 !important;
        border-radius: 8px !important;
        color: #F8FAFC !important;
        transition: border-color 0.2s ease;
    }
    section[data-testid="stSidebar"] div[data-baseweb="select"] > div:hover {
        border-color: #E50914 !important;
    }
    section[data-testid="stSidebar"] div[data-baseweb="slider"] {
        padding-top: 4px;
    }

    /* Minimalist Cinema Tabs (Zero Emojis, Sleek Navigation) */
    button[data-baseweb="tab"] {
        font-size: 14.5px !important;
        font-weight: 600 !important;
        letter-spacing: 0.3px !important;
        color: #94A3B8 !important;
        background: transparent !important;
        padding-top: 4px !important;
        padding-bottom: 10px !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #F8FAFC !important;
        border-bottom-color: #E50914 !important;
    }
    
    /* Header Branding */
    .brand-container {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-top: -12px;
        padding-bottom: 6px;
        border-bottom: 1px solid #1E293B;
        margin-bottom: 18px;
    }
    .brand-title {
        font-size: 32px;
        font-weight: 800;
        letter-spacing: -0.5px;
        color: #F8FAFC;
        margin: 0;
    }
    .brand-title span {
        color: #E50914;
    }
    .brand-subtitle {
        color: #94A3B8;
        font-size: 14px;
        margin-top: 4px;
    }

    /* Selected Movie Hero Banner */
    .hero-card {
        background-color: #151C28;
        border: 1px solid #232D3F;
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 30px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    }
    .hero-title {
        font-size: 26px;
        font-weight: 700;
        color: #FFFFFF;
        margin-bottom: 8px;
    }
    .hero-meta {
        display: flex;
        gap: 16px;
        align-items: center;
        color: #94A3B8;
        font-size: 14px;
        margin-bottom: 14px;
    }
    .rating-badge {
        background-color: #F5C518;
        color: #000000;
        font-weight: 700;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 13px;
    }
    .genre-tag {
        background-color: #1E293B;
        color: #CBD5E1;
        padding: 3px 10px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 500;
        border: 1px solid #334155;
        display: inline-block;
        margin-right: 6px;
    }

    /* Recommendation Cards */
    .movie-card {
        background-color: #151C28;
        border: 1px solid #232D3F;
        border-radius: 10px;
        padding: 12px;
        transition: transform 0.2s ease, border-color 0.2s ease;
        height: 100%;
        display: flex;
        flex-direction: column;
    }
    .movie-card:hover {
        transform: translateY(-4px);
        border-color: #475569;
    }
    .match-badge {
        background-color: #059669;
        color: #FFFFFF;
        font-size: 12px;
        font-weight: 700;
        padding: 3px 8px;
        border-radius: 4px;
        display: inline-block;
        margin-bottom: 8px;
    }
    .card-title {
        font-size: 15px;
        font-weight: 600;
        color: #F1F5F9;
        margin-top: 6px;
        margin-bottom: 4px;
        line-height: 1.3;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }
    .card-subtext {
        font-size: 12px;
        color: #94A3B8;
        margin-bottom: 6px;
    }

    /* Fallback Poster Card */
    .fallback-poster {
        width: 100%;
        height: 280px;
        background-color: #1E293B;
        border-radius: 6px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        padding: 15px;
        color: #94A3B8;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# DATA LOADING & CACHING
# -----------------------------------------------------------------------------
@st.cache_data
def load_movie_data():
    df = pd.read_csv('data/clean_movies.csv')
    with open('data/recs_cache.pkl', 'rb') as f:
        recs_dict = pickle.load(f)
    return df, recs_dict

df, recs_dict = load_movie_data()

# -----------------------------------------------------------------------------
# POSTER FETCHING FUNCTION WITH RAM CACHE
# -----------------------------------------------------------------------------
ctx = ssl._create_unverified_context()

@st.cache_data(show_spinner=False)
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=3) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            poster_path = data.get('poster_path')
            if poster_path:
                return f"https://image.tmdb.org/t/p/w500{poster_path}"
    except Exception:
        pass
    return None

# -----------------------------------------------------------------------------
# SIDEBAR CONTROLS
# -----------------------------------------------------------------------------
st.sidebar.markdown("""
<div class="sidebar-brand-box">
    <div class="sidebar-brand-title">
        <span>🎬</span>
        <span>MOVIEVERSE</span>
    </div>
    <div class="sidebar-brand-sub">
        Content-Based Similarity Engine
    </div>
    <div style="margin-top: 6px; margin-left: 2px; font-size: 12px; color: #94A3B8; display: flex; align-items: center; gap: 6px;">
        <span>By</span>
        <span style="color: #F8FAFC; font-weight: 600; background: #1E293B; border: 1px solid #334155; padding: 1px 8px; border-radius: 4px; font-size: 11px; letter-spacing: 0.5px;">MAHFUZ</span>
    </div>
</div>
""", unsafe_allow_html=True)
st.sidebar.markdown("---")

# Quick search / pick popular movie
popular_presets = [
    "Inception",
    "The Dark Knight",
    "Interstellar",
    "The Avengers",
    "Titanic",
    "Avatar",
    "The Godfather",
    "Pulp Fiction",
    "Gladiator",
    "The Matrix",
    "Fight Club",
    "Toy Story",
    "Jurassic Park",
    "Iron Man",
    "Harry Potter and the Half-Blood Prince"
]

st.sidebar.markdown("""
<div class="sidebar-label">
    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#F5C518" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
    <span>Featured Curations</span>
</div>
""", unsafe_allow_html=True)
selected_preset = st.sidebar.selectbox(
    "Featured Curations",
    ["-- Choose from popular --"] + popular_presets,
    label_visibility="collapsed"
)

# Full catalog searchable dropdown
all_titles = sorted(df['title'].tolist())

if selected_preset != "-- Choose from popular --":
    default_idx = all_titles.index(selected_preset) if selected_preset in all_titles else 0
else:
    default_idx = all_titles.index("Inception") if "Inception" in all_titles else 0

st.sidebar.markdown("""
<div class="sidebar-label" style="margin-top: 14px;">
    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#E50914" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
    <span>Search 4,100+ Catalog</span>
</div>
""", unsafe_allow_html=True)
selected_movie = st.sidebar.selectbox(
    "Search 4,100+ Catalog",
    all_titles,
    index=default_idx,
    label_visibility="collapsed"
)

st.sidebar.markdown("""
<div class="sidebar-label" style="margin-top: 14px;">
    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="4" y1="21" x2="4" y2="14"></line><line x1="4" y1="10" x2="4" y2="3"></line><line x1="12" y1="21" x2="12" y2="12"></line><line x1="12" y1="8" x2="12" y2="3"></line><line x1="20" y1="21" x2="20" y2="16"></line><line x1="20" y1="12" x2="20" y2="3"></line><line x1="1" y1="14" x2="7" y2="14"></line><line x1="9" y1="8" x2="15" y2="8"></line><line x1="17" y1="16" x2="23" y2="16"></line></svg>
    <span>Recommendations Count</span>
</div>
""", unsafe_allow_html=True)
rec_count = st.sidebar.slider(
    "Recommendations Count",
    min_value=3,
    max_value=10,
    value=5,
    step=1,
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
**Model Specification:**
- **Technique:** Content-Based Filtering
- **Metric:** Cosine Distance & Similarity
- **Features:** Genre, Director, Cast, Keywords
- **Catalog Size:** 4,138 Verified Movies
""")

# -----------------------------------------------------------------------------
# MAIN APP TABS (Clean Professional Typography - Zero AI / Cartoon Emojis)
# -----------------------------------------------------------------------------
tab_discover, tab_browse = st.tabs([
    "Film Recommendations", 
    "Browse by Genre"
])

# -----------------------------------------------------------------------------
# TAB 1: FILM RECOMMENDATIONS
# -----------------------------------------------------------------------------
with tab_discover:
    # Fetch Selected Movie Details
    movie_row = df[df['title'] == selected_movie].iloc[0]
    movie_idx = movie_row.name
    movie_id = int(movie_row['id'])
    
    release_year = str(movie_row['release_date'])[:4] if pd.notna(movie_row['release_date']) else "N/A"
    genres_list = str(movie_row['genres']).split() if pd.notna(movie_row['genres']) else []
    director_name = movie_row['director'] if pd.notna(movie_row['director']) and movie_row['director'] else "Unknown"
    cast_names = ", ".join(str(movie_row['cast']).split(",")[:3]) if pd.notna(movie_row['cast']) else "N/A"
    rating_val = movie_row['vote_average']
    overview_text = movie_row['overview'] if pd.notna(movie_row['overview']) else "No synopsis available."

    # Hero Banner
    col_hero_poster, col_hero_info = st.columns([1, 3.2])

    with col_hero_poster:
        poster_url = fetch_poster(movie_id)
        if poster_url:
            st.image(poster_url, use_container_width=True)
        else:
            st.markdown(f"""
            <div class="fallback-poster">
                <div style="font-size: 36px; margin-bottom: 10px;">🎬</div>
                <div style="font-weight: 600; color: #F1F5F9;">{selected_movie}</div>
                <div style="font-size: 13px;">({release_year})</div>
            </div>
            """, unsafe_allow_html=True)

    with col_hero_info:
        st.markdown(f'<div class="hero-title">{selected_movie} ({release_year})</div>', unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="hero-meta">
            <span class="rating-badge">★ {rating_val:.1f} / 10</span>
            <span>Director: <strong style="color: #F8FAFC;">{director_name}</strong></span>
            <span>Starring: <strong style="color: #F8FAFC;">{cast_names}</strong></span>
        </div>
        """, unsafe_allow_html=True)

        # Genre tags
        genre_badges = "".join([f'<span class="genre-tag">{g}</span>' for g in genres_list])
        st.markdown(f"<div style='margin-bottom: 15px;'>{genre_badges}</div>", unsafe_allow_html=True)

        st.markdown(f"<p style='color: #CBD5E1; font-size: 14px; line-height: 1.6;'>{overview_text}</p>", unsafe_allow_html=True)

    # Recommendation Results Section
    st.markdown(f"### Recommended Films Matching '{selected_movie}'")
    st.caption(f"Ranked by Vector Cosine Similarity (Top {rec_count} Selections)")

    # Retrieve recommendations from precomputed cache
    recs = recs_dict.get(movie_idx, [])[:rec_count]

    if recs:
        # Create dynamic grid columns
        cols = st.columns(len(recs))
        
        for idx, (rec_idx, sim_score) in enumerate(recs):
            rec_row = df.loc[rec_idx]
            rec_id = int(rec_row['id'])
            rec_title = rec_row['title']
            rec_year = str(rec_row['release_date'])[:4] if pd.notna(rec_row['release_date']) else ""
            rec_rating = rec_row['vote_average']
            rec_genres = " • ".join(str(rec_row['genres']).split()[:2])
            match_pct = int(round(sim_score * 100))

            with cols[idx]:
                rec_poster = fetch_poster(rec_id)
                if rec_poster:
                    st.image(rec_poster, use_container_width=True)
                else:
                    st.markdown(f"""
                    <div class="fallback-poster" style="height: 200px;">
                        <div style="font-size: 28px;">🎬</div>
                        <div style="font-size: 13px; font-weight: 600; color: #FFF; margin-top: 5px;">{rec_title}</div>
                    </div>
                    """, unsafe_allow_html=True)

                st.markdown(f"""
                <div style="margin-top: 8px;">
                    <span class="match-badge">{match_pct}% Match</span>
                    <div class="card-title" title="{rec_title}">{rec_title}</div>
                    <div class="card-subtext">{rec_year} | ★ {rec_rating:.1f}</div>
                    <div style="font-size: 11px; color: #64748B;">{rec_genres}</div>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.info("No close matches found for this title.")

# -----------------------------------------------------------------------------
# TAB 2: BROWSE BY GENRE
# -----------------------------------------------------------------------------
with tab_browse:
    st.markdown("### 🍿 Explore Catalog by Genre")
    
    available_genres = [
        "Action", "Adventure", "Animation", "Comedy", "Crime", 
        "Drama", "Fantasy", "Horror", "Mystery", "Romance", 
        "Science Fiction", "Thriller"
    ]
    
    picked_genre = st.selectbox("Select Film Genre:", available_genres, index=0)
    
    # Filter and sort by rating and popularity
    genre_movies = df[df['genres'].str.contains(picked_genre, na=False, case=False)]
    genre_movies = genre_movies.sort_values(by=['vote_average', 'vote_count'], ascending=[False, False]).head(8)
    
    st.write(f"Top-rated **{picked_genre}** films in the MovieVerse database:")
    
    browse_cols = st.columns(4)
    for i, (_, r) in enumerate(genre_movies.iterrows()):
        col_pos = i % 4
        with browse_cols[col_pos]:
            g_poster = fetch_poster(int(r['id']))
            if g_poster:
                st.image(g_poster, use_container_width=True)
            else:
                st.markdown(f"""
                <div class="fallback-poster" style="height: 180px;">
                    <div style="font-size: 24px;">🎬</div>
                    <div style="font-size: 13px; font-weight: 600; color: #FFF;">{r['title']}</div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div style="margin-top: 6px; margin-bottom: 20px;">
                <div class="card-title">{r['title']}</div>
                <div class="card-subtext">{str(r['release_date'])[:4]} | ★ {r['vote_average']:.1f}</div>
            </div>
            """, unsafe_allow_html=True)
