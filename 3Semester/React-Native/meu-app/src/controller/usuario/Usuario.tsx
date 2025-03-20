import { constants } from "os";
import React, { useEffect, useState } from "react";
import { UsuarioModel } from "../../model/Usuario.model";

const Usuario: React.FC<{}> = ({ }) => {

    const[nome, setNome] = useState('');
    const[idade, setIdade] = useState(0);
    const[dataDeNascimento, setDataDeNascimento] = useState('');

    const[usuario, setUsuario] = useState<UsuarioModel>();

    const salvar = () => {
        console.log('salvar');
        console.log(nome);
        console.log(idade);
        console.log(dataDeNascimento);
        setUsuario({
            id: 0,
            nome: nome,
            idade: idade,
            dataDeNascimento: dataDeNascimento
        });

       
        
    }  

    useEffect(() => {
        console.log(usuario)
    },[usuario]);

    return (
        <div>
            <div className="mb-3">
                <label className="form-label">Nome</label>
                <input type="text" className="form-control" id="nome" aria-describedby="nome" 
                    onChange={(e) => { setNome(e.target.value) }}/>                    
            </div>
            <div className="mb-3">
                <label className="form-label">Idade</label>
                <input type="number" className="form-control" id="idade" aria-describedby="idade"
                    onChange={(e) => { setIdade(parseInt(e.target.value)) }} />                    
            </div>
            <div className="mb-3">
                <label className="form-label">Data de Nascimento</label>
                <input type="date" className="form-control" id="dataDeNascimento" aria-describedby="data de nascimento" 
                    onChange={(e) => { setDataDeNascimento(e.target.value) }}/>                    
            </div>
            <button type="button" className="btn btn-primary"
                onClick={salvar}>Salvar</button>

            <div>
                {nome} <br/>
                {idade} <br/>
                {dataDeNascimento} <br/>
            </div>            
        </div>        
    );
}
export default Usuario;