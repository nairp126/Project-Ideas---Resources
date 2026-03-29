# 🚀 Intermediate Project Ideas

Ready to level up? These projects solve real-world problems and focus on **Web Development** and **APIs**. They require planning a database schema and designing a RESTful API.

---

## 1. 📚 Study Group Finder

**Problem Statement:** Students struggle to find peers with similar academic schedules and study preferences for forming effective study groups.

### Key Features (MVP)

* User registration and authentication
* Create and join study groups based on course/subject
* Set availability schedules (weekly calendar)
* Search and filter groups by course, meeting time, location preference
* Basic messaging within groups
* View group member profiles

### Database Schema

```text
Users: id, name, email, password_hash, university, major, created_at
StudyGroups: id, course_name, subject, max_members, meeting_preference, description, creator_id, created_at
GroupMembers: id, group_id, user_id, joined_at
Availability: id, user_id, day_of_week, start_time, end_time
Messages: id, group_id, user_id, content, sent_at
```

### API Endpoints

* `POST /api/auth/register` - Create new user account
* `POST /api/auth/login` - User login
* `GET /api/groups` - List all study groups (with filters)
* `POST /api/groups` - Create a new study group
* `GET /api/groups/:id` - Get group details
* `POST /api/groups/:id/join` - Join a study group
* `DELETE /api/groups/:id/leave` - Leave a study group
* `POST /api/availability` - Set user availability
* `GET /api/groups/:id/messages` - Get group messages
* `POST /api/groups/:id/messages` - Send message to group

---

## 2. 🛠️ Local Service Marketplace

**Problem Statement:** People need reliable recommendations for local services (plumbers, tutors, cleaners) but struggle to find trusted providers in their area.

### Key Features (MVP)

* Service provider registration with profile and skills
* Customer search and filter by service type, location, rating
* Booking/request system for services
* Rating and review system
* Service provider availability calendar
* Basic dashboard for providers to manage requests

### Database Schema

```text
Users: id, name, email, password_hash, role (customer/provider), phone, created_at
Providers: id, user_id, business_name, description, location, category
Services: id, provider_id, service_name, description, price_range
Bookings: id, customer_id, provider_id, service_id, requested_date, status, created_at
Reviews: id, booking_id, customer_id, provider_id, rating, comment, created_at
Availability: id, provider_id, date, is_available
```

### API Endpoints

* `POST /api/auth/register` - Register user (customer or provider)
* `POST /api/auth/login` - User login
* `GET /api/providers` - Search providers (filter by category, location, rating)
* `GET /api/providers/:id` - Get provider profile and services
* `POST /api/bookings` - Create service booking request
* `GET /api/bookings/user/:userId` - Get user's bookings
* `PATCH /api/bookings/:id/status` - Update booking status (accept/reject/complete)
* `POST /api/reviews` - Submit review for completed service
* `GET /api/providers/:id/reviews` - Get provider reviews
* `POST /api/providers/:id/availability` - Set provider availability

---

## 3. 💸 Expense Splitting App

**Problem Statement:** Roommates and friends find it tedious to track shared expenses and settle debts, leading to awkward conversations and forgotten payments.

### Key Features (MVP)

* User registration and friend connections
* Create groups (household, trip, etc.)
* Add expenses with split options (equal, percentage, custom amounts)
* Track who owes whom
* Settle up functionality to record payments
* View balance summary and transaction history
* Export group expenses as CSV

### Database Schema

```text
Users: id, name, email, password_hash, created_at
Groups: id, name, description, created_by, created_at
GroupMembers: id, group_id, user_id, joined_at
Expenses: id, group_id, description, total_amount, paid_by_user_id, date, created_at
ExpenseSplits: id, expense_id, user_id, amount_owed
Settlements: id, group_id, paid_by_user_id, paid_to_user_id, amount, date, created_at
```

### API Endpoints

