package com.attendance.faceattendance;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.web.SecurityFilterChain;

@Configuration
public class SecurityConfig {


    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        http
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/login", "/css/**", "/js/**", "/images/**").permitAll() // login page allow
                .anyRequest().authenticated()
            )
            .formLogin(form -> form
                .loginPage("/login")  // custom login page
                .permitAll()
            )
            .logout(logout -> logout.permitAll());

        return http.build();
    }

}
