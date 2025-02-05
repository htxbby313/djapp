import React from "react";

function App() {
  return (
    <div>
      <h1>🎵 DJ Streaming App</h1>
      <video controls>
        <source src="https://ns1.idgt.me:10000/stream" type="video/mp4" />
      </video>
    </div>
  );
}

export default App;
