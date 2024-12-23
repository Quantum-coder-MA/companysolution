import streamlit as st
import requests
import pandas as pd

# Base URL for Django API
BASE_URL = "http://127.0.0.1:8000/api/"

def fetch_data(endpoint):
    """Fetch data from a specific API endpoint"""
    try:
        response = requests.get(BASE_URL + endpoint)
        return response.json()
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return []

def validate_commercialization(produit_id, secteur_id):
    """Check if a product is commercialized in a specific sector"""
    try:
        response = requests.get(f"{BASE_URL}commercializations/?produit={produit_id}&secteur={secteur_id}")
        return len(response.json()) > 0
    except Exception as e:
        st.error(f"Error checking commercialization: {e}")
        return False

def list_products():
    """Display a list of products"""
    st.header("Product List")
    products = fetch_data("produits/")
    
    if products:
        df = pd.DataFrame(products)
        st.dataframe(df[['nom', 'label', 'price']])
    else:
        st.write("No products found.")

def list_sectors():
    """Display a list of sectors"""
    st.header("Sector List")
    sectors = fetch_data("secteurs/")
    
    if sectors:
        df = pd.DataFrame(sectors)
        st.dataframe(df[['nom', 'ville', 'region']])
    else:
        st.write("No sectors found.")

def list_representatives():
    """Display a list of representatives"""
    st.header("Representatives List")
    representatives = fetch_data("representatives/")
    
    if representatives:
        df = pd.DataFrame(representatives)
        st.dataframe(df[['nom', 'prenom', 'email', 'telephone']])
    else:
        st.write("No representatives found.")

def add_product():
    """Add a new product"""
    st.header("Add New Product")
    with st.form("add_product_form"):
        name = st.text_input("Product Name")
        label = st.number_input("Label", step=1)
        price = st.number_input("Price", step=0.01)
        
        submit = st.form_submit_button("Add Product")
        if submit:
            payload = {"nom": name, "label": label, "price": price}
            try:
                response = requests.post(BASE_URL + "produits/", json=payload)
                if response.status_code in [200, 201]:
                    st.success("Product added successfully!")
                else:
                    st.error(f"Error adding product: {response.text}")
            except Exception as e:
                st.error(f"Error: {e}")

def add_sector():
    """Add a new sector"""
    st.header("Add New Sector")
    with st.form("add_sector_form"):
        name = st.text_input("Sector Name")
        city = st.text_input("City")
        region = st.text_input("Region")
        
        submit = st.form_submit_button("Add Sector")
        if submit:
            payload = {"nom": name, "ville": city, "region": region}
            try:
                response = requests.post(BASE_URL + "secteurs/", json=payload)
                if response.status_code in [200, 201]:
                    st.success("Sector added successfully!")
                else:
                    st.error(f"Error adding sector: {response.text}")
            except Exception as e:
                st.error(f"Error: {e}")

def assign_representative():
    """Assign a representative to a product in a specific sector"""
    st.header("Assign Representative")
    
    # Fetch data for dropdowns
    products = fetch_data("produits/")
    sectors = fetch_data("secteurs/")
    representatives = fetch_data("representatives/")
    
    with st.form("assign_rep_form"):
        # Dropdown selections
        product = st.selectbox("Select Product", 
            [p['nom'] for p in products], key='product_select')
        sector = st.selectbox("Select Sector", 
            [s['nom'] for s in sectors], key='sector_select')
        representative = st.selectbox("Select Representative", 
            [f"{r['nom']} {r['prenom']}" for r in representatives], key='rep_select')
        
        label = st.number_input("Label", step=1)
        price = st.number_input("Price", step=0.01)
        
        submit = st.form_submit_button("Assign Representative")
        if submit:
            # Get IDs for selected items
            product_id = next(p['id'] for p in products if p['nom'] == product)
            sector_id = next(s['id'] for s in sectors if s['nom'] == sector)
            rep_name, rep_surname = representative.split(' ')
            representative_id = next(r['id'] for r in representatives 
                                     if r['nom'] == rep_name and r['prenom'] == rep_surname)
            
            # Validate commercialization
            if validate_commercialization(product_id, sector_id):
                payload = {
                    "produit": product_id, 
                    "secteur": sector_id,
                    "representative": representative_id,
                    "label": label,
                    "price": price
                }
                
                try:
                    response = requests.post(BASE_URL + "gestions/", json=payload)
                    if response.status_code in [200, 201]:
                        st.success("Representative assigned successfully!")
                    else:
                        st.error(f"Error assigning representative: {response.text}")
                except Exception as e:
                    st.error(f"Error: {e}")
            else:
                st.warning("Product is not commercialized in this sector!")


