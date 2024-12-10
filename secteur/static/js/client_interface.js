// API Configuration
const BASE_URL = 'http://127.0.0.1:8000/api/';

// Utility function for fetching data
async function fetchData(endpoint) {
    try {
        const response = await fetch(`${BASE_URL}${endpoint}`);
        return await response.json();
    } catch (error) {
        console.error(`Error fetching ${endpoint}:`, error);
        return [];
    }
}

// Update Dashboard Statistics
async function updateDashboardStats() {
    const produits = await fetchData('produits/');
    const secteurs = await fetchData('secteurs/');
    const representants = await fetchData('representatives/');
    const commercialisations = await fetchData('commercializations/');

    document.getElementById('total-produits').textContent = produits.length;
    document.getElementById('total-secteurs').textContent = secteurs.length;
    document.getElementById('total-representants').textContent = representants.length;
    document.getElementById('total-commercialisations').textContent = commercialisations.length;
}

// Client Interface for Attachments Table
async function populateGestionsTable() {
    // Fetch the gestions data
    const gestions = await fetchData('gestions/');
    const gestionsListElement = document.getElementById('gestions-list');
    gestionsListElement.innerHTML = ''; // Clear existing entries

    gestions.forEach(gestion => {
        // Assuming 'gestion' contains nested fields like 'representative', 'secteur', and 'produit'
        const representative = gestion.representative;
        const secteur = gestion.secteur;
        const produit = gestion.produit;

        const row = `
            <tr>
                <td>${representative.nom} ${representative.prenom}</td>
                <td>${secteur.ville}</td>
                <td>${produit.nom}</td>
                <td>${gestion.label ? 'Confirmed' : 'Not Confirmed'}</td>
                <td>${gestion.price}</td>
            </tr>
        `;
        gestionsListElement.innerHTML += row;
    });
}


// Populate Recent Products Table
async function populateProduitsTable() {
    const produits = await fetchData('produits/');
    const produitsListElement = document.getElementById('produits-list');
    produitsListElement.innerHTML = ''; // Clear existing entries

    produits.slice(0, 5).forEach(produit => {
        const row = `
            <tr>
                <td>${produit.nom}</td>
                <td>${produit.price} MAD</td>
                <td>${produit.label}</td>
            </tr>
        `;
        produitsListElement.innerHTML += row;
    });
}

// Populate Representatives by Sector Table
async function populateRepresentantsTable() {
    // Assuming 'gestions' is an array of objects
    const gestions = await fetchData('gestions/');
    const representantsListElement = document.getElementById('representants-list');
    representantsListElement.innerHTML = ''; // Clear existing entries

    // Iterate over each gestion object
    for (const gestion of gestions) {
        // Extract representative, secteur, and produit data directly from the gestion object
        const representant = gestion.representative;
        const secteur = gestion.secteur;
        const produit = gestion.produit;

        // Build the table row entry
        const entry = `
            <tr>
                <td>${representant.nom} ${representant.prenom}</td>
                <td>${secteur.nom}</td>
                <td>${produit.nom}</td>
            </tr>
        `;
        
        // Append the entry to the table
        representantsListElement.innerHTML += entry;
    }
}


// Populate Commercialization Status Table
async function populateCommercializationTable() {
    const commercializations = await fetchData('commercializations/');
    const commercializationListElement = document.getElementById('commercializations-list');
    commercializationListElement.innerHTML = ''; // Clear existing entries

    commercializations.forEach(commercialization => {
        const row = `
            <tr>
                <td>${commercialization.product_name}</td>
                <td>${commercialization.sector_name}</td>
                <td>${commercialization.representative_name}</td>
                <td>${commercialization.confirmed ? 'Confirmed' : 'Not Confirmed'}</td>
            </tr>
        `;
        commercializationListElement.innerHTML += row;
    });
}

// Initialize Dashboard
async function initializeDashboard() {
    await updateDashboardStats();
    await populateProduitsTable();
    await populateRepresentantsTable();
    await populateGestionsTable();
    await populateCommercializationTable(); // Add this new function
}

// Run initialization when DOM is fully loaded
document.addEventListener('DOMContentLoaded', initializeDashboard);
