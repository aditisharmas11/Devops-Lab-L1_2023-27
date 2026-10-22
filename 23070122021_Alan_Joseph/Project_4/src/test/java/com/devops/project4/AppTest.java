package com.devops.project4;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class AppTest {
    @Test
    public void addsTwoNumbers() {
        assertEquals(5, App.add(2, 3));
    }
}
