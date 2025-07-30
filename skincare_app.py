
# app.py - Streamlit Web Application
# Skincare Ingredient Safety Checker
# Run with: streamlit run app.py

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time

# Konfigurasi halaman
st.set_page_config(
    page_title="🧪 Skincare Safety Checker",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
body {
    margin-bottom: 2rem;
}

.main-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 2rem;
    border-radius: 15px;
    text-align: center;
    color: white;
}

.metric-card {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    padding: 1rem;
    border-radius: 10px;
    text-align: center;
    color: white;
    margin: 0.5rem 0;
}

.safe-card {
    background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    padding: 1rem;
    border-radius: 10px;
    border-left: 5px solid #28a745;
}

.danger-card {
    background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
    padding: 1rem;
    border-radius: 10px;
    border-left: 5px solid #dc3545;
}

.ingredient-item {
    background: #f8f9fa;
    padding: 1rem;
    border-radius: 8px;
    border-left: 4px solid #dc3545;
    margin: 0.5rem 0;
}

.stTextArea > div > div > textarea {
    font-size: 16px;
}

/* Update untuk Streamlit modern */
.appview-container .main .block-container {
    padding-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

class SkincareAnalyzer:
    def __init__(self):
        self.dangerous_ingredients = {
            'paraben': {
                'description': 'Dapat mengganggu hormon (EU Regulation No. 1223/2009)',
                'category': 'Endocrine Disruptor',
                'risk_level': 'High',
                'common_names': ['methylparaben', 'propylparaben', 'butylparaben']
            },
            'sulfate': {
                'description': 'Bersifat keras dan dapat mengiritasi kulit',
                'category': 'Irritant',
                'risk_level': 'Medium',
                'common_names': ['sodium lauryl sulfate', 'sls', 'sodium laureth sulfate']
            },
            'phthalate': {
                'description': 'May disrupt hormones and affect reproductive health (EU Regulation No. 1223/2009)',
                'category': 'Endocrine Disruptor',
                'risk_level': 'High',
                'common_names': ['dibutyl phthalate (dbp)', 'diethylhexyl phthalate (dehp)']
            },
            'formaldehyde': {
                'description': 'Known carcinogen and skin sensitizer',
                'category': 'Carcinogen, Allergen',
                'risk_level': 'High',
                'common_names': ['formalin', 'methylene glycol', 'quaternium-15']
            },
            'mercury': {
                'description': 'Neurotoxin, harmful to kidney and nervous system',
                'category': 'Heavy Metal, Neurotoxin',
                'risk_level': 'Critical',
                'common_names': ['calomel', 'mercuric chloride']
            },
            'hydroquinone': {
                'description': 'Skin lightener, can cause ochronosis (skin discoloration)',
                'category': 'Skin Irritant, Pigmentation Disrupter',
                'risk_level': 'High',
                'common_names': ['dihydroxybenzene', 'quinol']
            },
            'triclosan': {
                'description': 'May disrupt hormones and contribute to antibiotic resistance',
                'category': 'Endocrine Disruptor, Antibiotic Resistance',
                'risk_level': 'High',
                'common_names': ['triclosan', 'tcs']
            },
            'alcohol': {
                'description': 'Can be drying and irritating for some skin types (depending on type and concentration)',
                'category': 'Irritant, Drying Agent',
                'risk_level': 'Medium',
                'common_names': ['ethanol', 'isopropyl alcohol', 'sd alcohol']
            },
            'fragrance': {
                'description': 'Common allergen and can cause skin irritation (often a mix of undisclosed chemicals)',
                'category': 'Allergen, Irritant',
                'risk_level': 'Medium',
                'common_names': ['parfum', 'perfume', 'aroma']
            },
            'lead': {
                'description': 'Neurotoxin, harmful to nervous system (especially in children)',
                'category': 'Heavy Metal, Neurotoxin',
                'risk_level': 'Critical',
                'common_names': ['lead acetate']
            },
             'toluene': {
                'description': 'Can affect respiratory system and nervous system',
                'category': 'Toxin',
                'risk_level': 'High',
                'common_names': ['methylbenzene', 'toluol']
            },
            'bha': {
                'description': 'Possible endocrine disruptor and carcinogen',
                'category': 'Endocrine Disruptor, Possible Carcinogen',
                'risk_level': 'High',
                'common_names': ['butylated hydroxyanisole']
            },
            'bht': {
                'description': 'Possible endocrine disruptor and skin allergen',
                'category': 'Endocrine Disruptor, Allergen',
                'risk_level': 'Medium',
                'common_names': ['butylated hydroxytoluene']
            },
            'petrolatum': {
                'description': 'Can be contaminated with PAHs (polycyclic aromatic hydrocarbons) if not refined properly',
                'category': 'Contaminant Risk',
                'risk_level': 'Medium',
                'common_names': ['petroleum jelly', 'mineral oil jelly']
            },
             'phenoxyethanol': {
                'description': 'Preservative, can be an allergen and skin irritant (restricted in some countries)',
                'category': 'Preservative, Allergen, Irritant',
                'risk_level': 'Medium',
                'common_names': ['ethylene glycol phenyl ether']
            },
            'propylene glycol': {
                'description': 'Can be a skin irritant and allergen',
                'category': 'Irritant, Allergen',
                'risk_level': 'Medium',
                'common_names': ['1,2-propanediol']
            },
            'siloxane': {
                'description': 'Possible endocrine disruptors (especially cyclosiloxanes like cyclopentasiloxane and cyclohexasiloxane)',
                'category': 'Endocrine Disruptor',
                'risk_level': 'High',
                'common_names': ['cyclopentasiloxane', 'cyclohexasiloxane', 'dimethicone', 'cyclomethicone']
            },
             'oxybenzone': {
                'description': 'Sunscreen ingredient, can be a hormone disruptor and marine pollutant',
                'category': 'Endocrine Disruptor, Environmental Hazard',
                'risk_level': 'High',
                'common_names': ['benzophenone-3']
            },
            'benzoyl peroxide': {
                'description': 'Can be a skin irritant and sensitizer',
                'category': 'Irritant, Sensitizer',
                'risk_level': 'Medium',
                'common_names': ['benzyl peroxide']
            },
            'resorcinol': {
                'description': 'Possible endocrine disruptor and allergen',
                'category': 'Endocrine Disruptor, Allergen',
                'risk_level': 'High',
                'common_names': ['1,3-benzenediol']
            },
            'synthetic dyes': {
                'description': 'Some synthetic dyes (e.g., coal tar dyes) can be carcinogens or allergens',
                'category': 'Possible Carcinogen, Allergen',
                'risk_level': 'High',
                'common_names': ['ci 19140', 'yellow 5', 'red 40']
            }
        }

    def analyze_ingredients(self, ingredients_text):
        ingredients_text_lower = ingredients_text.lower()
        found_dangerous = []
        is_safe = True
        for ingredient, data in self.dangerous_ingredients.items():
            # Check for main ingredient name
            if ingredient in ingredients_text_lower:
                found_dangerous.append({'name': ingredient, 'description': data['description'], 'category': data['category'], 'risk_level': data['risk_level']})
                is_safe = False
                continue # No need to check common names if main name is found

            # Check for common names
            if 'common_names' in data:
                for common_name in data['common_names']:
                    if common_name in ingredients_text_lower:
                        found_dangerous.append({'name': common_name, 'description': data['description'], 'category': data['category'], 'risk_level': data['risk_level']})
                        is_safe = False
                        break # Move to the next main ingredient once a common name is found

        return is_safe, found_dangerous

# Instantiate the analyzer
analyzer = SkincareAnalyzer()

# Streamlit App Layout
st.markdown('<div class="main-header"><h1>🧪 Skincare Ingredient Safety Checker</h1></div>', unsafe_allow_html=True)

# Input Area
st.header("Enter Skincare Ingredients:")
ingredient_input = st.text_area("Paste the ingredient list here:", height=150, placeholder="e.g., Aqua, Glycerin, Alcohol, Fragrance, Sodium Laureth Sulfate")

# Analyze Button
if st.button("Analyze Ingredients", help="Click to check the safety of the ingredients"):
    if ingredient_input:
        st.subheader("Analysis Results:")
        with st.spinner("Analyzing..."):
            is_safe, dangerous_ingredients_found = analyzer.analyze_ingredients(ingredient_input)
            time.sleep(1) # Simulate processing time

        if is_safe:
            st.markdown('<div class="safe-card"><h2>✅ Safe Ingredients</h2><p>Based on the list provided, no commonly known dangerous ingredients were found.</p></div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="danger-card"><h2>❌ Potentially Dangerous Ingredients Found</h2><p>Please be aware of the following ingredients in your product:</p></div>', unsafe_allow_html=True)
            for ingredient_info in dangerous_ingredients_found:
                st.markdown(f"""
                <div class="ingredient-item">
                    <strong>{ingredient_info['name'].title()}</strong>
                    <p><strong>Risk Level:</strong> {ingredient_info['risk_level']}</p>
                    <p><strong>Category:</strong> {ingredient_info['category']}</p>
                    <p><strong>Description:</strong> {ingredient_info['description']}</p>
                </div>
                """, unsafe_allow_html=True)

    else:
        st.warning("Please enter some ingredients to analyze.")

# Optional: Add some metrics or charts (requires data processing)
# Example: Distribution of dangerous ingredients in a dataset (if you have one loaded)
# st.header("Dangerous Ingredient Distribution (Example)")
# if 'df' in locals(): # Check if DataFrame exists from previous cells
#     dangerous_counts = df[df['status'] == 'Berbahaya']['product_type'].value_counts().head(10)
#     fig = px.bar(dangerous_counts, x=dangerous_counts.index, y=dangerous_counts.values, title='Top 10 Product Types with Dangerous Ingredients')
#     st.plotly_chart(fig)
# else:
#     st.info("Load a dataset to see distribution charts.")

# Information Section
st.sidebar.header("About")
st.sidebar.info(
    "This tool checks skincare ingredient lists against a predefined list of potentially dangerous substances. "
    "**Please note:** This is a basic tool and not a substitute for professional advice. "
    "Ingredient safety can depend on concentration, context, and individual sensitivities."
)

st.sidebar.header("Dangerous Ingredients Checked")
dangerous_list = [f"- **{k.title()}**: {v['description']}" for k, v in analyzer.dangerous_ingredients.items()]
st.sidebar.markdown("
".join(dangerous_list))

