document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('upload-form');
    const resultBox = document.getElementById('prediction-result');

    form.addEventListener('submit', async (event) => {
        event.preventDefault();

        const formData = new FormData(form);
        const patientId = formData.get('patient-id');

        try {
            const response = await fetch('/', {
                method: 'POST',
                body: formData
            });

            if (response.ok) {
                const result = await response.json();
                displayResult(result, patientId);
            } else {
                resultBox.innerHTML = `<p>Error: ${response.statusText}</p>`;
            }
        } catch (error) {
            resultBox.innerHTML = `<p>Error: ${error.message}</p>`;
        }
    });

    function displayResult(result, patientId) {
        const { filename, predicted_class } = result;
        resultBox.innerHTML = `
            <div style="display: flex; align-items: flex-start;">
                <img src="/static/uploads/${filename}" alt="Uploaded Image" class="result-image" style="width: 150px; height: 150px; margin-right: 10px;">
                <div class="details-container" >
                    <h3>Patient ID: ${patientId}</h3>
                    <h3>Predicted Class: ${predicted_class}</h3>
                </div>
            </div>
        `;
    }
});

document.addEventListener('DOMContentLoaded', function() {
    var menuButton = document.getElementById('menu-button');
    var sidebar = document.getElementById('sidebar');

    menuButton.addEventListener('click', function() {
        // Toggle the 'active' class on the sidebar
        sidebar.classList.toggle('active');
    });
});
