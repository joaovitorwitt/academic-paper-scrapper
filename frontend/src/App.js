import "./index.css";
import HomePage from "./pages/HomePage";
import jsonData from "./links.json";

function App() {
  function renderJSON() {
    fetch(jsonData)
      .then((response) => response.json())
      .then((json) => console.log(json))
      .catch((err) => console.log(err));
  }

  renderJSON();

  return <HomePage />;
}

export default App;
