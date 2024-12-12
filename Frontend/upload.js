document.getElementById('uploadNewPdfButton').addEventListener('click', function() {
    document.getElementById('pdfInput').click();
});

document.getElementById('pdfInput').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
        const formData = new FormData();
        formData.append('pdf', file);

        fetch('/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
});