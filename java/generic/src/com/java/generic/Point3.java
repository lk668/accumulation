package com.java.generic;

/**
 * Created by damonl on 17-4-28.
 */
public class Point3<T> {

    private T key;

    public void setKey(T key) {
        this.key = key;
    }

    public T getKey() {
        return key;
    }
}
