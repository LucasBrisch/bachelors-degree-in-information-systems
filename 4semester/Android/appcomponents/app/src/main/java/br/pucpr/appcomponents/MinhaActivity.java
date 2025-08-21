package br.pucpr.appcomponents;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.os.Bundle;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import android.widget.EditText;
import android.widget.Toast;
import android.widget.Button;

public class MinhaActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_minha);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });

        EditText edtPrimeiro = findViewById(R.id.editTextText3);
        EditText edtSegundo = findViewById(R.id.editTextText4);

        Button btnIniciar = findViewById(R.id.button3);
        Button btnconsultar = findViewById(R.id.button4);

        btnIniciar.setOnClickListener(v -> {
            double primeiro = Double.parseDouble(edtPrimeiro.getText().toString());
            double segundo = Double.parseDouble(edtSegundo.getText().toString());

            Intent intent = new Intent(this, MeuService.class);
            intent.putExtra("prieiro", primeiro);
            intent.putExtra("segundo", segundo);

            Toast.makeText(this, "clicou", Toast.LENGTH_LONG).show();
        });

        btnconsultar.setOnClickListener ( v -> {
            Intent intent = new Intent(this, SegundaActivity.class);
            startActivity(intent);
        });
    }
}