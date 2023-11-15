"use client";
import { useCallback, useState, useRef } from "react";
import Webcam from "react-webcam";
import { submitFile } from './api';

export default function LiveCamera() {
  const [canAccessCamera, setCanAccessCamera] = useState(false);
  const [cameraFacingModeFront, setCameraFacingModeFront] = useState(true);
  const webcamRef = useRef(null);
  const [img, setImg] = useState(null);
  const [response, setResponse] = useState(null);

  const videoConstraints = cameraFacingModeFront
    ? {
        facingMode: "user",
      }
    : { facingMode: { exact: "environment" } };

  const capture = useCallback(() => {
    const imageSrc = webcamRef.current.getScreenshot();
    setImg(imageSrc);
    console.log(img);
  }, [webcamRef]);

  const handleTakePhoto = () => {
    capture();
    if (img) {
        fetch(img)
        .then(res => res.blob())
        .then(blob => {
             const file = new File([blob], "capture",{ type: "image/png" })
             submitFile(file, setResponse);
             setCanAccessCamera(false);
        })



    }
  };

  return (
    <div>
      <h2>Camera</h2>
      <button onClick={() => setCanAccessCamera(!canAccessCamera)}>
        Toggle Camera
      </button>

      {canAccessCamera && (
        <div>
          <Webcam
            ref={webcamRef}
            screenshotFormat="image/jpeg"
            videoConstraints={videoConstraints}
          />
          <button onClick={handleTakePhoto}>Capture</button>

          <button
            onClick={() => setCameraFacingModeFront(!cameraFacingModeFront)}
          >
            Switch Camera Direction
          </button>
        </div>
      )}
      {response && (
        <div>
          <p>Response from server:</p>
          <pre>{JSON.stringify(response, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}
