package br.pucpr.projetowebservice.controller;

import br.pucpr.projetowebservice.dto.UsuarioDTO;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import jakarta.validation.Valid;
import jakarta.websocket.server.PathParam;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;

@RestController
@RequestMapping("/api/v1/usuario")
public class UsuarioController {

    private List<UsuarioDTO> usuarios = new ArrayList<>();

    @PostMapping
    public ResponseEntity<UsuarioDTO> save(@Valid @RequestBody UsuarioDTO usuarioDTO) {
        usuarioDTO.setId(1);
        usuarios.add(usuarioDTO);
        return ResponseEntity.status(HttpStatus.CREATED).body(usuarioDTO);
    }

    @GetMapping
    @Operation(summary = "obter usuario por ID", description = "retorna a lista de usuarios")
    @ApiResponses(value = {
            @ApiResponse (responseCode = "200", description = "Recuperado com sucesso"),
    })
    public List<UsuarioDTO> findAll() {
        return usuarios;
    }

    @PutMapping("/{id}")
    public UsuarioDTO update(@PathVariable("id") Integer id, @RequestBody UsuarioDTO usuarioDTO) {
        usuarioDTO.setId(id);
        return usuarioDTO;
    }

    @DeleteMapping("/{id}")
    public void delete(@PathVariable("id") Integer id) {
    }

}
