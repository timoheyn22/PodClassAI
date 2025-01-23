document.addEventListener('DOMContentLoaded', function () {
    // Function to toggle the visibility of dropdown contents
    function toggleDropdown(dropdownId) {
        document.getElementById(dropdownId).classList.toggle('show');
    }

    // Function to update button text with selected dropdown value
    function updateButtonText(buttonId, value) {
        document.getElementById(buttonId).textContent = value;
    }

    // Event listeners for language and speed dropdowns
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

    // Event listeners for dropdown options
    const languageOptions = document.querySelectorAll('#languageDropdown a');
    const speedOptions = document.querySelectorAll('#speedDropdown a');

    languageOptions.forEach(option => {
        option.addEventListener('click', function () {
            updateButtonText('selectLanguageButton', this.textContent);
            toggleDropdown('languageDropdown');
            checkFormValidity();
        });
    });

    speedOptions.forEach(option => {
        option.addEventListener('click', function () {
            updateButtonText('selectSpeedButton', this.textContent);
            toggleDropdown('speedDropdown');
            checkFormValidity();
        });
    });

    // Event listener for the Create Podcast button
    const createPodcastButton = document.getElementById('createPodcastButton');
    const downloadPodcastButton = document.getElementById('downloadPodcastButton');

    // Set initial disabled-button class on page load
    createPodcastButton.classList.add('disabled-button');
    downloadPodcastButton.classList.add('disabled-button');

    // Event listener for PDF upload button and input
    const pdfInput = document.getElementById('pdfInput');
    const uploadNewPdfButton = document.getElementById('uploadNewPdfButton');
    const pdfContainer = document.getElementById('pdfContainer');

    if (createPodcastButton) {
        createPodcastButton.addEventListener('click', function () {
            const selectedLanguage = selectLanguageButton.textContent;
            const selectedSpeed = selectSpeedButton.textContent;

            fetch('/create_podcast', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ language: selectedLanguage, speed: selectedSpeed }),
            })
                .then((response) => response.json())
                .then((data) => {
                    if (data.message) {
                        alert(data.message);
                        downloadPodcastButton.disabled = false;
                        createPodcastButton.classList.remove('disabled-button'); // Enable the download button
                    } else if (data.error) {
                        alert('Error: ' + data.error);
                    }
                })
                .catch((error) => {
                    console.error('Error:', error);
                });
        });
    }
    uploadNewPdfButton.addEventListener('click', () => {
        pdfInput.click();
    });

    pdfInput.addEventListener('change', (event) => {
        const file = event.target.files[0];
        if (file) {
            const fileURL = URL.createObjectURL(file);

            // Anzeigen des Dateinamens auf dem Button
            uploadNewPdfButton.textContent = file.name;

            // PDF in den Container einbetten
            pdfContainer.innerHTML = `<embed src="${fileURL}" type="application/pdf" width="100%" height="100%">`;
            checkFormValidity();
        }
    });

    // Function to check form validity and enable/disable the Create Podcast button
function checkFormValidity() {
    const selectedLanguage = selectLanguageButton.textContent;
    const selectedSpeed = selectSpeedButton.textContent;
    const pdfUploaded = pdfInput.files.length > 0;

    if (selectedLanguage !== 'Select language' && selectedSpeed !== 'Select speed' && pdfUploaded) {
        createPodcastButton.disabled = false;
        createPodcastButton.classList.remove('disabled-button');
    } else {
        createPodcastButton.disabled = true;
        createPodcastButton.classList.add('disabled-button');
    }
}

    // Close the dropdown when clicking outside of it
    window.addEventListener('click', function (event) {
        if (!event.target.matches('#selectLanguageButton') && !event.target.matches('#selectSpeedButton')) {
            const dropdowns = document.getElementsByClassName('dropdown-content');
            for (let i = 0; i < dropdowns.length; i++) {
                const openDropdown = dropdowns[i];
                if (openDropdown.classList.contains('show')) {
                    openDropdown.classList.remove('show');
                }
            }
        }
    });
});
