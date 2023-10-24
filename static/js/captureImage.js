let cameraStream = undefined;
let imageBlob = undefined;
const video = document.getElementById('preview-video');
const canvas = document.getElementById('canvas');
const captureButton = document.getElementById('capture');
const capturedImage = document.getElementById('capture-img');


// Check if the browser supports getUserMedia
if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
    alert('Your browser does not support the getUserMedia API.');
} else {
    // Access the webcam
    navigator.mediaDevices.getUserMedia({ video: true })
        .then((stream) => {
            cameraStream = stream;
            video.srcObject = stream;
        })
        .catch((error) => {
            console.error('Error accessing webcam: ', error);
            alert('Error accessing webcam');
        });
}

// Capture button click event
captureButton.addEventListener('click', () => {
    const mediaStreamTrack = cameraStream.getVideoTracks()[0];
    const imageCapture = new ImageCapture(mediaStreamTrack);

    const photoOptions = {
        imageWidth: 1920,
        imageHeight: 1080,
        format: 'image/jpeg', // Set the format to JPG
    };

    imageCapture.takePhoto(photoOptions).then(
        (blob) => {
            // Disable preview video
            video.style.display = 'none';
            const imageUrl = URL.createObjectURL(blob);
            capturedImage.src = imageUrl;
            capturedImage.style.display = 'block';
            imageBlob = blob;
        }
    )
});


function saveStudentToAPI() {
    const studentName = document.getElementById('student-name').value;
    const registrationNo = document.getElementById('registration-no').value;
    const department = document.getElementById('department').value;
    const studentLevel = document.getElementById('student-level').value;

    const courses = document.getElementsByClassName('student-course');
    let selectedCourses = []
    for (const course of courses) {
        if (course.checked) {
            selectedCourses.push(course.value);
        }
    }

    const formData = new FormData();
    formData.append("name", studentName);
    formData.append("registration_no", registrationNo);
    formData.append("department", department);
    formData.append("level", studentLevel);
    formData.append("courses", selectedCourses);
    formData.append("student_picture", new File([imageBlob], 'student_picture.jpg'));


    // const student
    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    const headers = new Headers({
        "X-CSRFToken": csrfToken
    });

    // Make the fetch request
    fetch(document.URL, {
        method: 'POST',
        body: formData,
        headers,
    })
        .then(response => {
            if (response.ok) {
                // Handle the response here
                window.location.replace("/list");
            } else {
                // Handle errors
                console.error("Request failed:", response.status);
                const formErrors = document.getElementById('form-errors');
                response.text().then((t) => { console.log(t); formErrors.innerHTML = t; });
            }
        })
        .catch(error => {
            // Handle network errors
            console.error("Network error:", error);
        });
}

const form = document.getElementById("student-reg-form");
if (form) {
    form.addEventListener("submit", function (event) {
        // Prevent the form from submitting by default
        event.preventDefault();

        // Get all required form elements
        const requiredElements = form.querySelectorAll("[required]");

        let isValid = true;

        // Image should have been captured
        if (!imageBlob) {
            video.style.border = "5px solid red";
            alert('Yet to snap a picture!')
            return
        }

        // Loop through the required elements
        requiredElements.forEach(function (element) {
            if (element.value.trim() === "") {
                isValid = false;
                // Optionally, you can add visual feedback (e.g., highlighting the empty field).
                element.style.border = "2px solid red";
            } else {
                // Remove the red border if the field is filled in.
                element.style.border = "";
            }
        });

        if (isValid) {
            saveStudentToAPI();
        }
    });
}

function resetForCapture() {
    capturedImage.style.display = 'none';
    video.style.display = 'block';
}