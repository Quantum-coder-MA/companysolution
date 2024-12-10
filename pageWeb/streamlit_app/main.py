import streamlit as st
import requests

# Configuration
API_BASE_URL = 'http://localhost:8000/api/'  # Adjust to your Django backend URL

def fetch_data(endpoint):
    """Fetch data from the API endpoint"""
    try:
        response = requests.get(f"{API_BASE_URL}{endpoint}")
        return response.json()
    except requests.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return []

def create_data(endpoint, data):
    """Create data via API"""
    try:
        response = requests.post(f"{API_BASE_URL}{endpoint}", json=data)
        if response.status_code == 201:
            st.success("Data created successfully!")
            return response.json()
        else:
            st.error(f"Error creating data: {response.json().get('error', 'Unknown error')}")
            return None
    except requests.RequestException as e:
        st.error(f"Error sending data: {e}")
        return None

def main():
    st.title("Product-Representative Management System")

    # Tabs for different management sections
    tab1, tab2, tab3, tab4 = st.tabs([
        "Geographic Sectors", 
        "Products", 
        "Representatives", 
        "Product-Representative Assignment"
    ])

    with tab1:
        st.header("Geographic Sectors")
        with st.form("sector_form"):
            sector_name = st.text_input("Sector Name")
            sector_code = st.text_input("Sector Code")
            submit_sector = st.form_submit_button("Add Sector")
            
            if submit_sector:
                sector_data = {
                    "name": sector_name,
                    "code": sector_code
                }
                create_data("sectors/", sector_data)
        
        # Display existing sectors
        sectors = fetch_data("sectors/")
        if sectors:
            st.subheader("Existing Sectors")
            for sector in sectors:
                st.write(f"Name: {sector['name']}, Code: {sector['code']}")

    with tab2:
        st.header("Products")
        with st.form("product_form"):
            product_name = st.text_input("Product Name")
            product_description = st.text_area("Product Description")
            
            # Fetch sectors for multi-select
            sectors = fetch_data("sectors/")
            sector_options = {sector['id']: sector['name'] for sector in sectors}
            selected_sectors = st.multiselect("Select Sectors", options=list(sector_options.keys()), format_func=lambda x: sector_options.get(x, ''))
            
            submit_product = st.form_submit_button("Add Product")
            
            if submit_product:
                product_data = {
                    "name": product_name,
                    "description": product_description
                }
                product_response = create_data("products/", product_data)
                
                # Associate sectors with the product
                if product_response and selected_sectors:
                    for sector_id in selected_sectors:
                        sector_assoc_data = {
                            "product": product_response['id'],
                            "sector": sector_id
                        }
                        # You might need to implement a separate endpoint for this in your Django backend

        # Display existing products
        products = fetch_data("products/")
        if products:
            st.subheader("Existing Products")
            for product in products:
                st.write(f"Name: {product['name']}, Sectors: {', '.join([sector['name'] for sector in product.get('sectors', [])])}")

    with tab3:
        st.header("Representatives")
        with st.form("representative_form"):
            rep_name = st.text_input("Representative Name")
            rep_email = st.text_input("Email")
            rep_phone = st.text_input("Phone (Optional)")
            
            # Fetch sectors for multi-select
            sectors = fetch_data("sectors/")
            sector_options = {sector['id']: sector['name'] for sector in sectors}
            selected_sectors = st.multiselect("Managed Sectors", options=list(sector_options.keys()), format_func=lambda x: sector_options.get(x, ''))
            
            submit_rep = st.form_submit_button("Add Representative")
            
            if submit_rep:
                rep_data = {
                    "name": rep_name,
                    "email": rep_email,
                    "phone": rep_phone
                }
                rep_response = create_data("representatives/", rep_data)
                
                # Associate sectors with the representative
                if rep_response and selected_sectors:
                    for sector_id in selected_sectors:
                        sector_assoc_data = {
                            "representative": rep_response['id'],
                            "sector": sector_id
                        }
                        # You might need to implement a separate endpoint for this in your Django backend

        # Display existing representatives
        representatives = fetch_data("representatives/")
        if representatives:
            st.subheader("Existing Representatives")
            for rep in representatives:
                st.write(f"Name: {rep['name']}, Email: {rep['email']}, Sectors: {', '.join([sector['name'] for sector in rep.get('sectors', [])])}")

    with tab4:
        st.header("Product-Representative Assignment")
        with st.form("assignment_form"):
            # Fetch products, representatives, and sectors
            products = fetch_data("products/")
            representatives = fetch_data("representatives/")
            sectors = fetch_data("sectors/")

            # Create dropdown options
            product_options = {p['id']: p['name'] for p in products}
            rep_options = {r['id']: r['name'] for r in representatives}
            sector_options = {s['id']: f"{s['name']} ({s['code']})" for s in sectors}

            # Dropdowns for selection
            selected_product = st.selectbox("Select Product", options=list(product_options.keys()), format_func=lambda x: product_options.get(x, ''))
            selected_rep = st.selectbox("Select Representative", options=list(rep_options.keys()), format_func=lambda x: rep_options.get(x, ''))
            selected_sector = st.selectbox("Select Sector", options=list(sector_options.keys()), format_func=lambda x: sector_options.get(x, ''))

            submit_assignment = st.form_submit_button("Assign")

            if submit_assignment:
                assignment_data = {
                    "product": selected_product,
                    "representative": selected_rep,
                    "sector": selected_sector
                }
                create_data("product-rep-sectors/", assignment_data)

        # Display existing assignments
        assignments = fetch_data("product-rep-sectors/")
        if assignments:
            st.subheader("Existing Assignments")
            for assignment in assignments:
                st.write(f"Product: {assignment['product_name']}, "
                         f"Representative: {assignment['representative_name']}, "
                         f"Sector: {assignment['sector_name']}")

if __name__ == "__main__":
    main()