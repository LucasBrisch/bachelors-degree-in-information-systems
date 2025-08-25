package br.pucpr.appcomponents;

import android.app.Service;
import android.content.Intent;
import android.os.IBinder;
import android.util.Log;

public class MeuService extends Service {
    public MeuService() {
    }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {

        // Recupera os valores enviados pela Activity
        double primeiro = intent.getDoubleExtra("primeiro", 0.0);
        double segundo = intent.getDoubleExtra("segundo", 0.0);

        // Executa o cálculo como soma repetida
        double resultado = 0;
        for (int i = 0; i < segundo; i++) {
            resultado += primeiro;
        }

        Log.d("AppComponentes", "Valor A: " + primeiro);
        Log.d("AppComponentes", "Valor B: " + segundo);
        Log.d("AppComponentes", "Resposta: " + resultado);


        // Envia uma Intent broadcast avisando que o cálculo terminou
        Intent broadcastIntent = new Intent("CALCULO_FINALIZADO");
        sendBroadcast(broadcastIntent);

        // Encerra o serviço após a execução
        stopSelf();

        // Indica que o serviço não será recriado automaticamente
        return START_NOT_STICKY;



    }

    @Override
    public IBinder onBind(Intent intent) {
        // TODO: Return the communication channel to the service.
        throw new UnsupportedOperationException("Not yet implemented");
    }
}