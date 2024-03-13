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

public class MainActivity extends AppCompatActivity {

    TextInputEditText email, password;

    Button login;

    TextView signup;

    FirebaseAuth firebaseAuth = FirebaseAuth.getInstance();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        email = findViewById(R.id.email);
        password = findViewById(R.id.password);
        login = findViewById(R.id.log_in);
        signup = findViewById(R.id.sign_up);

        signup.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(MainActivity.this, RegisterPage.class);
                startActivity(intent);
                finish();
            }
        });

        login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String e = email.getText().toString().trim();
                String p = password.getText().toString().trim();

                if (TextUtils.isEmpty(e)) {
                    Toast.makeText(MainActivity.this, "Enter Email", Toast.LENGTH_LONG).show();
                    return;
                }
                if (TextUtils.isEmpty(p)) {
                    Toast.makeText(MainActivity.this, "Enter Password", Toast.LENGTH_LONG).show();
                    return;
                }

                firebaseAuth.signInWithEmailAndPassword(e, p)
                        .addOnCompleteListener(new OnCompleteListener<AuthResult>() {
                            @Override
                            public void onComplete(@NonNull Task<AuthResult> task) {
                                if (task.isSuccessful()) {
                                    // Authentication successful
                                    Toast.makeText(MainActivity.this, "Login successful", Toast.LENGTH_LONG).show();
                                    Intent i = new Intent(MainActivity.this, HomePage.class);
                                    startActivity(i);
                                    finish();
                                } else {
                                    // If sign in fails, display a message to the user.
                                    if (task.getException() != null) {
                                        String errorMessage = task.getException().getMessage();

                                        if (errorMessage.contains("INVALID_EMAIL")) {
                                            Toast.makeText(MainActivity.this, "Invalid email address", Toast.LENGTH_LONG).show();
                                        } else if (errorMessage.contains("USER_NOT_FOUND")) {
                                            Toast.makeText(MainActivity.this, "User not found", Toast.LENGTH_LONG).show();
                                        } else if (errorMessage.contains("WRONG_PASSWORD")) {
                                            Toast.makeText(MainActivity.this, "Wrong password", Toast.LENGTH_LONG).show();
                                        } else {
                                            Toast.makeText(MainActivity.this, "Authentication failed: " + errorMessage, Toast.LENGTH_LONG).show();
                                        }
                                    }
                                }
                            }
                        });
            }
        });
    }
}
