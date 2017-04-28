package com.java.generic;

/**
 * Created by damonl on 17-4-28.
 */

interface PointIn <T> {

    public T say();
}
public class Point4 implements PointIn {

    private String info;

    public Point4 (String info){
        this.info = info;
    }

    @Override
    public String say(){
        return ""+info;
    }
}
