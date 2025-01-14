document.addEventListener('DOMContentLoaded', function () {
    // Funktion für das Dropdown-Umschalten
    function toggleDropdown(dropdownId) {
        document.getElementById(dropdownId).classList.toggle('show');
    }

    // Event-Listener für Sprache-Dropdown
    const selectLanguageButton = document.getElementById('selectLanguageButton');
    const selectSpeedButton = document.getElementById('selectSpeedButton');

    if (selectLanguageButton) {
        selectLanguageButton.addEventListener('click', function () {
            toggleDropdown('languageDropdown');
        });
    }

    if (selectSpeedButton) {
        selectSpeedButton.addEventListener('click', function () {
            toggleDropdown('speedDropdown');
        });
    }

    // Schließen der Dropdowns, wenn außerhalb geklickt wird
    window.addEventListener('click', function (event) {
        if (
            !event.target.matches('#selectLanguageButton') &&
            !event.target.matches('#selectSpeedButton')
        ) {
            const dropdowns = document.getElementsByClassName('dropdown-content');
            for (let i = 0; i < dropdowns.length; i++) {
                const openDropdown = dropdowns[i];
                if (openDropdown.classList.contains('show')) {
                    openDropdown.classList.remove('show');
                }
            }
        }
    });

    // PDF-Upload-Button-Funktionalität
    const uploadNewPdfButton = document.getElementById('uploadNewPdfButton');
    const pdfInput = document.getElementById('pdfInput');

    if (uploadNewPdfButton && pdfInput) {
        uploadNewPdfButton.addEventListener('click', function () {
            pdfInput.click();
        });

        pdfInput.addEventListener('change', function (event) {
            const file = event.target.files[0];
            if (file) {
                const formData = new FormData();
                formData.append('pdf', file);

                fetch('/upload', {
                    method: 'POST',
                    body: formData,
                })
                    .then((response) => response.json())
                    .then((data) => {
                        console.log('Success:', data);
                    })
                    .catch((error) => {
                        console.error('Error:', error);
                    });
            }
        });
    }

    // PDF-Upload und Vorschau
    const pdfContainer = document.getElementById('pdfContainer');
    const pdfUpload = document.getElementById('pdfInput'); // Überprüfen, ob pdfInput oder pdfUpload korrekt ist

    if (pdfContainer && pdfUpload) {
        pdfUpload.addEventListener('change', function (event) {
            const file = event.target.files[0];
            if (file && file.type === 'application/pdf') {
                const fileReader = new FileReader();
                fileReader.onload = function () {
                    const pdfData = fileReader.result;
                    pdfContainer.innerHTML = `<embed src="${pdfData}" type="application/pdf" width="100%" height="100%">`;
                };
                fileReader.readAsDataURL(file);
            } else {
                alert('Please upload a valid PDF file.');
            }
        });
    }

    // Zurück zur Startseite
    const backToHomeButton = document.getElementById('backToHomeButton');

    if (backToHomeButton) {
        backToHomeButton.addEventListener('click', function () {
            window.location.href = '/';
        });
    }

    // Podcast erstellen
    const createPodcastButton = document.getElementById('createPodcastButton');

    if (createPodcastButton) {
        createPodcastButton.addEventListener('click', function () {
            fetch('/create_podcast', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
            })
                .then((response) => response.json())
                .then((data) => {
                    if (data.message) {
                        alert(data.message);
                    } else if (data.error) {
                        alert('Error: ' + data.error);
                    }
                })
                .catch((error) => {
                    console.error('Error:', error);
                });
        });
    }
});