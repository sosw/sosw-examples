
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src="sosw_logo.png" className="App-logo" alt="logo" />
        <img src="sosw_logo_text.png" className="App-logo-text" />
      </header>
      <div className="App-content">
        <div>
          <h1 className="h1">CRUD-functions</h1>
        </div>
        <div>
          <label htmlFor="tableName" className="table-name-label">Table name:</label>
          <input id="tableName" className="mb-2 form-control tableNameIn" placeholder="Table name" />

        </div>
        <div>
 <button className="btn btn-table" /*onClick={addTodoHandler}*/>
            Find table
          </button>
        </div>
      </div>
      <div className="App-content">
        <h1 className="h1">List Table</h1>
      </div>
    </div>
  );
}

export default App;
