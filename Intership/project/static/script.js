
const fileInput = document.getElementById('imageInput');

// Get the element to display the selected file
const selectedFileDisplay = document.getElementById('selectedFileDisplay');

// Add event listener for change event
fileInput.addEventListener('change', function() {
    // Check if files are selected
    if (fileInput.files.length > 0) {
        // Files are selected
        const selectedFile = fileInput.files[0];
        // Display the selected file name
        selectedFileDisplay.textContent = `Selected file: ${selectedFile.name}`;
    } else {
        // No files selected
        selectedFileDisplay.textContent = 'No file selected';
    }
});

function uploadImage() {
    const fileInput = document.getElementById('imageInput');
    const file = fileInput.files[0];
    if (!file) {
        alert('Please select an image.');
        return;
    }

    const formData = new FormData();
    formData.append('image', file);

    fetch('/detect', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        displayResults(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function displayResults(results) {
    const outputDiv = document.getElementById('output');
    outputDiv.innerHTML = '';

    if (results.error) {
        outputDiv.innerHTML = `<p>Error: ${results.error}</p>`;
    } else {
        const imageElement = document.createElement('img');
        imageElement.src = results.image_path;
        imageElement.classList.add('output-image');
        outputDiv.appendChild(imageElement);

        const objectsList = document.createElement('ul');
        results.objects.forEach(obj => {
            const listItem = document.createElement('li');
            listItem.textContent = `${obj.class} - Confidence: ${obj.confidence}`;
            objectsList.appendChild(listItem);
        });
        outputDiv.appendChild(objectsList);
    }
}