* `POST /api/auth/register` - Register new user
* `POST /api/auth/login` - User login
* `POST /api/groups` - Create new group
* `POST /api/groups/:id/members` - Add member to group
* `GET /api/groups/:id` - Get group details and members
* `POST /api/expenses` - Add new expense
* `GET /api/groups/:id/expenses` - Get all expenses for a group
* `GET /api/groups/:id/balances` - Calculate current balances (who owes whom)
* `POST /api/settlements` - Record a payment/settlement
* `GET /api/groups/:id/export` - Export expenses as CSV
* `DELETE /api/expenses/:id` - Delete expense

---

## 4. 🥗 Recipe Meal Planner

**Problem Statement:** People waste time deciding what to cook daily and often end up with unused groceries because they lack organized meal planning.

### Key Features (MVP)

* Browse and search recipes by ingredients, cuisine, dietary restrictions
* Weekly meal planner calendar
* Automatic shopping list generation from planned meals
* Mark items as purchased on shopping list
* Save favorite recipes
* Basic nutrition information display

### Database Schema

```text
Users: id, name, email, password_hash, dietary_preferences, created_at
Recipes: id, title, description, cuisine_type, prep_time, cook_time, servings, instructions, created_at
Ingredients: id, name, category (produce, dairy, meat, etc.)
RecipeIngredients: id, recipe_id, ingredient_id, quantity, unit
MealPlans: id, user_id, recipe_id, planned_date, meal_type (breakfast/lunch/dinner)
ShoppingLists: id, user_id, created_at
ShoppingListItems: id, list_id, ingredient_id, quantity, unit, is_purchased
Favorites: id, user_id, recipe_id, created_at
```

### API Endpoints

* `POST /api/auth/register` - Register user
* `POST /api/auth/login` - User login
* `GET /api/recipes` - Search/filter recipes
* `GET /api/recipes/:id` - Get recipe details with ingredients and instructions
* `POST /api/recipes` - Create custom recipe
* `POST /api/meal-plans` - Add recipe to meal plan
* `GET /api/meal-plans/week/:date` - Get week's meal plan
* `DELETE /api/meal-plans/:id` - Remove from meal plan
* `POST /api/shopping-lists/generate` - Generate shopping list from meal plan
* `GET /api/shopping-lists/:id` - Get shopping list
* `PATCH /api/shopping-lists/:id/items/:itemId` - Mark item as purchased
* `POST /api/favorites` - Save recipe to favorites
* `GET /api/users/:id/favorites` - Get user's favorite recipes

---

## 5. 🅿️ Parking Spot Finder

**Problem Statement:** Drivers waste time and fuel circling neighborhoods looking for parking, especially in urban areas, while some people have unused parking spaces.

### Key Features (MVP)

* List parking spots (driveway, garage) with availability schedule
* Search spots by location, date/time, price
* Real-time availability status
* Booking and payment integration (simplified with status tracking)
* Rating system for spots and renters
* Map view of available spots
* Host dashboard to manage listings and bookings

### Database Schema

```text
Users: id, name, email, password_hash, phone, role (renter/host/both), created_at
ParkingSpots: id, host_id, address, latitude, longitude, spot_type, price_per_hour, description, photos
Availability: id, spot_id, date, start_time, end_time, is_available
Bookings: id, spot_id, renter_id, start_datetime, end_datetime, total_price, status, created_at
Payments: id, booking_id, amount, payment_status, transaction_id, created_at
Reviews: id, booking_id, reviewer_id, reviewee_id, rating, comment, created_at
```

### API Endpoints

