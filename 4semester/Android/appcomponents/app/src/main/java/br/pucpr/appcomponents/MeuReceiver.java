package br.pucpr.appcomponents;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.app.Service;
import android.content.Intent;
import android.os.IBinder;
import android.util.Log;
import android.widget.Toast;


public class MeuReceiver extends BroadcastReceiver {

    // Referência ao botão que será reabilitado ao receber a intent
    private final Button btnConsultar;

    /**
     * Construtor que recebe uma referência ao botão que será controlado pelo Receiver.
     * Este botão geralmente está na Activity principal e é desabilitado durante o processamento.
     *
     * @param btnConsultar botão que será reabilitado quando o cálculo terminar
     */
    public MeuReceiver(Button btnConsultar) {
        this.btnConsultar = btnConsultar;
    }

    /**
     * Método executado automaticamente quando a intent registrada é recebida.
     * Exibe uma notificação para o usuário e reabilita o botão.
     *
     * @param context o contexto da aplicação no momento da recepção
     * @param intent a intent recebida, que deve sinalizar o fim do processamento
     */
    @Override
    public void onReceive(Context context, Intent intent) {
        Log.d("AppVazio", "Intent recebida: " + intent.getAction());

        // Exibe uma mensagem ao usuário
        Toast.makeText(context, "Cálculo finalizado!", Toast.LENGTH_SHORT).show();

        // Reabilita o botão para permitir nova consulta
        btnConsultar.setEnabled(true);
    }
}
