# 🍽️ Dish Genie

**Dish Genie** is a Python Flask-based web application that helps users find delicious recipes across Indian, Italian, and Mexican cuisines. With a clean interface, downloadable PDFs, and stylish visuals, it's your personal kitchen assistant!

---

## 🚀 Features

- 🔍 Search or select cuisines to get tailored recipes
- 📄 Download recipe PDFs
- 🖼️ Styled with custom images and HTML templates
- ⚙️ Easily deployable to platforms like Render

---

## 📁 Project Structure

```
Dish-Genie/
│
├── static/                  # Static assets
│   ├── genie_loading.png
│   ├── ingredients_background.png
│   └── logo.png
│
├── templates/               # HTML templates
│   ├── index.html
│   ├── landing.html
│   └── result.html
│
├── indian_recipes.pdf       # Recipe PDFs
├── italian_recipes.pdf
├── mexican_recipes.pdf
│
├── app.py                   # Main Flask application
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (not tracked in Git)
├── .gitattributes
```

---

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/dish-genie.git
cd dish-genie
```

### 2. Create a Virtual Environment (optional)

```bash
python -m venv venv
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate          # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask App

```bash
python app.py
```

Then open your browser and go to:  
`http://localhost:5000`

---

## 🌐 Deployment on Render

1. Push your project to GitHub
2. Go to [https://render.com](https://render.com)
3. Click "New" → "Web Service"
4. Connect your GitHub repo
5. Fill in:
   - **Start Command**: `gunicorn app:app`
   - **Runtime**: Python 3
   - Add environment variables from your `.env` file (if needed)
6. Click **Create Web Service**

Render will automatically build and deploy your Flask app!

---

## 📸 Screenshots

> *(Add screenshots here when available)*

---

## 📜 License

This project is licensed under the **MIT License** — feel free to use, share, and modify.

---

## 🙌 Acknowledgements

- [Flask](https://flask.palletsprojects.com/) – Web framework
- [Render](https://render.com) – Easy cloud hosting
- You – for trying Dish Genie! ❤️

---

## 🧠 Future Improvements

- User accounts and recipe saving
- More cuisines and meal types
- AI-powered recipe generation from ingredients

---

Enjoy cooking with **Dish Genie**! 🍳✨

