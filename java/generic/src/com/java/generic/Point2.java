package com.java.generic;

/**
 * 泛型构造函数
 * Created by damonl on 17-4-28.
 */
public class Point2<T> {

    private T value;

    public Point2(T value) {
        this.value = value;
    }

    public T getValue() {
        return value;
    }

    public void setValue(T value) {
        this.value = value;
    }
}

/**
 * 多个泛型
 * @param <K>
 * @param <T>
 */
class MultiGeneric<K, T>{
    private K v1;
    private T v2;

    public K getV1() {
        return v1;
    }

    public void setV1(K v1) {
        this.v1 = v1;
    }

    public T getV2() {
        return v2;
    }

    public void setV2(T v2) {
        this.v2 = v2;
    }
}
