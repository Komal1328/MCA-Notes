package com.example.student_budgtting_system_firebase;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.android.material.textfield.TextInputEditText;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;

public class RegisterPage extends AppCompatActivity {

    TextInputEditText email, password, name;

    Button register;

    TextView login;

    FirebaseAuth firebaseAuth = FirebaseAuth.getInstance();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register_page);

//        name = findViewById(R.id.nameR);
        email = findViewById(R.id.emailR);
        password = findViewById(R.id.passwordR);
        register = findViewById(R.id.register);
        login = findViewById(R.id.log_inR);

        login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(RegisterPage.this, MainActivity.class);
                startActivity(intent);
                finish();
            }
        });

        register.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                String e,p,n;
//                n = String.valueOf(name.getText());
                e = String.valueOf(email.getText());
                p = String.valueOf(password.getText());

//                if(TextUtils.isEmpty(n)){
//                    Toast.makeText(RegisterPage.this,"Enter Name", Toast.LENGTH_LONG).show();
//                    return;
//                }

                if(TextUtils.isEmpty(e)){
                    Toast.makeText(RegisterPage.this,"Enter Email", Toast.LENGTH_LONG).show();
                    return;
                }
                if(TextUtils.isEmpty(p)){
                    Toast.makeText(RegisterPage.this,"Enter Password", Toast.LENGTH_LONG).show();
                    return;
                }

                firebaseAuth.createUserWithEmailAndPassword(e,p)
                        .addOnCompleteListener(new OnCompleteListener<AuthResult>() {
                            @Override
                            public void onComplete(@NonNull Task<AuthResult> task) {
                                if(task.isSuccessful()){
                                    Toast.makeText(RegisterPage.this,"Registration Successful",Toast.LENGTH_LONG).show();
                                    Intent i = new Intent(RegisterPage.this,HomePage.class);
                                    startActivity(i);
                                    finish();
                                }
                                else {
                                    Toast.makeText(RegisterPage.this,"Registration failed",Toast.LENGTH_LONG).show();
                                }
                            }
                        });
            }
        });
    }
}