# ✂️ Urban Cuts - Smart Salon Queue Management System<br>
<br>
![Urban Cuts Banner](https://via.placeholder.com/1200x400.png?text=Urban+Cuts+-+Smart+Salon+Queue+Management)<br>
<br>
> **Say goodbye to long, uncertain waiting times at the salon.** Urban Cuts is a real-time, full-stack web application designed to digitize local salons. It offers a transparent queue management system where customers can book their turn and track their waiting time from home, while salon owners manage everything via a sleek admin dashboard.<br>
<br>
---<br>
<br>
## 🚀 Live Demo<br>
* **Customer App:** [Insert your Netlify Link here]<br>
* **Admin Dashboard:** [Insert your Netlify Link/admin.html here]<br>
* *(Note: Backend is hosted on free tier, please allow 50 seconds for the server to wake up on the first request.)*<br>
<br>
---<br>
<br>
## ✨ Key Features<br>
<br>
### For Customers (User Interface)<br>
* **Real-Time Queue Tracking:** View the live number of people ahead and the estimated waiting time.<br>
* **Smart Token System:** Receive a unique token number upon booking to track your exact turn.<br>
* **Multi-Service Selection:** Choose multiple services (e.g., Haircut + Beard Trim) in a single booking.<br>
* **Spam Protection:** System prevents multiple active bookings from the same phone number to avoid queue clutter.<br>
* **Premium UI/UX:** Built with a modern dark theme and glassmorphism elements.<br>
<br>
### For Salon Owners (Admin Dashboard)<br>
* **Live Queue Dashboard:** View all pending customers instantly without refreshing the page.<br>
* **One-Click Completion:** Mark a customer's service as "Done" to instantly update the live queue for everyone else.<br>
* **Direct Contact:** Integrated "Call" button to directly dial the customer if they aren't present.<br>
* **Analytics at a Glance:** See total pending customers and total estimated workload.<br>
<br>
---<br>
<br>
## 🛠️ Tech Stack<br>
<br>
**Frontend:**<br>
* HTML5, CSS3 (Modern UI/UX)<br>
* Vanilla JavaScript (Fetch API for asynchronous requests)<br>
* Hosted on: **Netlify**<br>
<br>
**Backend:**<br>
* Python 3<br>
* Flask (Web Framework)<br>
* Flask-SQLAlchemy (ORM)<br>
* Flask-CORS<br>
* Hosted on: **Render**<br>
<br>
**Database:**<br>
* PostgreSQL (Cloud Database on Render)<br>
<br>
---<br>
<br>
## ⚙️ How It Works (System Architecture)<br>
1. **Booking:** Customer selects services and submits details via the frontend.<br>
2. **Validation:** Backend verifies if the phone number already has a pending slot. If clear, it assigns a Token ID.<br>
3. **Database:** Data is securely stored in the PostgreSQL database.<br>
4. **Polling:** The frontend fetches `/status` every 5 seconds to update the live wait time and current token dynamically.<br>
5. **Execution:** The admin clicks "Done" on their dashboard, which triggers a `POST /complete/<id>` request, updating the database and instantly reducing the wait time for the next customers.<br>
<br>
---<br>
<br>
## 💻 Local Setup & Installation<br>
<br>
Want to run this project on your local machine? Follow these steps:<br>
<br>
### Prerequisites<br>
* Python 3.x installed<br>
* PostgreSQL installed locally (or a cloud DB URL)<br>
<br>
### Backend Setup<br>
1. Clone the repository:<br>
   `git clone https://github.com/yourusername/salon-startup.git`<br>
   `cd salon-startup`<br>
2. Create a virtual environment (optional but recommended):<br>
   `python -m venv venv`<br>
   `source venv/bin/activate  # On Windows use: venv\Scripts\activate`<br>
3. Install the required dependencies:<br>
   `pip install -r requirements.txt`<br>
4. Set up the Database:<br>
   * Open `app.py` and modify the fallback SQLite URL or set a `DATABASE_URL` environment variable pointing to your local PostgreSQL instance.<br>
5. Run the server:<br>
   `python app.py`<br>
   *The server will start on http://127.0.0.1:5000*<br>
<br>
### Frontend Setup<br>
1. Open `index.html` and `admin.html`.<br>
2. Change the `API_URL` variable to your local server:<br>
   `const API_URL = "http://127.0.0.1:5000";`<br>
3. Open `index.html` in your browser (preferably using a Live Server extension).<br>
<br>
---<br>
<br>
## 🔮 Future Scope<br>
- [ ] Add SMS/WhatsApp notifications using Twilio API when the user's turn is approaching.<br>
- [ ] Implement AI-based dynamic wait time prediction based on historical data.<br>
- [ ] Add specific Barber selection functionality.<br>
- [ ] Salon owner authentication (Login system for Admin panel).<br>
<br>
---<br>
<br>
## 👨‍💻 Author<br>
Built with ❤️ by **Pratham Kumar Singh**<br>
* Passionate about AI, Data Science, and building startups that solve real-world problems.<br>

