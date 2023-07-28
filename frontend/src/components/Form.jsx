// import { useState } from "react";
import "../assets/Form.css";
import "../index.css";

export default function Form() {
  // const [newQuery, setNewQuery] = useState("");

  // this is for displaying the search query of the user
  // const [queries, setQueries] = useState([]);

  // function that will
  function handleSearch(e) {
    e.preventDefault();
  }

  return (
    <>
      <form onSubmit={handleSearch} action="" className="form">
        <div className="input-row">
          <label htmlFor="query">Search for any scientific paper</label>
          <input
            type="text"
            name="query"
            className="input-field"
            // value={query}
            // onChange={(e) => setQuery(e.target.value)}
          />
        </div>
        <div className="input-row">
          <input type="submit" value={"Search"} />
        </div>
      </form>
    </>
  );
}
