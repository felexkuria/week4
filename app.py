from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

EXCEL_FILE = 'product-catalog.xlsx'

@app.route('/')
def index():
    # Read the Introduction worksheet for instructions
    intro_df = pd.read_excel(EXCEL_FILE, sheet_name='Introduction', engine='openpyxl')
    instructions = intro_df.to_html(index=False)
    
    # Read the Brands worksheet
    brands_df = pd.read_excel(EXCEL_FILE, sheet_name='Brands', engine='openpyxl')
    brands = brands_df['CODE - BRAND_SYSTEM_NAME'].tolist()
    
    return render_template('index.html', instructions=instructions, brands=brands)

@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    name = request.form['name']
    description = request.form['description']
    brand = request.form['brand']
    
    # Create a new row of data
    new_data = {
        'Name': [name],
        'Description': [description],
        'Brand': [brand],
        # Add other fields as needed
    }
    new_df = pd.DataFrame(new_data)
    
    # Append to the Upload Template worksheet
    with pd.ExcelWriter(EXCEL_FILE, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
        new_df.to_excel(writer, sheet_name='Upload Template', index=False, header=False, startrow=writer.sheets['Upload Template'].max_row)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)