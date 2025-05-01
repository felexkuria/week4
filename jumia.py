# Using pandas to read Excel file
import pandas as pd

# Add error handling for missing openpyxl dependency
try:
    # Sample data to write to Excel
    data = {
        'Sid': [''] * 9,       
        'Name': ['QUALITY MODERN CHARCOAL STOVE', 'Stainless Steel Flask Vaccum Coffee Pot-2L', 'Stainless Steel Flask Vaccum Coffee Pot-2L', 'Stainless Steel Flask Vaccum Coffee Pot-2L', 'Stainless Steel Flask Vaccum Coffee Pot-2L', 'Stainless Steel Flask Vaccum Coffee Pot-2L', 'Chest Freezer', '5 Layer Square Vegetable Fruits Rotating Rack With Wheels', '6l Single Deep Fryer'],
        'Name_AR': [''] * 9,
        'Name_FR': [''] * 9,
        'Description': [''] * 9,
        'Description_AR': [''] * 9, 
        'Description_FR': [''] * 9,
        'SellerSKU': [''] * 9,
        'ParentSKU': [''] * 9,
        'Brand': [''] * 9,
        'PrimaryCategory': [''] * 9,
        'AdditionalCategory': [''] * 9,
        'GTIN_Barcode': [''] * 9,
        'variation': [''] * 9,
        'ac_design': [''] * 9,
        'air_cooler_type': [''] * 9,
        'blender_type': [''] * 9,
        'capacity': [''] * 9,
        'capacity_kg': [''] * 9,
        'capacity_kva': [''] * 9,
        'capacity_liter': [''] * 9,
        'capacity_litres': [''] * 9,
        'capacity_slices': [''] * 9,
        'certifications': [''] * 9,
        'color': [''] * 9,
        'color_AR': [''] * 9,
        'color_FR': [''] * 9,
        'color_family': [''] * 9,
        'cooker_type': [''] * 9,
        'defrost_type': [''] * 9,
        'fan_type': [''] * 9,
        'freezer_type': [''] * 9,
        'fridge_type': [''] * 9,
        'horse_power': [''] * 9,
        'installation_type': [''] * 9,
        'juicer_type': [''] * 9,
        'main_material': [''] * 9,
        'manufacturer_txt': [''] * 9,
        'material_family': [''] * 9,
        'model': [''] * 9,
        'note': [''] * 9,
        'package_content': [''] * 9,
        'package_content_AR': [''] * 9,
        'package_content_FR': [''] * 9,
        'power': [''] * 9,
        'product_line': [''] * 9,
        'product_measures': [''] * 9,
        'product_warranty': [''] * 9,
        'product_weight': [''] * 9,
        'production_country': [''] * 9,
        'short_description': [''] * 9,
        'short_description_AR': [''] * 9,
        'short_description_FR': [''] * 9,
        'storage_features': [''] * 9,
        'stove_type': [''] * 9,
        'venting_type': [''] * 9,
        'warranty_address': [''] * 9,
        'warranty_duration': [''] * 9,
        'warranty_type': [''] * 9,
        'washer_capacity': [''] * 9,
        'washing_machine_type': [''] * 9,
        'wattage': [''] * 9,
        'youtube_id': [''] * 9,
        'MainImage': [''] * 9,
        'Image2': [''] * 9,
        'Image3': [''] * 9,
        'Image4': [''] * 9,
        'Image5': [''] * 9,
        'Image6': [''] * 9,
        'Image7': [''] * 9,
        'Image8': [''] * 9
    }    
    
    # Generate descriptions dynamically based on product names
    descriptions = [
        f"<p>Planning a Tea party?- &nbsp;{name} will keep your guests well supplied with Hot Tea or Coffee</p>"
        f"<p>Fashion Healthy Bottle's 2 Litre Capacity is enough to minimize the need for frequent refills. It holds enough, for your vacationing family</p>"
        f"<p>It is made of quality material both in the &nbsp;inside and outside: Glass Inside and Stainless Steel Outside.</p>"
        f"<p>It is also very easy to clean and does not break in the event it falls off.</p>"
        f"<p>Order yours online on Jumia Kenya and have it delivered either at your place of residence or work place.</p>"
        for name in data['Name']
    ]
    data['Description'] = descriptions
    
    # Create DataFrame from sample data
    df = pd.DataFrame(data)
    
    # Write DataFrame to Excel file on specific sheet
    with pd.ExcelWriter('product-catalog.xlsx', engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name='Upload Template', index=False)
        
    # Read back and display the data to verify
    df_verify = pd.read_excel("product-catalog.xlsx", sheet_name='Upload Template', engine='openpyxl')
    print("Data written successfully:")
    print(df_verify)

except ImportError:
    print("Please install openpyxl first: pip install openpyxl")
