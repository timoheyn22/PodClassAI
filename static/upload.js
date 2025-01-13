document.getElementById('uploadNewPdfButton').addEventListener('click', function() {
    document.getElementById('pdfInput').click();
});

document.getElementById('pdfInput').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file && file.type === 'application/pdf') {
        // Update the button text with the PDF file name
        document.getElementById('uploadNewPdfButton').textContent = file.name;

        // Display the PDF in the pdfContainer
        const fileReader = new FileReader();
        fileReader.onload = function() {
            const pdfData = fileReader.result;
            const pdfContainer = document.getElementById('pdfContainer');
            pdfContainer.innerHTML = `<embed src="${pdfData}" type="application/pdf" width="100%" height="100%">`;
        };
        fileReader.readAsDataURL(file);

        // Upload the PDF file to the server
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
    } else {
        alert('Please upload a valid PDF file.');
    }
});

document.getElementById('pdfUpload').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file && file.type === 'application/pdf') {
        const fileReader = new FileReader();
        fileReader.onload = function() {
            const pdfData = fileReader.result;
            const pdfContainer = document.getElementById('pdfContainer');
            pdfContainer.innerHTML = `<embed src="${pdfData}" type="application/pdf" width="100%" height="100%">`;
        };
        fileReader.readAsDataURL(file);
    } else {
        alert('Please upload a valid PDF file.');
    }
});

document.getElementById('selectLanguageButton').addEventListener('click', function() {
    document.getElementById('languageDropdown').style.display = 'block';
});

document.querySelectorAll('#languageDropdown a').forEach(function(item) {
    item.addEventListener('click', function(event) {
        event.preventDefault();
        const selectedLanguage = event.target.getAttribute('data-lang');
        document.getElementById('selectLanguageButton').textContent = selectedLanguage;
        document.getElementById('languageDropdown').style.display = 'none';
    });
});

document.getElementById('selectLanguageButton').addEventListener('click', function() {
    document.getElementById('languageDropdown').style.display = 'block';
});

document.querySelectorAll('#languageDropdown a').forEach(function(item) {
    item.addEventListener('click', function(event) {
        event.preventDefault();
        const selectedLanguage = event.target.getAttribute('data-lang');
        document.getElementById('selectLanguageButton').textContent = selectedLanguage;
        document.getElementById('languageDropdown').style.display = 'none';
    });
});

document.addEventListener('click', function(event) {
    if (!event.target.matches('#selectLanguageButton')) {
        document.getElementById('languageDropdown').style.display = 'none';
    }
}   );

document.getElementById('backToHomeButton').addEventListener('click', function() {
    window.location.href = '/';
});

document.getElementById('selectSpeedButton').addEventListener('click', function() {
    document.getElementById('speedDropdown').style.display = 'block';
});

document.querySelectorAll('#speedDropdown a').forEach(function(item) {
    item.addEventListener('click', function(event) {
        event.preventDefault();
        const selectedSpeed = event.target.getAttribute('data-speed');
        document.getElementById('selectSpeedButton').textContent = selectedSpeed;
        document.getElementById('speedDropdown').style.display = 'none';
    });
});

document.addEventListener('click', function(event) {
    if (!event.target.matches('#selectSpeedButton')) {
        document.getElementById('speedDropdown').style.display = 'none';
    }
});

    document.getElementById('backToHomeButton').addEventListener('click', function() {
        window.location.href = "home.html"; // Replace 'upload.html' with your actual upload page URL
    });

    document.getElementById('createPodcastButton').addEventListener('click', function() {
    fetch('/create_podcast', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            alert(data.message);
        } else if (data.error) {
            alert('Error: ' + data.error);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});


