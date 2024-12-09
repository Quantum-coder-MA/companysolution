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
    const Produit = await fetchData('produits/');
    const secteurs = await fetchData('secteurs/');
    const representants = await fetchData('representatives/');
    const commercialisations = await fetchData('commercializations/');

    document.getElementById('total-produits').textContent = Produit.length;
    document.getElementById('total-secteurs').textContent = secteurs.length;
    document.getElementById('total-representants').textContent = representants.length;
    document.getElementById('total-commercialisations').textContent = commercialisations.length;
}
// client_interface.js
async function populateAttachmentsTable() {
    const attachments = await fetchData('attachments/');

    const attachmentsListElement = document.getElementById('attachments-list');
    attachmentsListElement.innerHTML = '';

    attachments.forEach(attachment => {
        const row = `
            <tr>
                <td>${attachment.representative_name} ${attachment.representative_prenom}</td>
                <td>${attachment.sector_name}</td>
                <td>${attachment.product_name}</td>
                <td>${attachment.commercialization_confirmed ? 'Confirmed' : 'Not Confirmed'}</td>
                <td>${attachment.confirmed ? 'Confirmed' : 'Not Confirmed'}</td>
            </tr>
        `;
        attachmentsListElement.innerHTML += row;
    });
}
// Populate Recent Products Table
async function populateProduitTable() {
    const Produit = await fetchData('produits/');
    const ProduitListElement = document.getElementById('produits-list');
    ProduitListElement.innerHTML = ''; // Clear existing entries

    Produit.slice(0, 5).forEach(produit => {
        const row = `
            <tr>
                <td>${produit.nom}</td>
                <td>${produit.price} €</td>
                <td>${produit.label}</td>
            </tr>
        `;
        ProduitListElement.innerHTML += row;
    });
}

// Populate Representatives by Sector Table
async function populateRepresentantsTable() {
    const gestions = await fetchData('gestions/');
    const representantsListElement = document.getElementById('representants-list');
    representantsListElement.innerHTML = ''; // Clear existing entries

    const representantsMap = new Map();

    for (const gestion of gestions) {
        const representantResponse = await fetchData(`representatives/${gestion.representative}/`);
        const secteurResponse = await fetchData(`secteurs/${gestion.secteur}/`);
        const produitResponse = await fetchData(`produits/${gestion.produit}/`);

        const entry = `
            <tr>
                <td>${representantResponse.nom} ${representantResponse.prenom}</td>
                <td>${secteurResponse.nom}</td>
                <td>${produitResponse.nom}</td>
            </tr>
        `;
        representantsListElement.innerHTML += entry;
    }
}

// Initialize Dashboard
async function initializeDashboard() {
    await updateDashboardStats();
    await populateProduitsTable();
    await populateRepresentantsTable();
    await populateAttachmentsTable();
}

// Run initialization when DOM is fully loaded
document.addEventListener('DOMContentLoaded', initializeDashboard);
