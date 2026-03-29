# Zero to Data Scientist

## Overview

**Who this is for:** Complete beginners with little or no programming experience who want to land their first data science, data analyst, or ML engineer role.

**Estimated total time:** 8–12 months (assuming 10–15 hours per week)

**Roadmap:** [Data Scientist Roadmap](../Roadmaps/Data-Scientist.md)

This path takes you from zero programming knowledge to a portfolio strong enough to apply for junior data science or data analyst roles. You'll learn Python and statistics fundamentals, then move into data manipulation, visualization, and machine learning, finishing with end-to-end projects that demonstrate real analytical thinking.

---

## Phase 1: Python & Statistics Fundamentals (~6 weeks)

**Goal:** Write Python confidently and understand the statistical concepts that underpin data science.

**Roadmap:** [Data Scientist Roadmap](../Roadmaps/Data-Scientist.md)

**What to learn:**
- Python syntax: variables, data types, control flow, functions, list comprehensions
- Data structures: lists, dictionaries, sets, tuples
- File I/O: reading and writing CSV and JSON files
- Descriptive statistics: mean, median, mode, variance, standard deviation
- Probability basics: distributions, conditional probability, Bayes' theorem
- NumPy fundamentals: arrays, vectorized operations, broadcasting

**Projects to Build:**

1. [Frequency Counter (Word/Character)](../Project-Ideas/Beginner/README.md) — Analyze a text file and compute word frequency distributions. Introduces counting, sorting, and basic statistical summaries.
2. [Grade Calculator](../Project-Ideas/Beginner/README.md) — Extend this to compute class-wide statistics (mean, median, standard deviation, percentiles) and generate a grade distribution report.

**Resources:**
- [Python Cheatsheet](../Resources/Cheatsheets/Python-Cheatsheet.md) — syntax reference for the language features you're learning
- [Python Snippets](../Resources/Snippets/Python-Snippets.md) — reusable patterns for data processing, string manipulation, and file I/O
- [Git Cheatsheet](../Resources/Cheatsheets/Git-Cheatsheet.md) — version control for your notebooks and scripts
- [Linux/Bash Cheatsheet](../Resources/Cheatsheets/Linux-Bash-Cheatsheet.md) — terminal commands for navigating files and running scripts
- [Developer Workflow Guide](../Resources/Guides/Developer-Workflow-Guide.md) — set up pyenv, virtual environments, and Jupyter

**Milestone:** You can write Python scripts that read data files, compute descriptive statistics, and output formatted summaries.

---

## Phase 2: Data Manipulation & Visualization (~6 weeks)

**Goal:** Clean, transform, and visualize real-world datasets using pandas and matplotlib.

**Roadmap:** [Data Scientist Roadmap](../Roadmaps/Data-Scientist.md)

**What to learn:**
- pandas: DataFrames, Series, indexing, filtering, groupby, merge, pivot tables
- Data cleaning: handling missing values, duplicates, type conversion, outliers
- matplotlib and seaborn: line charts, bar charts, scatter plots, histograms, heatmaps
- Exploratory Data Analysis (EDA) workflow
- SQL for data analysis: SELECT, JOIN, GROUP BY, window functions
- Working with real datasets (Kaggle, UCI ML Repository, government open data)

**Projects to Build:**

3. [Personal Budget Tracker](../Project-Ideas/Beginner/README.md) — Extend this to load transaction data from CSV, clean it with pandas, and generate matplotlib visualizations of spending by category over time.
4. [Data Analysis CLI Tool](../Project-Ideas/Intermediate/README.md) — Build the full CLI: load CSVs, compute statistics, filter rows, group and aggregate, and generate ASCII bar charts. This is a core data analyst skill.

**Resources:**
- [SQL Cheatsheet](../Resources/Cheatsheets/SQL-Cheatsheet.md) — SQL syntax for querying databases and data warehouses
- [Sorting Algorithms](../Resources/Algorithms/Sorting-Algorithms.md) — understand the algorithms behind pandas sort operations
- [Data Structures Reference](../Resources/Algorithms/Data-Structures-Reference.md) — hash maps and trees underpin pandas indexing and groupby

**Milestone:** You can take a raw CSV dataset, clean it with pandas, perform exploratory analysis, and produce a set of visualizations that tell a clear story.

---

## Phase 3: Machine Learning Fundamentals (~8 weeks)

