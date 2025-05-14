# app.py
from flask import Flask, render_template, request, session, redirect, url_for
import os
import requests
from dotenv import load_dotenv
from PyPDF2 import PdfReader

app = Flask(__name__)
app.secret_key = os.urandom(24)

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# --- Load Recipe Context from PDFs ---
RECIPE_PDFS = [
    "italian_recipes.pdf",
    "mexican_recipes.pdf",
    "indian_recipes.pdf"
]

def read_pdf(file_path):
    try:
        pdf_reader = PdfReader(file_path)
        text = ""
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text
    except Exception as e:
        print(f"Error reading {file_path}: {str(e)}")
        return ""

recipe_documents = ""
for pdf_file in RECIPE_PDFS:
    if os.path.exists(pdf_file):
        recipe_documents += read_pdf(pdf_file) + "\n"
    else:
        print(f"Warning: {pdf_file} not found!")

if not recipe_documents.strip():
    recipe_documents = "No specific recipe examples available."

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        ingredients = request.form.get('ingredients')
        cuisine_type = request.form.get('cuisine_type')
        difficulty_level = request.form.get('difficulty_level')

        session['ingredients'] = ingredients
        session['cuisine_type'] = cuisine_type
        session['difficulty_level'] = difficulty_level

        return generate_recipe_and_redirect(ingredients, cuisine_type, difficulty_level)

    return render_template('form.html')

def generate_recipe_and_redirect(ingredients, cuisine_type, difficulty_level):
    user_prompt = (
        f"Invent a {difficulty_level.lower()} {cuisine_type.lower()} recipe "
        f"using these ingredients: {ingredients}. "
        "Provide:\n"
        "- A creative recipe name\n"
        "- List of ingredients with approximate quantities\n"
        "- Step-by-step cooking instructions\n"
        "- Preparation time if possible\n"
        "Return as clean plain text, no Markdown."
    )

    system_prompt = (
        "You are DishGenie, a magical chef assistant. "
        "Use creativity to invent delicious recipes, while referring to the example recipes below "
        "for inspiration and formatting.\n\n"
        f"Example Recipes:\n{recipe_documents}"
    )

    try:
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "openai/gpt-4o-mini",
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "top_p": 0.8,
            "temperature": 0.5
        }

        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        recipe = result['choices'][0]['message']['content']
        session['recipe'] = recipe
        session.pop('error', None)
        return redirect(url_for('result'))

    except Exception as e:
        session['error'] = str(e)
        return redirect(url_for('result'))

@app.route('/regenerate')
def regenerate():
    ingredients = session.get('ingredients')
    cuisine = session.get('cuisine_type')
    difficulty = session.get('difficulty_level')

    if ingredients and cuisine and difficulty:
        return generate_recipe_and_redirect(ingredients, cuisine, difficulty)
    else:
        return redirect(url_for('form'))

@app.route('/result')
def result():
    recipe = session.get('recipe')
    error = session.get('error')
    return render_template('result.html', recipe=recipe, error=error, background='ingredients_background.jpg')

if __name__ == '__main__':
    app.run(debug=True)
