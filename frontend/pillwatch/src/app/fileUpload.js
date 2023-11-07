'use client';
import { useState } from 'react';
import { submitFile } from './api';

function FileUpload() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [response, setResponse] = useState(null);

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    setSelectedFile(file)
  };
  const handleSubmit = (e) => {
    submitFile(selectedFile, setResponse);
  }

  return (
    <div>
      <h2>File Upload</h2>
      <input type="file" onChange={handleFileChange} />
      {selectedFile && (
        <div>
          <p>Selected File: {selectedFile.name}</p>
          <p>File size: {selectedFile.size} bytes</p>
          <p>File type: {selectedFile.type}</p>
        </div>
      )}
      <button onClick={handleSubmit}>Submit</button>
      {response && (
        <div>
          <p>Response from server:</p>
          <pre>{JSON.stringify(response, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default FileUpload;