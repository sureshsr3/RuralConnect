// // captureButton.addEventListener('click', function() {
// //     // Access the webcam
// //     navigator.mediaDevices.getUserMedia({ video: true })
// //     .then(function(stream) {
// //         // Display the stream from the webcam in a video element
// //         const video = document.createElement('video');
// //         document.body.appendChild(video);
// //         video.srcObject = stream;
// //         video.play();

// //         // Create a canvas element to capture the image
// //         const canvas = document.createElement('canvas');
// //         canvas.width = video.videoWidth;
// //         canvas.height = video.videoHeight;
// //         const context = canvas.getContext('2d');

// //         // Create a capture button
// //         const captureButton = document.createElement('button');
// //         captureButton.textContent = "Capture";
// //         document.body.appendChild(captureButton);

// //         // Capture image from the video stream when capture button is clicked
// //         captureButton.onclick = function() {
// //             // Draw the current frame from the video onto the canvas
// //             context.drawImage(video, 0, 0, canvas.width, canvas.height);

// //             // Stop the video stream
// //             stream.getTracks().forEach(track => track.stop());

// //             // Convert canvas content to base64 data URL
// //             const imageData = canvas.toDataURL('image/jpeg');

// //             // Set the captured image as the source of the uploadedImage element
// //             uploadedImage.src = imageData;

// //             // Call the processImage function with the captured image data
// //             processImage(imageData);

// //             // Upload the captured image to the server
// //             uploadImage(imageData);

// //             // Remove video, canvas, and capture button elements from the DOM
// //             video.remove();
// //             canvas.remove();
// //             captureButton.remove();
// //         };
// //     })
// //     .catch(function(error) {
// //         console.error('Error accessing the webcam: ', error);
// //     });
// // });

// // function uploadImage(imageData) {
// //     // Create a FormData object to send image data to server
// //     const formData = new FormData();
// //     formData.append('image', imageData);

// //     // Send image data to server using AJAX
// //     fetch('upload.php', {
// //         method: 'POST',
// //         body: formData
// //     })
// //     .then(response => {
// //         if (!response.ok) {
// //             throw new Error('Failed to upload image');
// //         }
// //         return response.text();
// //     })
// //     .then(data => {
// //         console.log('Image uploaded successfully:', data);
// //     })
// //     .catch(error => {
// //         console.error('Error uploading image:', error);
// //     });
// // }

// const fileInput = document.getElementById('fileInput');
// const extractButton = document.getElementById('extractButton');
// const uploadedImage = document.getElementById('uploadedImage');
// const outputDiv = document.getElementById('output');
// const documentTypeSelect = document.getElementById('documentType');

// let imageName = ""; // Variable to store the image name
// let selectedDocumentType = ""; // Variable to store the selected document type

// fileInput.addEventListener('change', function(event) {
//     const file = event.target.files[0];
//     const reader = new FileReader();

//     reader.onload = function(e) {
//         uploadedImage.src = e.target.result;
//     };

//     reader.readAsDataURL(file);
//     imageName = file.name; // Extract the image name
// });

// documentTypeSelect.addEventListener('change', function(event) {
//     selectedDocumentType = event.target.value; // Store the selected document type
// });

// extractButton.addEventListener('click', function() {
//     if (!imageName) {
//         console.error('Error: No image selected');
//         return;
//     }

//     if (!selectedDocumentType) {
//         console.error('Error: No document type selected');
//         return;
//     }

//     const imageData = uploadedImage.src;

//     // Pass image data, name, and document type to processing function
//     processImage(imageData, imageName, selectedDocumentType);
// });

// function processImage(imageData, imageName, documentType) {
//     // You can write your image processing code here
//     // Example: Display image name, document type, and data
//     outputDiv.innerHTML = `<p>Image Name: ${imageName}</p>`;
//     outputDiv.innerHTML += `<p>Document Type: ${documentType}</p>`;
//     outputDiv.innerHTML += `<p>Image Data: ${imageData}</p>`;
// }



const fileInput = document.getElementById('fileInput');
const extractButton = document.getElementById('extractButton');
const uploadedImage = document.getElementById('uploadedImage');
const outputDiv = document.getElementById('output');
const documentTypeSelect = document.getElementById('documentType');

let imageName = ""; // Variable to store the image name

fileInput.addEventListener('change', function(event) {
    const file = event.target.files[0];
    const reader = new FileReader();

    reader.onload = function(e) {
        uploadedImage.src = e.target.result;
    };

    reader.readAsDataURL(file);
    imageName = file.name; // Extract the image name
});

extractButton.addEventListener('click', function() {
    if (!imageName) {
        console.error('Error: No image selected');
        return;
    }

    const selectedDocumentType = documentTypeSelect.value;
    
    // Create a FormData object to send image data and document type to server
    const formData = new FormData();
    formData.append('fileInput', fileInput.files[0]);
    formData.append('documentType', selectedDocumentType);

    // Send image data and document type to server for processing
    fetch('/extract', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Display the output returned by the server
        outputDiv.innerHTML = data.output;
    })
    .catch(error => {
        console.error('Error processing image:', error);
    });
});
