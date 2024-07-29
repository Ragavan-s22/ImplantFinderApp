document.addEventListener('DOMContentLoaded', () => {
    const predictButton = document.getElementById('find-btn');
    predictButton.addEventListener('click', () => {
        const fileInput = document.getElementById('xray-upload');
        const file = fileInput.files[0];

        if (file) {
            const formData = new FormData();
            formData.append('file', file);

            fetch('/upload', {
                method: 'POST',
                body: formData
            })
            .then(response => response.text())
            .then(result => {
                document.getElementById('result-box').innerHTML = `<h2>Result: ${result}</h2>`;
            })
            .catch(error => {
                console.error('Error:', error);
                document.getElementById('result-box').innerHTML = '<h2>Error processing the image</h2>';
            });
        } else {
            alert('Please select a file.');
        }
    });
});