* `POST /api/auth/register` - Register user
* `POST /api/auth/login` - User login
* `POST /api/spots` - List a new parking spot
* `GET /api/spots` - Search spots (filter by location, date, time, price)
* `GET /api/spots/:id` - Get spot details
* `PATCH /api/spots/:id` - Update spot information
* `POST /api/spots/:id/availability` - Set availability schedule
* `GET /api/spots/:id/availability` - Check availability for date range
* `POST /api/bookings` - Create booking
* `GET /api/bookings/user/:userId` - Get user's bookings (renter or host)
* `PATCH /api/bookings/:id/status` - Update booking status (confirm/cancel/complete)
* `POST /api/payments` - Process payment for booking
* `POST /api/reviews` - Submit review
* `GET /api/spots/:id/reviews` - Get spot reviews

---

## 6. 📊 Personal Finance Dashboard 💰

**Problem Statement:** People struggle to get a unified view of their spending habits across multiple accounts and categories, making it hard to identify where their money actually goes.

### Key Features (MVP)

* Manual transaction entry with category tagging
* Monthly and yearly spending summaries by category
* Budget goal setting per category with progress tracking
* Recurring transaction detection and labeling
* Net worth tracker (assets minus liabilities)
* CSV import from bank exports

### Database Schema

```text
Users: id, name, email, password_hash, currency, created_at
Accounts: id, user_id, name, type (checking/savings/credit/investment), balance, created_at
Transactions: id, account_id, user_id, amount, type (income/expense), category, description, date, is_recurring, created_at
Budgets: id, user_id, category, monthly_limit, created_at
Assets: id, user_id, name, value, type, updated_at
Liabilities: id, user_id, name, amount, type, updated_at
```

### API Endpoints

* `POST /api/auth/register` - Register user
* `POST /api/auth/login` - User login
* `POST /api/accounts` - Add financial account
* `GET /api/accounts` - List user accounts
* `POST /api/transactions` - Add transaction
* `GET /api/transactions` - List transactions (filter by date, category, account)
* `GET /api/reports/monthly` - Monthly spending summary by category
* `POST /api/budgets` - Set budget for a category
* `GET /api/budgets` - Get budgets with current spending progress
* `POST /api/transactions/import` - Import transactions from CSV
* `GET /api/net-worth` - Calculate current net worth

---

## 7. 🏋️ Workout Tracker App

**Problem Statement:** Fitness enthusiasts need a way to log workouts, track progressive overload over time, and visualize their strength gains without relying on expensive apps.

### Key Features (MVP)

* Exercise library with muscle group tagging
* Log workout sessions with sets, reps, and weight
* View personal records (PRs) per exercise
* Progress charts showing weight lifted over time
* Workout plan templates (push/pull/legs, etc.)
* Rest timer between sets

### Database Schema

```text
Users: id, name, email, password_hash, created_at
Exercises: id, name, muscle_group, equipment, description
WorkoutPlans: id, user_id, name, description, created_at
PlanExercises: id, plan_id, exercise_id, sets, reps, order
WorkoutSessions: id, user_id, plan_id, date, duration_minutes, notes
SessionSets: id, session_id, exercise_id, set_number, reps, weight_kg, completed_at
PersonalRecords: id, user_id, exercise_id, weight_kg, reps, achieved_at
```

### API Endpoints

* `POST /api/auth/register` - Register user
* `POST /api/auth/login` - User login
* `GET /api/exercises` - List exercises (filter by muscle group)
* `POST /api/exercises` - Add custom exercise
* `POST /api/plans` - Create workout plan
* `GET /api/plans` - List user's workout plans
* `POST /api/sessions` - Start a workout session
* `POST /api/sessions/:id/sets` - Log a set
* `GET /api/sessions/:id` - Get session details
* `GET /api/exercises/:id/history` - Get lift history for an exercise
* `GET /api/exercises/:id/pr` - Get personal record for an exercise

---

## 8. 🤖 ML Model Training Dashboard

**Problem Statement:** Data science students need a simple interface to train, compare, and evaluate machine learning models on their own datasets without writing boilerplate code every time.

### Key Features (MVP)

