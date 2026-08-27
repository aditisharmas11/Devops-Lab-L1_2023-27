package com.arshansari.portfolio;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

class ProfileTest {
    @Test
    void summaryIncludesNameAndPrn() {
        Profile profile = new Profile("Arsh Ansari", "23070122047", "DevOps Lab L1 Maven Portfolio");
        String summary = profile.summary();
        assertTrue(summary.contains("Arsh Ansari"));
        assertTrue(summary.contains("23070122047"));
        assertEquals("Arsh Ansari", profile.name());
    }
}
