package com.arshansari.portfolio;

public final class Profile {
    private final String name;
    private final String prn;
    private final String title;

    public Profile(String name, String prn, String title) {
        this.name = name;
        this.prn = prn;
        this.title = title;
    }

    public String name() {
        return name;
    }

    public String prn() {
        return prn;
    }

    public String title() {
        return title;
    }

    public String summary() {
        return name + " (" + prn + ") — " + title;
    }
}
