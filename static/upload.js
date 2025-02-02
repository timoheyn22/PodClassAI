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
    // Add click event listener to the language dropdown button
    if (selectLanguageButton) {
        selectLanguageButton.addEventListener('click', function () {
            toggleDropdown('languageDropdown');
        });
    }
    // Add click event listener to the speed dropdown button
    if (selectSpeedButton) {
        selectSpeedButton.addEventListener('click', function () {
            toggleDropdown('speedDropdown');
        });
    }

    // Event listeners for dropdown options
    const languageOptions = document.querySelectorAll('#languageDropdown a');
    const speedOptions = document.querySelectorAll('#speedDropdown a');

    // Update button text and toggle dropdown visibility when a language is selected
    languageOptions.forEach(option => {
        option.addEventListener('click', function () {
            updateButtonText('selectLanguageButton', this.textContent);
            toggleDropdown('languageDropdown');
            checkFormValidity();
        });
    });

    // Update button text and toggle dropdown visibility when a speed is selected
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

    // Grey Out the Create Podcast and Download Podcast buttons on Page Load
    createPodcastButton.classList.add('disabled-button');
    downloadPodcastButton.classList.add('disabled-button');


    // Event listener for PDF upload button and input
    const pdfInput = document.getElementById('pdfInput');
    const uploadNewPdfButton = document.getElementById('uploadNewPdfButton');
    const pdfContainer = document.getElementById('pdfContainer');

    // Handle Create Podcast button click to send selected options to the server
    if (createPodcastButton) {
        createPodcastButton.addEventListener('click', function () {
            const selectedLanguage = selectLanguageButton.textContent;
            const selectedSpeed = selectSpeedButton.textContent;

            // Send data to the server via a POST request
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
                        downloadPodcastButton.disabled = false; // Enable the download button
                        downloadPodcastButton.classList.remove('disabled-button'); // Enable the download button
                    } else if (data.error) {
                        alert('Error: ' + data.error);  // Display error message
                    }
                })
                .catch((error) => {
                    console.error('Error:', error);
                });
        });
    }

    // Trigger file input dialog when the Upload PDF button is clicked
    uploadNewPdfButton.addEventListener('click', () => {
        pdfInput.click();
    });

    // Handle PDF file upload
    pdfInput.addEventListener('change', (event) => {
    const file = event.target.files[0];
    if (file) {
        const formData = new FormData();
        formData.append('pdf', file);

        // Send the uploaded file to the server
        fetch('/upload_pdf', {
            method: 'POST',
            body: formData,
        })
        .then((response) => response.json())
        .then((data) => {
            if (data.success) {
                alert('PDF uploaded successfully!');
                uploadNewPdfButton.textContent = file.name; // Update button text to show file name
                const fileURL = URL.createObjectURL(file);
                pdfContainer.innerHTML = `<embed src="${fileURL}" type="application/pdf" width="100%" height="100%">`;
                checkFormValidity(); // Check if the form is valid
            } else {
                alert(`Error: ${data.error}`); // Display error message
            }
        })
        .catch((error) => {
            console.error('Error uploading PDF:', error);  // Log any errors
        });
    }
});

    // Function to check form validity and enable/disable the Create Podcast button
    function checkFormValidity() {
        const selectedLanguage = selectLanguageButton.textContent;
        const selectedSpeed = selectSpeedButton.textContent;
        const pdfUploaded = pdfInput.files.length > 0;

         // Enable the button if all Values are entered
        if (selectedLanguage !== 'Select language' && selectedSpeed !== 'Select speed' && pdfUploaded) {
            createPodcastButton.disabled = false;
            createPodcastButton.classList.remove('disabled-button');
        } else {
            createPodcastButton.disabled = true;
            createPodcastButton.classList.add('disabled-button');
        }
    }


    // Handle Download Podcast button click to download the generated file
    downloadPodcastButton.addEventListener('click', function () {
        const downloadLink = document.createElement('a');
        downloadLink.href = '../static/Uploads/MP3/output.mp3'; // File location
        downloadLink.download = 'output.mp3'; // Suggested file name
        downloadLink.style.display = 'none';
        document.body.appendChild(downloadLink);
        downloadLink.click(); // Trigger the download
        document.body.removeChild(downloadLink);
    });

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