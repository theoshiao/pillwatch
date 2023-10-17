import "bootstrap/dist/css/bootstrap.min.css";

async function Home() {
  const res = await fetch("http://127.0.0.1:5000/api/time");
  const time = await res.json();
  console.log(time);
  return (
    <>
      <h1> hello, it is {time.time} </h1>
    </>
  );
}

export default Home;
