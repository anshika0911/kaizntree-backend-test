// Fetch item data from Django backend
fetch('/api/get_items/')
    .then(response => response.json())
    .then(data => {
        const tableBody = document.getElementById('table-body');

        data.forEach(item => {
            const row = document.createElement('tr');
            const stockRatio = item.available_stock / item.in_stock;
            const indicatorCell = document.createElement('td');
            indicatorCell.classList.add('stock-indicator');

            // Add appropriate stock indicator class to the indicator cell
            if (stockRatio < 0.25) {
                indicatorCell.classList.add('out-of-stock');
            } else if (stockRatio < 0.5) {
                indicatorCell.classList.add('low-stock');
            }

            row.innerHTML = `
                <td><input type="checkbox" class="checkbox"></td>
                <td>${item.sku}</td>
                <td><a href="">${item.name}</a></td>
                <td>${item.in_stock}</td>
                <td>${item.available_stock}</td>
                <td>${item.category_id}</td>
            `;

            // Append the indicator cell to the row
            row.appendChild(indicatorCell);
            tableBody.appendChild(row);
        });
    })
    .catch(error => console.error('Error fetching data:', error));

function redirectToCategoryPage() {
    window.location.href = 'http://localhost:8000/api/categories/';
}

function redirectToItemPage() {
    window.location.href = 'http://localhost:8000/api/items/';
}
