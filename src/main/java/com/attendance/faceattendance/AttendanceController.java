package com.attendance.faceattendance;
import org.springframework.ui.Model;

import java.io.BufferedReader;
import java.io.File;
import java.io.InputStreamReader;
import java.util.List;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class AttendanceController {

    private final AttendanceRepository attendanceRepository;

    public AttendanceController(AttendanceRepository attendanceRepository) {
        this.attendanceRepository = attendanceRepository;
    }


       @GetMapping("/login")
    public String loginPage() {
        return "login"; // ye login.html ko load karega
    }



    @GetMapping("/")
    public String home() {
        return "index"; // index.html render hoga
    }

    @GetMapping("/run-script")
    public String runScript(Model model) {
        try {
            // Load Python script from resources dynamically
           ClassLoader classLoader = getClass().getClassLoader();
           File scriptFile = new File(classLoader.getResource("Scripts/face_attendance/simple_attendance.py").getFile());
           String scriptPath = scriptFile.getAbsolutePath();

           String pythonPath = "/Library/Frameworks/Python.framework/Versions/3.13/bin/python3";

           ProcessBuilder pb = new ProcessBuilder(pythonPath, scriptPath);
           pb.directory(scriptFile.getParentFile());

            Process process = pb.start();

            BufferedReader reader = new BufferedReader(
                    new InputStreamReader(process.getInputStream())
            );

            String line;
            StringBuilder output = new StringBuilder();
            while ((line = reader.readLine()) != null) {
                output.append(line).append("\n");
            }

            process.waitFor();

            // Output ko model me bhejna UI ke liye
            model.addAttribute("result", output.toString());

        } catch (Exception e) {
            e.printStackTrace();
            model.addAttribute("result", "⚠️ Error running script: " + e.getMessage());
        }
        return "index"; // same page pe result show hoga
    }

      @GetMapping("/attendance")
    public String viewAttendance(Model model) {
        List<Attendance> records = attendanceRepository.findAll();
        model.addAttribute("attendanceList", records);
        return "attendance"; // attendance.html
    }

    
}
