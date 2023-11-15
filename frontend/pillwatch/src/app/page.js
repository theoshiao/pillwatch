import "bootstrap/dist/css/bootstrap.min.css";
import FileUpload from "./fileUpload";
import LiveCamera from "./liveCamera";

async function Home() {
  const res = await fetch("http://127.0.0.1:5000/api/time");
  const timestamp = await res.json();
  const date = new Date(timestamp.time*1000);
  return (
    <>
      <p> hello, it is {date.toDateString()} </p>
      <FileUpload />
      <LiveCamera />
    </>
  );
}

export default Home;