* Upload CSV datasets and preview data
* Select target column and feature columns
* Choose from common ML algorithms (linear regression, decision tree, random forest, SVM)
* Train model and display evaluation metrics (accuracy, RMSE, confusion matrix)
* Compare multiple model runs side by side
* Download trained model as a pickle file

### Database Schema

```text
Users: id, name, email, password_hash, created_at
Datasets: id, user_id, name, filename, row_count, column_count, uploaded_at
ModelRuns: id, user_id, dataset_id, algorithm, hyperparameters (JSON), target_column, feature_columns (JSON), status, created_at
ModelMetrics: id, run_id, metric_name, metric_value
ModelFiles: id, run_id, file_path, created_at
```

### API Endpoints

* `POST /api/auth/register` - Register user
* `POST /api/auth/login` - User login
* `POST /api/datasets` - Upload dataset (CSV)
* `GET /api/datasets` - List user datasets
* `GET /api/datasets/:id/preview` - Preview first 50 rows
* `POST /api/models/train` - Start model training job
* `GET /api/models` - List model runs
* `GET /api/models/:id` - Get model run details and metrics
* `GET /api/models/:id/download` - Download trained model file
* `DELETE /api/models/:id` - Delete model run

---

## 9. 📱 Habit Tracker Mobile App

**Problem Statement:** People want to build positive habits but lack a simple, distraction-free tool to track daily streaks and reflect on their consistency over time.

### Key Features (MVP)

* Create habits with name, frequency (daily/weekly), and reminder time
* Check off habits each day
* Streak counter and longest streak tracking
* Weekly and monthly completion heatmap
* Push notification reminders
* Archive completed or abandoned habits

### Database Schema

```text
Users: id, name, email, password_hash, timezone, created_at
Habits: id, user_id, name, description, frequency, target_days (JSON), reminder_time, color, is_archived, created_at
HabitLogs: id, habit_id, user_id, completed_date, created_at
Streaks: id, habit_id, current_streak, longest_streak, last_completed_date, updated_at
```

### API Endpoints

* `POST /api/auth/register` - Register user
* `POST /api/auth/login` - User login
* `POST /api/habits` - Create new habit
* `GET /api/habits` - List active habits
* `PATCH /api/habits/:id` - Update habit settings
* `DELETE /api/habits/:id` - Archive habit
* `POST /api/habits/:id/log` - Mark habit as completed for today
* `DELETE /api/habits/:id/log/:date` - Undo completion for a date
* `GET /api/habits/:id/stats` - Get streak and completion stats
* `GET /api/habits/:id/heatmap` - Get completion data for heatmap view

---

## 10. 🎮 Multiplayer Quiz Game

**Problem Statement:** Friends and classrooms need an engaging real-time quiz platform where a host can run live trivia sessions and participants compete on a leaderboard.

### Key Features (MVP)

* Host creates quiz with multiple-choice questions and time limits
* Players join via a room code
* Real-time question display and answer submission via WebSockets
* Live leaderboard updated after each question
* Host controls question pacing
* End-of-game results summary with correct answers

### Database Schema

```text
Users: id, name, email, password_hash, created_at
Quizzes: id, creator_id, title, description, is_public, created_at
Questions: id, quiz_id, question_text, time_limit_seconds, order
AnswerOptions: id, question_id, option_text, is_correct
GameSessions: id, quiz_id, host_id, room_code, status (waiting/active/finished), started_at, ended_at
GamePlayers: id, session_id, user_id, display_name, score, joined_at
PlayerAnswers: id, session_id, question_id, player_id, selected_option_id, answered_at, is_correct, points_earned
```

### API Endpoints

* `POST /api/auth/register` - Register user
* `POST /api/auth/login` - User login
* `POST /api/quizzes` - Create quiz
* `POST /api/quizzes/:id/questions` - Add question to quiz
* `POST /api/sessions` - Start a game session (returns room code)
* `POST /api/sessions/join` - Join session by room code
* `GET /api/sessions/:id/leaderboard` - Get current leaderboard
* `POST /api/sessions/:id/next` - Host advances to next question
* `POST /api/sessions/:id/answer` - Player submits answer
* `GET /api/sessions/:id/results` - Get final results

