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
