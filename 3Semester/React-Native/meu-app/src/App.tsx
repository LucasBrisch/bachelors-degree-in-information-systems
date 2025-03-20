import React from 'react';
import './App.css';
import Menu from './layout/Menu';
import Usuario from './controller/usuario/Usuario';
import ListaUsuario from './controller/usuario/ListaUsuario';


function App() {
  return (
    <div className='container'>
      <Usuario></Usuario>
      <ListaUsuario></ListaUsuario>
      
      {/* <form>
        <div className="mb-3">
          <label className="form-label">Email address</label>
          <input type="email" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp"></input>            
        </div>
        <button className="btn btn-primary">Salvar</button>
      </form> */}


    </div>
  );
}

export default App;
