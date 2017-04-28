package com.java.generic;

/**
 * Created by damonl on 17-4-27.
 */
public class Main {
    public static void main(String[] args) {
        /**
         * 基本泛型使用
         */
        Point<String> p_s = new Point();
        Point<Integer> p_i = new Point();

        p_s.setX("11");
        p_s.setY("101");
        p_i.setX(10);
        p_i.setY(100);

        System.out.println("x=" + p_s.getX() + "   y=" + p_s.getY());
        System.out.println("x=" + p_i.getX() + "   y=" + p_i.getY());

        /**
         * 构造函数泛型
         */
        Point2<Integer> p2_i = new Point2<>(10);
        Point2<String> p2_s = new Point2<>("构造方法中使用泛型");

        System.out.println("value=" + p2_s.getValue());
        System.out.println("value=" + p2_i.getValue());

        /**
         * 多泛型使用
         */
        MultiGeneric<String, Integer> mg = new MultiGeneric<>();
        mg.setV1("多泛型使用");
        mg.setV2(10);
        System.out.println("Key: " + mg.getV1() + "  Value: " + mg.getV2());

        /**
         * 通配符案例调用
         */
        Point3<String> p3_s = new Point3<>();
        p3_s.setKey("Test 通配符");
        getPoint3Info(p3_s);

        /**
         * 接口泛型
         */
        Point4 p4 = new Point4("Test generic interface");
        System.out.println(p4.say());

        /**
         * 泛型方法
         */
        Point5 p5 = new Point5();
        System.out.println(p5.tell("Test generic function"));

        /**
         * 泛型数组
         */
        Point6 p6 = new Point6();
        String arr_string[] = {"string1-泛型数组", "string2-泛型数组"};
        Integer arr_int[] = {1,2,3};
        p6.getArrayElement(arr_string);
        p6.getArrayElement(arr_int);

    }

    /**
     * 通配符的使用
     * @param info
     */
    public static void getPoint3Info(Point3<?> info){
        System.out.println(info.getKey());
    }
}
