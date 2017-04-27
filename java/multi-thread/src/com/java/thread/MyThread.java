package com.java.thread;

/**
 * Created by damonl on 17-4-27.
 */
public class MyThread extends Thread {

    private String name;

    public MyThread(String name) {
        this.name = name;
    }

    @Override
    public void run() {
        for(int i = 0; i <= 100; i++) {
            System.out.println(name + ":" + i);
        }
    }
}
