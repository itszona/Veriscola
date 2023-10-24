//to verify image capture against database using JavaScript

function logMessage(message) {
    const messageLog = document.getElementById('message-log');
    messageLog.textContent = message;

}

let cameraStream = undefined;
let imageBlob = undefined;
const video = document.getElementById('preview-video');
const queryCanvasElement = canvas = document.getElementById('canvas-results');
const captureButton = document.getElementById('capture');
const queryImageElement = capturedImage = document.getElementById('capture-img');

const MODEL_URL = '/static/models'
const FACE_MATCHER_THRESHOLD = 0.6;

document.addEventListener('DOMContentLoaded', async function () {
    await faceapi.loadSsdMobilenetv1Model(MODEL_URL)
    await faceapi.loadFaceLandmarkModel(MODEL_URL)
    await faceapi.loadFaceRecognitionModel(MODEL_URL)

});

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
            const imageUrl = URL.createObjectURL(blob);
            // Disable preview video
            video.style.display = 'none';
            capturedImage.src = imageUrl;
            capturedImage.style.display = 'block';
            imageBlob = blob;
        }
    )
});

const buildFaceMatcher = async () => {
    const label = document.getElementById('student-reg-no').textContent;
    const studentPicture = document.getElementById('saved-student-picture');
    const faceDescription = await faceapi.detectSingleFace(studentPicture)
        .withFaceLandmarks()
        .withFaceDescriptor();
    if (!faceDescription) {
        logMessage('No faces detected in saved Student Picture. User should update profile with a clearer image.')
        throw new Error(`no faces detected for ${label}`);
    }
    const faceDescriptors = [faceDescription.descriptor];
    const labeledFaceDescriptors = new faceapi.LabeledFaceDescriptors(label, faceDescriptors);
    const faceMatcher = new faceapi.FaceMatcher(
        labeledFaceDescriptors,
        FACE_MATCHER_THRESHOLD
    );
    return faceMatcher;
}

const loadRecognizedFaces = async () => {
    const resultsQuery = await faceapi.detectAllFaces(queryImageElement)
        .withFaceLandmarks()
        .withFaceDescriptors();

    await faceapi.matchDimensions(
        queryCanvasElement,
        queryImageElement
    );

    const results = await faceapi.resizeResults(resultsQuery, {
        width: queryImageElement.width,
        height: queryImageElement.height,
    });

    console.log('Face detection results: ', results);
    if (results.length <= 0) {
        logMessage('No faces detected in picture')
    }
    else {
        logMessage(`Faces found: ${results.length}`)
    }
    const faceMatcher = await buildFaceMatcher();
    console.log('Results length: ', results.length);
    const queryDrawBoxes = results.map((res) => {
        const bestMatch = faceMatcher.findBestMatch(res.descriptor);
        return new faceapi.draw.DrawBox(res.detection.box, {
            label: bestMatch.toString(),
        });
    });
    allFaceLabels = [];
    queryDrawBoxes.forEach((drawBox) => {
        drawBox.draw(queryCanvasElement);
        allFaceLabels.push(drawBox.label);
    });

    results.forEach((res) => {
        faceapi.draw.drawFaceLandmarks(queryCanvasElement, res);
    });

    const studentRegNo = document.getElementById('student-reg-no').textContent;
    JsBarcode("#barcode", studentRegNo + Math.random());
    // Function to convert SVG to PDF and print it
};

document.querySelector('.is-link').addEventListener('click', function(){
    const svgElement = document.getElementById('barcode');
    const barcode = new XMLSerializer().serializeToString(svgElement);
    
    const blob = new Blob([barcode], {type: 'image/svg+xml'})

    const url = URL.createObjectURL(blob)

    const a = document.createElement('a')
    a.href = url
    a.download = 'barcode.pdf'

    a.click()

    URL.revokeObjectURL(url)
})


//async function generateAndPrintPDF() {
  //  barcode = await document.getElementById().parentElement;
    
    // Use html2canvas to convert the barcode SVG to a canvas
//    await html2canvas(barcode, {useCORS: true}).then((canvas) => {});
//}

// Attach the function to the 'Generate PDF' button
//document.getElementById('generatePdf').addEventListener('click', generateAndPrintPDF);




function resetForCapture() {
    const context = canvas.getContext("2d");

    // Clear the entire canvas
    context.clearRect(0, 0, canvas.width, canvas.height);

    capturedImage.style.display = 'none';
    video.style.display = 'block';
    logMessage('');

}



    //document.getElementById('convert-to-pdf').addEventListener('click', function() {
    //    const svgElement = document.getElementById('barcode-container');

        // Use html2canvas to capture the SVG as an image
    //    html2canvas(svgElement).then(canvas => {
    //        const imgData = canvas.toDataURL('image/png');

            // Create a PDF document
    //        const pdf = new jsPDF();
      //      const imgWidth = 210;
    //        const pageHeight = 297;
     //       const imgHeight = (canvas.height * imgWidth) / canvas.width;
       //     let position = 0;

//            pdf.addImage(imgData, 'PNG', 0, position, imgWidth, imgHeight);

            // Save the PDF or open in a new tab
  //          pdf.save('barcode.pdf');
  //      });
    //});