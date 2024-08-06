document.getElementById('upload-form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const formData = new FormData();
    const fileInput = document.getElementById('xray-upload');
    formData.append('file', fileInput.files[0]);

    const response = await fetch('/', {
        method: 'POST',
        body: formData
    });

    const result = await response.json();
    document.getElementById('prediction-result').textContent = `The image is predicted to be: ${result.prediction}`;
});
