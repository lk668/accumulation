package com.java.generic;

/**
 * Created by damonl on 17-4-28.
 */
public class Point6 {

    public <T> void getArrayElement(T arr []){
        for(T i: arr){
            System.out.println(i);
        }
    }
}
