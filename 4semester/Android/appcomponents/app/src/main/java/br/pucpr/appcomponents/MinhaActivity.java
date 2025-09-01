package br.pucpr.appcomponents;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.os.Build;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MinhaActivity extends AppCompatActivity {

    private Button btnIniciar, btnConsultar;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_minha);
//        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
//            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
//            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
//            return insets;
//        });

        btnIniciar = findViewById(R.id.btnIniciar);
        btnConsultar = findViewById(R.id.btnConsultar);

        EditText edtTxtPrimeiro = findViewById(R.id.edtPrimeiro);
        EditText edtTxtSegundo = findViewById(R.id.edtSegundo);

        btnIniciar.setOnClickListener( v -> {
            String primeiro = edtTxtPrimeiro.getText().toString();
            Double vlrPrimeiro = Double.parseDouble(primeiro);

            String segundo = edtTxtSegundo.getText().toString();
            Double vlrSegundo = Double.parseDouble(segundo);

            Intent intencao = new Intent(this, MeuService.class);
            intencao.putExtra("primeiro", vlrPrimeiro);
            intencao.putExtra("segundo", vlrSegundo);

            startService(intencao);

            // Toast.makeText(this, "Clicou", Toast.LENGTH_LONG).show();
        });

        btnConsultar.setOnClickListener(v -> {
            Intent intent = new Intent(this, SegundaActivity.class);
            startActivity(intent);
        });

    }

    private BroadcastReceiver meuReceiver;

    @Override
    protected void onStart() {
        super.onStart();

        meuReceiver = new MeuReceiver(btnConsultar);
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            registerReceiver(meuReceiver, new IntentFilter("CALCULO_FINALIZADO"), Context.RECEIVER_EXPORTED);
        }
    }

    @Override
    protected void onStop() {
        super.onStop();

        unregisterReceiver(meuReceiver);
    }
}