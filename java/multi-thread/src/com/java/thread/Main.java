package com.java.thread;

/**
 * Created by damonl on 17-4-27.
 */
public class Main {

    public static void main(String args[]) {
        MyThread t1 = new MyThread("t1");
        MyThread t2 = new MyThread("t2");

//        t1.run();
//        t2.run();
        /**
         * 线程的启动是用start()方法
         */
        t1.start();
        t2.start();

        MyRunnable r1 = new MyRunnable("r1");
        MyRunnable r2 = new MyRunnable("r2");

        Thread t_1 = new Thread(r1);
        Thread t_2 = new Thread(r2);
        t_1.start();
        t_2.start();
    }
}
