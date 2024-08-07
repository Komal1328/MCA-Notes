package com.example.student_budgtting_system_firebase;

import androidx.annotation.NonNull;
import androidx.appcompat.app.ActionBarDrawerToggle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;
import androidx.core.view.GravityCompat;
import androidx.drawerlayout.widget.DrawerLayout;

import android.content.Intent;
import android.os.Bundle;
import android.view.MenuItem;
import android.widget.Toast;

import com.google.android.material.navigation.NavigationView;

public class HomePage extends AppCompatActivity implements NavigationView.OnNavigationItemSelectedListener {
    private DrawerLayout drawerLayout;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home_page);

        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        drawerLayout = findViewById(R.id.drawer_layout);
        NavigationView navigationView = findViewById(R.id.nav_view);
        navigationView.setNavigationItemSelectedListener(this);

        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(this, drawerLayout, toolbar, R.string.open_nav,
                R.string.close_nav);
        drawerLayout.addDrawerListener(toggle);
        toggle.syncState();

        if (savedInstanceState == null) {
            getSupportFragmentManager().beginTransaction().replace(R.id.fragment_container, new HomeFragment()).commit();
            navigationView.setCheckedItem(R.id.nav_home);
        }
    }

    public boolean onNavigationItemSelected(@NonNull MenuItem item) {
        int itemId = item.getItemId();
        if (itemId == R.id.nav_home) {
            getSupportFragmentManager().beginTransaction().replace(R.id.fragment_container, new HomeFragment()).commit();
        }
        else if (itemId == R.id.nav_info) {
            getSupportFragmentManager().beginTransaction().replace(R.id.fragment_container, new InfoFragment()).commit();
        }
        else if (itemId == R.id.nav_prof) {
            getSupportFragmentManager().beginTransaction().replace(R.id.fragment_container, new ProfFragment()).commit();
        }
        else if (itemId == R.id.nav_food) {
            getSupportFragmentManager().beginTransaction().replace(R.id.fragment_container, new FoodFragment()).commit();
        }
        else if (itemId == R.id.nav_other) {
            getSupportFragmentManager().beginTransaction().replace(R.id.fragment_container, new OtherFragment()).commit();
        }
        else if (itemId == R.id.nav_month) {
            getSupportFragmentManager().beginTransaction().replace(R.id.fragment_container, new MonthFragment()).commit();
        }
        else if (itemId == R.id.nav_logout) {
            Intent i = new Intent(HomePage.this,MainActivity.class);
            startActivity(i);
            Toast.makeText(this, "Logout!", Toast.LENGTH_SHORT).show();
        }
//        switch (item.getItemId()) {
//            case R.id.nav_home:
//                getSupportFragmentManager().beginTransaction().replace(R.id.fragment_container, new HomeFragment()).commit();
//                break;
//            case R.id.nav_info:
//                getSupportFragmentManager().beginTransaction().replace(R.id.fragment_container, new InfoFragment()).commit();
//                break;
//            case R.id.nav_prof:
//                getSupportFragmentManager().beginTransaction().replace(R.id.fragment_container, new ProfFragment()).commit();
//                break;
//            case R.id.nav_food:
//                getSupportFragmentManager().beginTransaction().replace(R.id.fragment_container, new FoodFragment()).commit();
//                break;
//            case R.id.nav_other:
//                getSupportFragmentManager().beginTransaction().replace(R.id.fragment_container, new OtherFragment()).commit();
//                break;
//            case R.id.nav_month:
//                getSupportFragmentManager().beginTransaction().replace(R.id.fragment_container, new MonthFragment()).commit();
//                break;
//            case R.id.nav_logout:
//                Toast.makeText(this, "Logout!", Toast.LENGTH_SHORT).show();
//                break;
//        }
        drawerLayout.closeDrawer(GravityCompat.START);
        return true;
    }
    @Override
    public void onBackPressed() {
        if (drawerLayout.isDrawerOpen(GravityCompat.START)) {
            drawerLayout.closeDrawer(GravityCompat.START);
        } else {
            super.onBackPressed();
        }
    }
}