def list_assignement():
    """Display a list of products"""
    st.header("assignement")
    products = fetch_data("produits/")
    sectors = fetch_data("secteurs/")
    representatives = fetch_data("representatives/")   
    if products:
        df = pd.DataFrame(products)
        st.dataframe(df[['nom', 'label', 'price']])
    else:
        st.write("No products found.") 
    if sectors:
        ef = pd.DataFrame(sectors)
        st.dataframe(ef[['nom','ville','region']])
    else:
        st.write("No products found.")         
    if representatives:
        ik = pd.DataFrame(representatives)
        st.dataframe(ik[['nom','prenom']])
    else:
        st.write("No representatives found.")          








def list_attachement():
    """Display a list of sectors"""
    
    
    
    
    st.header("attachement List")
    attachement = fetch_data("attachement/")
    
    if attachement:
        df = pd.DataFrame(attachement)
        st.dataframe(df[['nom', 'ville', 'region', 'produit' 'price','secteur', 'representative'  ]])
    else:
        st.write("No sectors found.")



def view_product_management():
    """View product management details"""
    """View product management details"""
    st.header("Product Management Details")
    
    # Fetch data from the API
    gestions = fetch_data("gestions/")

    if gestions:
        # If the data exists, process it
        try:
            # Create a detailed dataframe
            cleaned_data = []
            for gestion in gestions:
                # Assuming 'produit' and 'contact' are already dictionaries
                produit_info = gestion.get("produit", {})
                representative_info = gestion.get("representative", {})
                secteur_info = gestion.get("secteur", {})             
                # Build a cleaned-up product dictionary
            

                # Build a cleaned-up product dictionary
                product_info = {
                    "Product ID": produit_info.get("id", "N/A"),
                    "Product Name": produit_info.get("nom", "N/A"),
                    "Product Label": produit_info.get("label", "N/A"),
                    "Product Price": produit_info.get("price", "N/A"),
                    "Region": secteur_info.get("region", "N/A"),
                    "City": secteur_info.get("ville", "N/A"),
                    "Address": representative_info.get("adress", "N/A"),
                    "Email": representative_info.get("email", "N/A"),
                    "Contact Name": representative_info.get("nom", "N/A"),
                    "Contact Phone": representative_info.get("telephone", "N/A"),
                }
                cleaned_data.append(product_info)

            # Convert cleaned data into a DataFrame
            df = pd.DataFrame(cleaned_data)

            # Display the dataframe in Streamlit
            st.dataframe(df)

        except Exception as e:
            st.error(f"Error processing data: {e}")
    else:
        st.write("No product management records found.")

def main():
    """Main Streamlit application"""
    st.title("Product Management System")
    
    # Sidebar navigation
    menu = [
        "List Products", 


        "List Sectors", 
        "List Representatives", 
        "Add Product", 
        "Add Sector", 
        "View Product Management"
    ]
    choice = st.sidebar.selectbox("Navigation", menu)
    
    # Routing based on menu selection
    if choice == "List Products":
        list_products()        
        

    elif choice == "List Sectors":
        list_sectors()
    elif choice == "List Representatives":
        list_representatives()
    elif choice == "Add Product":
        add_product()
    elif choice == "Add Sector":
        add_sector()

    elif choice == "View Product Management":
        view_product_management()

if __name__ == "__main__":
    main()
    
    
    
    
