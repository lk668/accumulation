package com.java.generic;

/**
 * 泛型基本使用
 * Created by damonl on 17-4-27.
 */
public class Point <T> {

    T x;
    T y;

    public T getX() {
        return x;
    }

    public T getY() {
        return y;
    }

    public void setX(T x) {
        this.x = x;
    }

    public void setY(T y) {
        this.y = y;
    }
}
