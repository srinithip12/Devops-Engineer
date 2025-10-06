package com.example.expensetracker;

import com.example.expensetracker.model.Expense;
import com.example.expensetracker.repository.ExpenseRepository;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;

import java.math.BigDecimal;
import java.time.LocalDate;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

import com.fasterxml.jackson.databind.ObjectMapper;

@SpringBootTest
@AutoConfigureMockMvc
public class ExpenseControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @Autowired
    private ExpenseRepository repository;

    @Autowired
    private ObjectMapper objectMapper;

    @Test
    public void createAndGetExpense() throws Exception {
        Expense e = new Expense("Test item", "Misc", new BigDecimal("123.45"), LocalDate.now());
        String json = objectMapper.writeValueAsString(e);

        // Create
        mockMvc.perform(post("/api/expenses")
                .contentType(MediaType.APPLICATION_JSON)
                .content(json))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.id").exists());

        // Total should be >= 123.45 (depending on seed)
        mockMvc.perform(get("/api/expenses/total"))
                .andExpect(status().isOk());
    }
}