**Goal:** Train, evaluate, and interpret machine learning models using scikit-learn.

**Roadmap:** [Data Scientist Roadmap](../Roadmaps/Data-Scientist.md)

**What to learn:**
- Supervised learning: linear regression, logistic regression, decision trees, random forests, SVMs
- Unsupervised learning: k-means clustering, PCA
- Model evaluation: train/test split, cross-validation, confusion matrix, precision/recall, ROC-AUC, RMSE
- Feature engineering: encoding categorical variables, scaling, handling imbalanced data
- Hyperparameter tuning: grid search, random search
- scikit-learn pipeline API
- Introduction to neural networks (perceptron, backpropagation concepts)

**Projects to Build:**

5. [ML Model Training Dashboard](../Project-Ideas/Intermediate/README.md) — Build the backend: upload a CSV, select features and target, train multiple algorithms, and compare evaluation metrics side by side. This is your core ML portfolio piece.
6. [Symptom Tracker & Health Journal](../Project-Ideas/Intermediate/README.md) — Add a correlation analysis feature: use pandas and scipy to find correlations between lifestyle factors (sleep, exercise) and symptom severity scores.

**Resources:**
- [Dynamic Programming](../Resources/Algorithms/Dynamic-Programming.md) — understand optimization concepts that appear in ML algorithms
- [Searching Algorithms](../Resources/Algorithms/Searching-Algorithms.md) — BFS and DFS appear in decision tree traversal and graph-based ML
- [Big-O Cheatsheet](../Resources/Interview-Prep/Big-O-Cheatsheet.md) — understand the computational complexity of the algorithms you're using

**Milestone:** You can train a classification or regression model, evaluate it properly (no data leakage), tune hyperparameters, and explain the results to a non-technical audience.

---

## Phase 4: End-to-End Projects & Interview Prep (~8 weeks)

**Goal:** Build end-to-end data science projects, practice interview questions, and apply for jobs.

**Roadmap:** [Data Scientist Roadmap](../Roadmaps/Data-Scientist.md)

**What to learn:**
- End-to-end ML project structure (data → EDA → features → model → evaluation → presentation)
- Jupyter notebooks for reproducible analysis
- Writing clear data science reports and communicating findings
- SQL for analytics (window functions, CTEs, subqueries)
- A/B testing and statistical significance
- Introduction to deep learning (optional: PyTorch or TensorFlow basics)
- Technical interview patterns for data science (statistics, probability, SQL, ML concepts)

**Projects to Build:**

7. [Workout Tracker App](../Project-Ideas/Intermediate/README.md) — Add a data science layer: analyze workout history to identify trends, predict plateau points, and recommend progressive overload adjustments using regression.
8. [Distributed Online Learning Platform](../Project-Ideas/Advanced/README.md) — Study the recommendation service component. Implement a simplified version: a content-based filtering system that recommends courses based on a learner's completed courses and ratings.

**Resources:**
- [DSA Study Guide](../Resources/Interview-Prep/DSA-Study-Guide.md) — arrays, hash maps, and sorting are common in data science interviews
- [System Design Guide](../Resources/Interview-Prep/System-Design-Guide.md) — data science roles increasingly require understanding of data pipelines and ML systems
- [Behavioral Interview Guide](../Resources/Interview-Prep/Behavioral-Interview-Guide.md) — prepare STAR-format answers; data science interviews often include case study discussions
- [Practice Problems](../Resources/Interview-Prep/Practice-Problems.md) — SQL and statistics problems are common in data science take-home assessments
- [Open Source Guide](../Resources/Guides/Open-Source-Guide.md) — contribute to a data science open source project (scikit-learn, pandas, matplotlib)
- [GitHub Profile Guide](../Resources/Guides/GitHub-Profile-Guide.md) — showcase your notebooks and projects effectively

**Milestone:** You have 2–3 end-to-end data science projects on GitHub with clear README files, visualizations, and written conclusions. You can answer statistics and SQL interview questions confidently.

---

## What's Next

After landing your first role, explore:
- [Machine Learning Engineer Roadmap](../Roadmaps/Machine-Learning-Engineer.md) — move from analysis to building production ML systems
- [Advanced Project Ideas](../Project-Ideas/Advanced/README.md) — tackle distributed systems and ML platform architecture
- [System Design Guide](../Resources/Interview-Prep/System-Design-Guide.md) — prepare for senior data science and ML engineering interviews
