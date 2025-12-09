package com.attendance.faceattendance;

import jakarta.persistence.*;

@Entity
public class Attendance {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;
    private String date;
    private String status; // Present / Absent
    private String time;


    // ✅ Getter & Setter for id
    public Long getId() {
        return id;
    }
    public void setId(Long id) {
        this.id = id;
    }

    // ✅ Getter & Setter for name
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }

    // ✅ Getter & Setter for date
    public String getDate() {
        return date;
    }
    public void setDate(String date) {
        this.date = date;
    }

    // ✅ Getter & Setter for status
    public String getStatus() {
        return status;
    }
    public void setStatus(String status) {
        this.status = status;
    }

    // ✅ Getter & Setter for time
    public String getTime() {
        return time;
    }
    public void setTime(String time) {
        this.time = time;
    }
}
