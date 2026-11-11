"""
=============================================================================
MovieVerse - Presentation Generator (.pptx)
CSE 426: Data Mining & Warehouse Lab
Design: Minimal, Dark Cinema Aesthetic, Zero AI Clutter / No AI Icons
=============================================================================
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # -------------------------------------------------------------------------
    # COLOR PALETTE (Minimalist Dark Cinema Style - Letterboxd / Criterion / IMDb)
    # -------------------------------------------------------------------------
    BG_DARK     = RGBColor(11, 15, 23)      # #0B0F17 Deep Charcoal Slate
    CARD_BG     = RGBColor(21, 29, 42)      # #151D2A Elevated Surface Card
    CARD_BORDER = RGBColor(38, 51, 71)      # #263347 Subtle Border
    TEXT_MAIN   = RGBColor(248, 250, 252)   # #F8FAFC Crisp White
    TEXT_MUTED  = RGBColor(148, 163, 184)   # #94A3B8 Slate Gray
    ACCENT_RED  = RGBColor(229, 9, 20)      # #E50914 Cinema Red
    ACCENT_GOLD = RGBColor(245, 197, 24)    # #F5C518 IMDb Gold
    ACCENT_MINT = RGBColor(16, 185, 129)    # #10B981 Match Metric Green

    def set_slide_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_DARK
        bg.line.fill.background()
        return bg

    def add_header(slide, title_text, category="CSE 426: DATA MINING & WAREHOUSE LAB"):
        # Category subtitle
        cat_box = slide.shapes.add_textbox(Inches(0.9), Inches(0.45), Inches(11.5), Inches(0.35))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category.upper()
        p_cat.font.size = Pt(11)
        p_cat.font.bold = True
        p_cat.font.color.rgb = ACCENT_RED
        p_cat.font.name = "Arial"

        # Main Title
        title_box = slide.shapes.add_textbox(Inches(0.9), Inches(0.78), Inches(11.5), Inches(0.65))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(24)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_MAIN
        p_title.font.name = "Arial"

        # Subtle divider line
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.9), Inches(1.5), Inches(11.533), Inches(0.02))
        line.fill.solid()
        line.fill.fore_color.rgb = CARD_BORDER
        line.line.fill.background()

    def add_card(slide, left, top, width, height, bg_color=CARD_BG, border_color=CARD_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1)
        return card

    # =========================================================================
    # SLIDE 1: TITLE SLIDE (Cover)
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide1)

    # Accent decorative top bar
    top_bar = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.9), Inches(1.2), Inches(1.2), Inches(0.06))
    top_bar.fill.solid()
    top_bar.fill.fore_color.rgb = ACCENT_RED
    top_bar.line.fill.background()

    # Title & Subtitle Box
    title_box = slide1.shapes.add_textbox(Inches(0.9), Inches(1.5), Inches(11.5), Inches(2.2))
    tf1 = title_box.text_frame
    tf1.word_wrap = True

    p_proj = tf1.paragraphs[0]
    p_proj.text = "MOVIEVERSE"
    p_proj.font.size = Pt(46)
    p_proj.font.bold = True
    p_proj.font.color.rgb = TEXT_MAIN
    p_proj.font.name = "Arial"

    p_sub = tf1.add_paragraph()
    p_sub.text = "Content-Based Movie Recommendation System Using Cosine Similarity"
    p_sub.font.size = Pt(20)
    p_sub.font.color.rgb = ACCENT_GOLD
    p_sub.font.name = "Arial"
    p_sub.space_before = Pt(10)

    p_desc = tf1.add_paragraph()
    p_desc.text = "An interactive, vector-space discovery engine analyzing 4,100+ films based on genres, director, cast, and thematic keywords."
    p_desc.font.size = Pt(14)
    p_desc.font.color.rgb = TEXT_MUTED
    p_desc.font.name = "Arial"
    p_desc.space_before = Pt(8)

    # Metadata Card (Student details)
    add_card(slide1, Inches(0.9), Inches(4.2), Inches(11.533), Inches(2.2))

    meta_box = slide1.shapes.add_textbox(Inches(1.2), Inches(4.45), Inches(11.0), Inches(1.7))
    tf_meta = meta_box.text_frame
    tf_meta.word_wrap = True

    p1 = tf_meta.paragraphs[0]
    p1.text = "ACADEMIC PRESENTATION DETAILS"
    p1.font.size = Pt(11)
    p1.font.bold = True
    p1.font.color.rgb = ACCENT_RED

    p2 = tf_meta.add_paragraph()
    p2.text = "Course: CSE 426 – Data Mining & Warehouse Lab  |  Semester: 6th Semester"
    p2.font.size = Pt(14)
    p2.font.bold = True
    p2.font.color.rgb = TEXT_MAIN
    p2.space_before = Pt(8)

    p3 = tf_meta.add_paragraph()
    p3.text = "Student Name: [Your Name]      Student ID: [Your Student ID]      Section: [Your Section]"
    p3.font.size = Pt(13)
    p3.font.color.rgb = TEXT_MUTED
    p3.space_before = Pt(6)

    p4 = tf_meta.add_paragraph()
    p4.text = "Submitted To: [Course Teacher's Name]  |  Department of Computer Science and Engineering"
    p4.font.size = Pt(13)
    p4.font.color.rgb = TEXT_MUTED
    p4.space_before = Pt(4)

    # =========================================================================
    # SLIDE 2: PROBLEM STATEMENT & MOTIVATION
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide2)
    add_header(slide2, "1. Project Motivation & Problem Statement")

    # 3 Cards Layout
    col_w = Inches(3.64)
    gap = Inches(0.3)
    left_start = Inches(0.9)
    top_pos = Inches(1.8)
    card_h = Inches(5.0)

    # Card 1: The Challenge
    add_card(slide2, left_start, top_pos, col_w, card_h)
    tb1 = slide2.shapes.add_textbox(left_start + Inches(0.25), top_pos + Inches(0.25), col_w - Inches(0.5), card_h - Inches(0.5))
    tf_c1 = tb1.text_frame
    tf_c1.word_wrap = True
    p = tf_c1.paragraphs[0]
    p.text = "THE PROBLEM"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ACCENT_RED
    
    p = tf_c1.add_paragraph()
    p.text = "Choice Overload in Streaming"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = TEXT_MAIN
    p.space_before = Pt(8)

    p = tf_c1.add_paragraph()
    p.text = "• Modern audiences face thousands of movies on platforms like Netflix and Amazon Prime.\n\n• Over 70% of viewers spend 10+ minutes browsing without deciding what to watch.\n\n• The 'paradox of choice' leads to user frustration and decision fatigue."
    p.font.size = Pt(13)
    p.font.color.rgb = TEXT_MUTED
    p.space_before = Pt(14)

    # Card 2: Failure of Basic Search
    add_card(slide2, left_start + col_w + gap, top_pos, col_w, card_h)
    tb2 = slide2.shapes.add_textbox(left_start + col_w + gap + Inches(0.25), top_pos + Inches(0.25), col_w - Inches(0.5), card_h - Inches(0.5))
    tf_c2 = tb2.text_frame
    tf_c2.word_wrap = True
    p = tf_c2.paragraphs[0]
    p.text = "EXISTING LIMITATION"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GOLD

    p = tf_c2.add_paragraph()
    p.text = "Keyword Search is Inadequate"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = TEXT_MAIN
    p.space_before = Pt(8)

    p = tf_c2.add_paragraph()
    p.text = "• Traditional database search only matches exact strings in titles.\n\n• It fails to capture artistic style, directorial vision, pacing, or thematic tone.\n\n• A fan of Christopher Nolan's 'Inception' wants films with similar mood and intellect, not just words matching 'Dream'."
    p.font.size = Pt(13)
    p.font.color.rgb = TEXT_MUTED
    p.space_before = Pt(14)

    # Card 3: Our Solution
    add_card(slide2, left_start + (col_w + gap) * 2, top_pos, col_w, card_h)
    tb3 = slide2.shapes.add_textbox(left_start + (col_w + gap) * 2 + Inches(0.25), top_pos + Inches(0.25), col_w - Inches(0.5), card_h - Inches(0.5))
    tf_c3 = tb3.text_frame
    tf_c3.word_wrap = True
    p = tf_c3.paragraphs[0]
    p.text = "THE SOLUTION"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ACCENT_MINT

    p = tf_c3.add_paragraph()
    p.text = "MovieVerse Vector Similarity"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = TEXT_MAIN
    p.space_before = Pt(8)

    p = tf_c3.add_paragraph()
    p.text = "• Content-Based Vector Space Modeling.\n\n• Transforms film attributes (director, genre, cast, plot keywords) into multidimensional vectors.\n\n• Uses Cosine Similarity to find mathematically nearest films in semantic space.\n\n• Delivers real-time recommendations with match percentages."
    p.font.size = Pt(13)
    p.font.color.rgb = TEXT_MUTED
    p.space_before = Pt(14)

    # =========================================================================
    # SLIDE 3: DATASET ARCHITECTURE
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide3)
    add_header(slide3, "2. Dataset Description & Provenance")

    # Left Card: Dataset Overview
    add_card(slide3, Inches(0.9), Inches(1.8), Inches(5.6), Inches(5.0))
    tb_d1 = slide3.shapes.add_textbox(Inches(1.2), Inches(2.05), Inches(5.0), Inches(4.5))
    tf_d1 = tb_d1.text_frame
    tf_d1.word_wrap = True

    p = tf_d1.paragraphs[0]
    p.text = "DATASET PROVENANCE"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ACCENT_RED

    p = tf_d1.add_paragraph()
    p.text = "The Movie Database (TMDb) 5000"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = TEXT_MAIN
    p.space_before = Pt(6)

    p = tf_d1.add_paragraph()
    p.text = "• Source: Published on Kaggle via The Movie Database (TMDb) official API.\n\n• Raw Catalog Size: 4,803 feature-length films.\n\n• Cleaned Verified Catalog: 4,138 quality titles retained after pruning unreleased, zero-vote, or noisy records (threshold: vote_count >= 20).\n\n• Real-Time Asset Linking: TMDb Movie IDs are utilized to dynamically stream high-resolution official posters."
    p.font.size = Pt(13)
    p.font.color.rgb = TEXT_MUTED
    p.space_before = Pt(14)

    # Right Card: Metadata Schema Breakdown
    add_card(slide3, Inches(6.8), Inches(1.8), Inches(5.633), Inches(5.0))
    tb_d2 = slide3.shapes.add_textbox(Inches(7.1), Inches(2.05), Inches(5.0), Inches(4.5))
    tf_d2 = tb_d2.text_frame
    tf_d2.word_wrap = True

    p = tf_d2.paragraphs[0]
    p.text = "METADATA SCHEMA"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GOLD

    p = tf_d2.add_paragraph()
    p.text = "Key Extracted Features"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = TEXT_MAIN
    p.space_before = Pt(6)

    schema_items = [
        ("title", "Film title (e.g. Inception, The Dark Knight)"),
        ("genres", "Categorical labels (Action, Sci-Fi, Thriller, Drama)"),
        ("director", "Visionary lead (e.g. Christopher Nolan, Quentin Tarantino)"),
        ("cast", "Lead 4 performing actors (e.g. Leonardo DiCaprio)"),
        ("keywords", "Thematic plot tags (dream, heist, subconscious)"),
        ("overview", "Narrative plot synopsis for semantic depth"),
        ("vote_average", "Audience rating metric out of 10.0 scale")
    ]

    for col_name, col_desc in schema_items:
        p = tf_d2.add_paragraph()
        p.text = f"• {col_name}: {col_desc}"
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_MUTED
        p.space_before = Pt(6)

    # =========================================================================
    # SLIDE 4: DATA PREPROCESSING & WEIGHTED FEATURE SOUP
    # =========================================================================
    slide4 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide4)
    add_header(slide4, "3. Data Preprocessing & Weighted Feature Soup")

    # Step 1: Preprocessing steps (Top Card)
    add_card(slide4, Inches(0.9), Inches(1.8), Inches(11.533), Inches(2.2))
    tb_p1 = slide4.shapes.add_textbox(Inches(1.2), Inches(1.95), Inches(11.0), Inches(1.9))
    tf_p1 = tb_p1.text_frame
    tf_p1.word_wrap = True

    p = tf_p1.paragraphs[0]
    p.text = "STAGE 1: CLEANING & TOKEN NORMALIZATION"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = ACCENT_RED

    p = tf_p1.add_paragraph()
    p.text = "Handling Noise & Entity Collision Prevention"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = TEXT_MAIN
    p.space_before = Pt(4)

    p = tf_p1.add_paragraph()
    p.text = "1. Missing Value Imputation: Filled null entries in genre, cast, director, and plot overview.\n2. Entity Merging (Name Collision Fix): Director and actor names are normalized (e.g., 'Christopher Nolan' -> 'ChristopherNolan') so that separate individuals sharing first names (e.g. Tom Hardy vs Tom Cruise) are treated as distinct independent tokens."
    p.font.size = Pt(13)
    p.font.color.rgb = TEXT_MUTED
    p.space_before = Pt(8)

    # Step 2: The Weighted Feature Soup (Bottom Card)
    add_card(slide4, Inches(0.9), Inches(4.3), Inches(11.533), Inches(2.5))
    tb_p2 = slide4.shapes.add_textbox(Inches(1.2), Inches(4.45), Inches(11.0), Inches(2.2))
    tf_p2 = tb_p2.text_frame
    tf_p2.word_wrap = True

    p = tf_p2.paragraphs[0]
    p.text = "STAGE 2: DOMAIN-SPECIFIC FEATURE WEIGHTING"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GOLD

    p = tf_p2.add_paragraph()
    p.text = "Weighted Feature Soup Formulation"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = TEXT_MAIN
    p.space_before = Pt(4)

    p = tf_p2.add_paragraph()
    p.text = "Feature Soup = 3 × (Genres) + 2 × (Director) + 2 × (Keywords) + 2 × (Cast) + (Overview)"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = ACCENT_MINT
    p.space_before = Pt(8)

    p = tf_p2.add_paragraph()
    p.text = "• Why weighting matters: Director and Genre are the strongest signals of audience enjoyment. Weighting prevents a 200-word plot overview from drowning out the primary directorial and genre signature."
    p.font.size = Pt(13)
    p.font.color.rgb = TEXT_MUTED
    p.space_before = Pt(8)

    # =========================================================================
    # SLIDE 5: MATHEMATICAL MODEL (Cosine Similarity)
    # =========================================================================
    slide5 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide5)
    add_header(slide5, "4. The Recommendation Algorithm (Vector Space Model)")

    # Left: Mathematical Formula Box
    add_card(slide5, Inches(0.9), Inches(1.8), Inches(5.6), Inches(5.0))
    tb_m1 = slide5.shapes.add_textbox(Inches(1.2), Inches(2.05), Inches(5.0), Inches(4.5))
    tf_m1 = tb_m1.text_frame
    tf_m1.word_wrap = True

    p = tf_m1.paragraphs[0]
    p.text = "MATHEMATICAL FORMULATION"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ACCENT_RED

    p = tf_m1.add_paragraph()
    p.text = "Cosine Similarity Metric"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = TEXT_MAIN
    p.space_before = Pt(6)

    p = tf_m1.add_paragraph()
    p.text = "Similarity(A, B) = cos(θ) = (A · B) / ( ||A|| × ||B|| )"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GOLD
    p.space_before = Pt(12)

    p = tf_m1.add_paragraph()
    p.text = "=  Σ (Ai × Bi)  /  [ √(Σ Ai²) × √(Σ Bi²) ]"
    p.font.size = Pt(14)
    p.font.color.rgb = TEXT_MAIN
    p.space_before = Pt(6)

    p = tf_m1.add_paragraph()
    p.text = "• Vector Dimension: CountVectorizer constructs a 15,000-dimensional sparse vocabulary matrix.\n\n• Dot Product: Evaluates token co-occurrences between films A and B.\n\n• Normalization: Dividing by Euclidean norms ensures metric bounds between 0.0 (orthogonal/unrelated) and 1.0 (identical match)."
    p.font.size = Pt(13)
    p.font.color.rgb = TEXT_MUTED
    p.space_before = Pt(14)

    # Right: Why Cosine vs Euclidean Distance
    add_card(slide5, Inches(6.8), Inches(1.8), Inches(5.633), Inches(5.0))
    tb_m2 = slide5.shapes.add_textbox(Inches(7.1), Inches(2.05), Inches(5.0), Inches(4.5))
    tf_m2 = tb_m2.text_frame
    tf_m2.word_wrap = True

    p = tf_m2.paragraphs[0]
    p.text = "VIVA DEFENSE JUSTIFICATION"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ACCENT_MINT

    p = tf_m2.add_paragraph()
    p.text = "Why Cosine Over Euclidean?"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = TEXT_MAIN
    p.space_before = Pt(6)

    p = tf_m2.add_paragraph()
    p.text = "1. Invariant to Text Length:\nEuclidean distance is sensitive to vector magnitude. A movie with a lengthy 250-word plot synopsis would have a large Euclidean distance from a movie with a concise 40-word synopsis, even if both share the exact same themes."
    p.font.size = Pt(13)
    p.font.color.rgb = TEXT_MUTED
    p.space_before = Pt(12)

    p = tf_m2.add_paragraph()
    p.text = "2. Focus on Angular Direction:\nCosine similarity measures the angle between vectors rather than Euclidean straight-line distance, evaluating thematic orientation purely on proportions."
    p.font.size = Pt(13)
    p.font.color.rgb = TEXT_MUTED
    p.space_before = Pt(12)

    # =========================================================================
    # SLIDE 6: END-TO-END SYSTEM PIPELINE
    # =========================================================================
    slide6 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide6)
    add_header(slide6, "5. End-to-End System Architecture")

    # 4 Horizontal Pipeline Step Cards
    step_w = Inches(2.7)
    step_gap = Inches(0.24)
    step_top = Inches(2.0)
    step_h = Inches(4.6)

    pipeline_steps = [
        ("STEP 01", "Data Ingestion", "Raw TMDb CSV", "• Load 4,803 records\n• Prune low-vote noise (threshold >= 20)\n• Finalize 4,138 quality catalog titles", ACCENT_RED),
        ("STEP 02", "Feature Soup", "Entity Normalization", "• Clean director & actor spaces\n• Construct weighted soup (Genre×3 + Director×2 + Keywords×2 + Cast + Overview)", ACCENT_GOLD),
        ("STEP 03", "Vector Modeling", "Scikit-Learn Engine", "• CountVectorizer (15k features)\n• Compute Pairwise Cosine Similarity Matrix (4138 × 4138)\n• Cache top-15 matches", ACCENT_MINT),
        ("STEP 04", "Web Application", "Streamlit UI", "• Searchable catalog dropdown\n• Dynamic TMDb poster API\n• Real-time match % badges\n• Interactive slider controls", RGBColor(59, 130, 246))
    ]

    for idx, (step_tag, step_title, step_sub, step_body, col_color) in enumerate(pipeline_steps):
        s_left = Inches(0.9) + idx * (step_w + step_gap)
        add_card(slide6, s_left, step_top, step_w, step_h)

        tb_s = slide6.shapes.add_textbox(s_left + Inches(0.2), step_top + Inches(0.2), step_w - Inches(0.4), step_h - Inches(0.4))
        tf_s = tb_s.text_frame
        tf_s.word_wrap = True

        p = tf_s.paragraphs[0]
        p.text = step_tag
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = col_color

        p = tf_s.add_paragraph()
        p.text = step_title
        p.font.size = Pt(17)
        p.font.bold = True
        p.font.color.rgb = TEXT_MAIN
        p.space_before = Pt(4)

        p = tf_s.add_paragraph()
        p.text = step_sub
        p.font.size = Pt(12)
        p.font.color.rgb = col_color
        p.space_before = Pt(2)

        p = tf_s.add_paragraph()
        p.text = step_body
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_MUTED
        p.space_before = Pt(12)

    # =========================================================================
    # SLIDE 7: LIVE EXPERIMENTAL RESULTS
    # =========================================================================
    slide7 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide7)
    add_header(slide7, "6. Model Verification & Experimental Results")

    # 4 Test Cases Grid (2 rows x 2 cols)
    grid_w = Inches(5.6)
    grid_h = Inches(2.4)
    g_top1 = Inches(1.8)
    g_top2 = Inches(4.5)
    g_left1 = Inches(0.9)
    g_left2 = Inches(6.8)

    test_cases = [
        (g_left1, g_top1, "Test 1: 'Inception' (Sci-Fi / Nolan)", [
            ("Interstellar", "43.0% Match", "8.1 ★"),
            ("Memento", "42.4% Match", "8.1 ★"),
            ("The Prestige", "41.8% Match", "8.0 ★")
        ], ACCENT_RED),
        (g_left2, g_top1, "Test 2: 'The Dark Knight' (Action / Crime)", [
            ("The Dark Knight Rises", "64.2% Match", "7.6 ★"),
            ("Batman Begins", "62.4% Match", "7.5 ★"),
            ("Point Blank", "36.3% Match", "7.1 ★")
        ], ACCENT_GOLD),
        (g_left1, g_top2, "Test 3: 'The Avengers' (Superhero / Franchise)", [
            ("Avengers: Age of Ultron", "80.6% Match", "7.3 ★"),
            ("Iron Man 2", "53.1% Match", "6.6 ★"),
            ("Captain America: Civil War", "51.9% Match", "7.1 ★")
        ], ACCENT_MINT),
        (g_left2, g_top2, "Test 4: 'Toy Story' (Animation / Family)", [
            ("Toy Story 2", "59.7% Match", "7.3 ★"),
            ("Toy Story 3", "47.0% Match", "7.6 ★"),
            ("Cars 2", "29.9% Match", "5.8 ★")
        ], RGBColor(59, 130, 246))
    ]

    for c_left, c_top, case_title, case_items, accent in test_cases:
        add_card(slide7, c_left, c_top, grid_w, grid_h)

        tb_c = slide7.shapes.add_textbox(c_left + Inches(0.25), c_top + Inches(0.2), grid_w - Inches(0.5), grid_h - Inches(0.4))
        tf_c = tb_c.text_frame
        tf_c.word_wrap = True

        p = tf_c.paragraphs[0]
        p.text = case_title
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = accent

        for m_name, m_score, m_rating in case_items:
            p = tf_c.add_paragraph()
            p.text = f"• {m_name}   |   {m_score}   |   Rating: {m_rating}"
            p.font.size = Pt(13)
            p.font.color.rgb = TEXT_MAIN
            p.space_before = Pt(4)

    # =========================================================================
    # SLIDE 8: GRAPHICAL USER INTERFACE
    # =========================================================================
    slide8 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide8)
    add_header(slide8, "7. Graphical User Interface (Streamlit Web App)")

    # Left: UI Philosophy Card
    add_card(slide8, Inches(0.9), Inches(1.8), Inches(5.6), Inches(5.0))
    tb_ui1 = slide8.shapes.add_textbox(Inches(1.2), Inches(2.05), Inches(5.0), Inches(4.5))
    tf_ui1 = tb_ui1.text_frame
    tf_ui1.word_wrap = True

    p = tf_ui1.paragraphs[0]
    p.text = "FRONTEND DESIGN PHILOSOPHY"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ACCENT_RED

    p = tf_ui1.add_paragraph()
    p.text = "Letterboxd / IMDb Cinema Style"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = TEXT_MAIN
    p.space_before = Pt(6)

    p = tf_ui1.add_paragraph()
    p.text = "• Zero Artificial Buzzwords: Designed as an authentic film curation platform rather than generic AI slop.\n\n• High-Contrast Dark Theme: Deep slate (#0B0F17) background with cinema gold and scarlet accents.\n\n• Responsive Multi-Column Layout: Recommendations automatically format across dynamic grid columns.\n\n• Resilient Fallbacks: Offline-ready styling ensures cards display cleanly even when network latency prevents poster loading."
    p.font.size = Pt(13)
    p.font.color.rgb = TEXT_MUTED
    p.space_before = Pt(14)

    # Right: Key Interactive Features
    add_card(slide8, Inches(6.8), Inches(1.8), Inches(5.633), Inches(5.0))
    tb_ui2 = slide8.shapes.add_textbox(Inches(7.1), Inches(2.05), Inches(5.0), Inches(4.5))
    tf_ui2 = tb_ui2.text_frame
    tf_ui2.word_wrap = True

    p = tf_ui2.paragraphs[0]
    p.text = "INTERACTIVE CONTROLS"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GOLD

    p = tf_ui2.add_paragraph()
    p.text = "Core User Capabilities"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = TEXT_MAIN
    p.space_before = Pt(6)

    ui_features = [
        ("Searchable Catalog Dropdown", "Fast lookup across all 4,138 catalog movies."),
        ("Interactive Top-N Slider", "Adjust recommendation count from 3 to 10 in real time."),
        ("Hero Film Showcase", "Displays director, primary cast, genre tags, and story overview."),
        ("Real-Time Poster Streaming", "Fetches authentic official posters via TMDb API."),
        ("Match Percentage Badges", "Transparent mathematical cosine similarity percentage on each card."),
        ("Catalog Explorer Tab", "Browse top-rated films filtered across 12 distinct film genres.")
    ]

    for f_title, f_desc in ui_features:
        p = tf_ui2.add_paragraph()
        p.text = f"• {f_title}: {f_desc}"
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_MUTED
        p.space_before = Pt(6)

    # =========================================================================
    # SLIDE 9: CONCLUSION & VIVA DEFENSE SUMMARY
    # =========================================================================
    slide9 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide9)
    add_header(slide9, "8. Conclusion & Viva Defense Summary")

    # 3 Summary Cards
    col_w9 = Inches(3.64)
    gap9 = Inches(0.3)
    left_start9 = Inches(0.9)
    top_pos9 = Inches(1.8)
    card_h9 = Inches(5.0)

    # Card 1: Overcoming Cold-Start
    add_card(slide9, left_start9, top_pos9, col_w9, card_h9)
    tb_c1 = slide9.shapes.add_textbox(left_start9 + Inches(0.25), top_pos9 + Inches(0.25), col_w9 - Inches(0.5), card_h9 - Inches(0.5))
    tf_e1 = tb_c1.text_frame
    tf_e1.word_wrap = True
    p = tf_e1.paragraphs[0]
    p.text = "KEY ADVANTAGE 1"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ACCENT_RED
    
    p = tf_e1.add_paragraph()
    p.text = "Solves the Cold-Start Problem"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = TEXT_MAIN
    p.space_before = Pt(8)

    p = tf_e1.add_paragraph()
    p.text = "• Collaborative filtering fails when a newly added movie has zero ratings.\n\n• Content-Based Filtering relies strictly on film metadata (genres, director, cast).\n\n• Newly released films can be recommended immediately upon catalog ingestion."
    p.font.size = Pt(13)
    p.font.color.rgb = TEXT_MUTED
    p.space_before = Pt(14)

    # Card 2: Transparency & Explainability
    add_card(slide9, left_start9 + col_w9 + gap9, top_pos9, col_w9, card_h9)
    tb_c2 = slide9.shapes.add_textbox(left_start9 + col_w9 + gap9 + Inches(0.25), top_pos9 + Inches(0.25), col_w9 - Inches(0.5), card_h9 - Inches(0.5))
    tf_e2 = tb_c2.text_frame
    tf_e2.word_wrap = True
    p = tf_e2.paragraphs[0]
    p.text = "KEY ADVANTAGE 2"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GOLD

    p = tf_e2.add_paragraph()
    p.text = "High Model Explainability"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = TEXT_MAIN
    p.space_before = Pt(8)

    p = tf_e2.add_paragraph()
    p.text = "• Deep neural networks often function as black boxes.\n\n• Vector Space Cosine Similarity provides clear interpretability:\n'Film B is recommended because it shares Christopher Nolan as director, Science Fiction as genre, and Hans Zimmer themes.'\n\n• Ideal for academic defense."
    p.font.size = Pt(13)
    p.font.color.rgb = TEXT_MUTED
    p.space_before = Pt(14)

    # Card 3: Lab Curriculum Connection
    add_card(slide9, left_start9 + (col_w9 + gap9) * 2, top_pos9, col_w9, card_h9)
    tb_c3 = slide9.shapes.add_textbox(left_start9 + (col_w9 + gap9) * 2 + Inches(0.25), top_pos9 + Inches(0.25), col_w9 - Inches(0.5), card_h9 - Inches(0.5))
    tf_e3 = tb_c3.text_frame
    tf_e3.word_wrap = True
    p = tf_e3.paragraphs[0]
    p.text = "ACADEMIC RELEVANCE"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ACCENT_MINT

    p = tf_e3.add_paragraph()
    p.text = "Curriculum Alignment"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = TEXT_MAIN
    p.space_before = Pt(8)

    p = tf_e3.add_paragraph()
    p.text = "• Directly implements CSE 426 Lab: Recommendation Systems & Similarity Metrics.\n\n• Integrates Data Preprocessing, Vector Space Modeling, Sparse Matrix Operations, and Web Deployment.\n\n• Demonstrates complete end-to-end data mining lifecycle."
    p.font.size = Pt(13)
    p.font.color.rgb = TEXT_MUTED
    p.space_before = Pt(14)

    # Save presentation
    output_path = 'd:/6th Semester/NN lab/MovieVerse/MovieVerse_Presentation.pptx'
    prs.save(output_path)
    print(f"Presentation saved successfully to: {output_path}")

if __name__ == '__main__':
    create_presentation()