---

## 11. 🌿 Plant Care Reminder App

**Problem Statement:** Plant owners forget watering and fertilizing schedules, leading to dead plants. A smart reminder system tailored to each plant's needs would solve this.

### Key Features (MVP)

* Add plants with species, photo, and care schedule (watering frequency, sunlight needs)
* Log care actions (watered, fertilized, repotted)
* Upcoming care tasks dashboard sorted by urgency
* Push/email reminders for overdue care
* Plant health notes and history log
* Species lookup with default care recommendations

### Database Schema

```text
Users: id, name, email, password_hash, notification_preference, created_at
Plants: id, user_id, name, species, photo_url, location, acquired_date, notes, created_at
CareSchedules: id, plant_id, care_type (water/fertilize/repot), frequency_days, last_done_at, next_due_at
CareLogs: id, plant_id, user_id, care_type, notes, logged_at
Species: id, common_name, scientific_name, watering_frequency_days, sunlight, difficulty
```

### API Endpoints

* `POST /api/auth/register` - Register user
* `POST /api/auth/login` - User login
* `POST /api/plants` - Add a plant
* `GET /api/plants` - List user's plants
* `GET /api/plants/:id` - Get plant details and care history
* `PATCH /api/plants/:id` - Update plant info
* `POST /api/plants/:id/care` - Log a care action
* `GET /api/dashboard/upcoming` - Get upcoming care tasks sorted by due date
* `GET /api/species/search` - Search species for care recommendations
* `DELETE /api/plants/:id` - Remove plant

---

## 12. 🗺️ Travel Itinerary Planner

**Problem Statement:** Travelers spend hours across multiple tabs planning trips. A single tool to organize destinations, activities, accommodation, and budgets would save significant time.

### Key Features (MVP)

* Create trips with destination, dates, and travel companions
* Add daily itinerary items (activities, restaurants, transport)
* Accommodation and flight booking notes
* Per-trip budget tracker with expense logging
* Shareable trip link for collaborators
* Packing list generator based on trip duration and destination type

### Database Schema

```text
Users: id, name, email, password_hash, created_at
Trips: id, creator_id, title, destination, start_date, end_date, budget, share_token, created_at
TripCollaborators: id, trip_id, user_id, role (viewer/editor), added_at
ItineraryItems: id, trip_id, day_date, time, title, category (activity/food/transport/accommodation), location, notes, cost
TripExpenses: id, trip_id, user_id, description, amount, category, date
PackingItems: id, trip_id, name, category, is_packed
```

### API Endpoints

* `POST /api/auth/register` - Register user
* `POST /api/auth/login` - User login
* `POST /api/trips` - Create trip
* `GET /api/trips` - List user's trips
* `GET /api/trips/:id` - Get trip with full itinerary
* `POST /api/trips/:id/items` - Add itinerary item
* `PATCH /api/trips/:id/items/:itemId` - Update itinerary item
* `DELETE /api/trips/:id/items/:itemId` - Remove itinerary item
* `POST /api/trips/:id/expenses` - Log trip expense
* `GET /api/trips/:id/budget` - Get budget summary
* `GET /api/trips/shared/:token` - View shared trip (no auth required)

---

## 13. 🔬 Data Analysis CLI Tool

**Problem Statement:** Data analysts need a fast command-line tool to explore CSV datasets, compute statistics, and generate quick visualizations without opening a full notebook environment.

### Key Features (MVP)

* Load CSV files and display schema (column names, types, null counts)
* Compute descriptive statistics (mean, median, std, min, max) per column
* Filter rows by column value conditions
* Group by a column and aggregate (count, sum, mean)
* Export filtered/transformed data to a new CSV
* Generate ASCII bar charts for categorical columns

