package br.pucpr.appcomponents;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

import androidx.annotation.Nullable;

public class BancoHelper extends SQLiteOpenHelper {

    public BancoHelper(@Nullable Context context) {
        super(context, "MEU.DB", null, 1);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        db.execSQL("CREATE TABLE resultados(" +
                "_id INTEGER PRIMARY KEY AUTOINCREMENT," +
                "resultado INTEGER)");
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        db.execSQL("DROP TABLE IF EXISTS resultados");
        onCreate(db);
    }
}
