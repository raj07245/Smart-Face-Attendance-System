package com.attendance.faceattendance;

import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class AttendanceService {
    private final AttendanceRepository repository;

    public AttendanceService(AttendanceRepository repository) {
        this.repository = repository;
    }

    public List<Attendance> getAll() {
        return repository.findAll();
    }
}