### Database Schema

```text
Sessions: id, filename, loaded_at, row_count, column_count
AnalysisHistory: id, session_id, command, parameters (JSON), executed_at
SavedFilters: id, session_id, name, filter_expression, created_at
```

### API Endpoints

* `POST /api/sessions` - Load a CSV file into a session
* `GET /api/sessions/:id/schema` - Get column names and types
* `GET /api/sessions/:id/stats` - Get descriptive statistics
* `POST /api/sessions/:id/filter` - Apply row filter
* `POST /api/sessions/:id/groupby` - Group and aggregate data
* `GET /api/sessions/:id/export` - Export current view to CSV
* `POST /api/sessions/:id/chart` - Generate ASCII chart for a column

---

## 14. 🎵 Music Practice Log

**Problem Statement:** Musicians learning an instrument need a structured way to track practice sessions, set goals for pieces they are learning, and measure improvement over time.

### Key Features (MVP)

* Log practice sessions with instrument, duration, and pieces practiced
* Set learning goals for specific pieces (target tempo, target date)
* Track tempo progress over time for each piece
* Weekly practice time summary and streak tracking
* Metronome and timer built into the session logger
* Repertoire list of mastered pieces

### Database Schema

```text
Users: id, name, email, password_hash, primary_instrument, created_at
Pieces: id, user_id, title, composer, difficulty, status (learning/mastered/on_hold), target_tempo, created_at
PracticeSessions: id, user_id, date, total_duration_minutes, notes, created_at
SessionPieces: id, session_id, piece_id, duration_minutes, tempo_achieved, notes
Goals: id, user_id, piece_id, target_tempo, target_date, achieved_at
```

### API Endpoints

* `POST /api/auth/register` - Register user
* `POST /api/auth/login` - User login
* `POST /api/pieces` - Add piece to repertoire
* `GET /api/pieces` - List pieces (filter by status)
* `PATCH /api/pieces/:id` - Update piece status or target
* `POST /api/sessions` - Log practice session
* `GET /api/sessions` - List practice sessions
* `GET /api/pieces/:id/progress` - Get tempo progress history for a piece
* `GET /api/stats/weekly` - Get weekly practice time summary
* `POST /api/goals` - Set a practice goal

---

## 15. 🧬 Symptom Tracker & Health Journal

**Problem Statement:** People managing chronic conditions or tracking their health need a private journal to log symptoms, medications, and lifestyle factors so they can share meaningful data with their doctor.

### Key Features (MVP)

* Daily symptom logging with severity ratings (1–10)
* Medication and supplement tracking with dosage and timing
* Sleep, exercise, and diet logging
* Correlation view showing symptom trends alongside lifestyle factors
* Export health report as PDF for doctor visits
* Reminder notifications for medications

### Database Schema

```text
Users: id, name, email, password_hash, date_of_birth, created_at
Symptoms: id, user_id, name, description, created_at
SymptomLogs: id, user_id, symptom_id, severity, notes, logged_at
Medications: id, user_id, name, dosage, frequency, start_date, end_date
MedicationLogs: id, medication_id, user_id, taken_at, notes
LifestyleLogs: id, user_id, date, sleep_hours, exercise_minutes, water_ml, stress_level, notes
```

### API Endpoints

* `POST /api/auth/register` - Register user
* `POST /api/auth/login` - User login
* `POST /api/symptoms` - Define a tracked symptom
* `POST /api/symptoms/:id/log` - Log symptom occurrence with severity
* `GET /api/symptoms/:id/history` - Get symptom history over time
* `POST /api/medications` - Add medication
* `POST /api/medications/:id/log` - Log medication taken
* `POST /api/lifestyle` - Log daily lifestyle data
* `GET /api/reports/correlation` - Get symptom vs lifestyle correlation data
* `GET /api/reports/export` - Export health report as PDF
