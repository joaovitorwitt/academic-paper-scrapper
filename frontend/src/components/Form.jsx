import "../assets/Form.css";
import "../index.css";

export default function Form() {
  return (
    <>
      <section>
        <div className="container">
          <div className="form-wrapper">
            <div className="form-data-description">
              <p>
                Here you can search for scientific papers on different subjects
              </p>
            </div>

            <form action="">
              <div className="input-row">
                <label htmlFor=""></label>
                <input type="text" placeholder="Type something" />
              </div>
              <div className="input-row">
                <input type="submit" value={"Search"} />
              </div>
            </form>
          </div>
        </div>
      </section>
    </>
  );
}
