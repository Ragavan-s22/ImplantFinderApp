document.addEventListener('DOMContentLoaded', () => {
    const fileInput = document.getElementById('xray-upload');
    const resultBox = document.getElementById('result-box');
    const predictButton = document.getElementById('find-btn');
    let imgPreview = document.createElement('img');
    imgPreview.id = 'img-preview';
    imgPreview.style.display = 'none';
    resultBox.appendChild(imgPreview);

    fileInput.addEventListener('change', (event) => {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                imgPreview.src = e.target.result;
                imgPreview.style.display = 'block';
            }
            reader.readAsDataURL(file);
        } else {
            imgPreview.style.display = 'none';
        }
    });

    predictButton.addEventListener('click', () => {
        const file = fileInput.files[0];
        const patientId = document.getElementById('patient-id').value;
        if (file) {
            const formData = new FormData();
            formData.append('file', file);

            fetch('/upload', {
                method: 'POST',
                body: formData
            })
            .then(response => response.text())
            .then(result => {
                const resultHTML = `
                    <h3>Patient ID: ${patientId}</h3>
                    <h3>Implant Type: ${result}</h3>
                `;
                resultBox.innerHTML = `<h2>Result</h2>${resultHTML}`;
                resultBox.appendChild(imgPreview);
            })
            .catch(error => {
                console.error('Error:', error);
                resultBox.innerHTML = `<h2>Result</h2><h3>Error processing the image</h3>`;
                resultBox.appendChild(imgPreview);
            });
        } else {
            alert('Please select a file.');
        }
    });
});

