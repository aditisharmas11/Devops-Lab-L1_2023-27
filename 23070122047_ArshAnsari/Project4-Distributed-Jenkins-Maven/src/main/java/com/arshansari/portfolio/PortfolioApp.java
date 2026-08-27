package com.arshansari.portfolio;

public final class PortfolioApp {
    public static void main(String[] args) {
        Profile profile = new Profile(
            "Arsh Ansari",
            "23070122047",
            "DevOps Lab L1 Maven Portfolio"
        );
        System.out.println(profile.summary());
        System.out.println("Built by a distributed Jenkins pipeline (slave-1 compile/package, slave-2 tests).");
    }
}
