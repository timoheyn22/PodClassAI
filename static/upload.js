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







document.getElementById('backToHomeButton').addEventListener('click', function() {
    window.location.href = '/';
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


    // Funktion zum Umschalten der Sichtbarkeit der Dropdown-Inhalte
function toggleDropdown(dropdownId) {
    document.getElementById(dropdownId).classList.toggle('show');
}

// Event-Listener für die Buttons
document.getElementById('selectLanguageButton').addEventListener('click', function() {
    toggleDropdown('languageDropdown');
});

document.getElementById('selectSpeedButton').addEventListener('click', function() {
    toggleDropdown('speedDropdown');
});

// Schließe das Dropdown, wenn der Benutzer außerhalb davon klickt
window.onclick = function(event) {
    if (!event.target.matches('#selectLanguageButton') && !event.target.matches('#selectSpeedButton')) {
        var dropdowns = document.getElementsByClassName('dropdown-content');
        for (var i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}

