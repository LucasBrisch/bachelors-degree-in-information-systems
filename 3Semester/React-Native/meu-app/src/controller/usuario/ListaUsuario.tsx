import { constants } from "os";
import React, { useEffect, useState } from "react";
import { UsuarioModel } from "../../model/Usuario.model";

const ListaUsuario: React.FC<{}> = ({ }) => {

    const [usuarios, setUsuarios] = useState<UsuarioModel[]>();

    const buscarUsuarios = () => {
        setUsuarios([
            {
                id: 1,
                nome: 'Cleverson',
                idade: 20,
                dataDeNascimento: '30/07/2012'
            },
            {
                id: 2,
                nome: 'Pedro',
                idade: 25,
                dataDeNascimento: '01/01/2010'
            }
        ])
    }

    return (
        <div>
            <input className="form-control" type="text"></input>
            <button onClick={buscarUsuarios} type="button" className="btn btn-primary">Pesquisar</button>
            <table className="table">
                <thead>
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col">Nome</th>
                        <th scope="col">Idade</th>
                        <th scope="col">Data de Nascimento</th>
                    </tr>
                </thead>
                <tbody>
                    {
                        usuarios?.map(usuario => {
                            return (
                                <tr>
                                    <th scope="row">{usuario.id}</th>
                                    <td>{usuario.nome}</td>
                                    <td>{usuario.idade}</td>
                                    <td>{usuario.dataDeNascimento}</td>
                                </tr>
                            )
                        })
                    }
                </tbody>
            </table>
        </div>
    );
}
export default ListaUsuario;