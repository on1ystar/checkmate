const video2 = document.getElementById('videoElementElement')

Promise.all([
  faceapi.nets.tinyFaceDetector.loadFromUri('/static/'),
  faceapi.nets.faceLandmark68Net.loadFromUri('/static/'),
]).then(startVideo)

function startVideo() {
  navigator.getUserMedia(
    { video2: {} },
    stream => video2.srcObject = stream,
    err => console.error(err)
  )
}

video2.addEventListener('play', () => {
  const canvas = faceapi.createCanvasFromMedia(video2)
  document.body.append(canvas)
  const displaySize = { width: video2.width, height: video2.height }
  faceapi.matchDimensions(canvas, displaySize)
  setInterval(async () => {
    const detections = await faceapi.detectAllFaces(video2, new faceapi.TinyFaceDetectorOptions()).withFaceLandmarks().withFaceExpressions()
    const resizedDetections = faceapi.resizeResults(detections, displaySize)
    canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height)
    faceapi.draw.drawDetections(canvas, resizedDetections)
    faceapi.draw.drawFaceLandmarks(canvas, resizedDetections)
  }, 100)
})