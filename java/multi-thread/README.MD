#### Java 实现多线程

1. 方法一为继承Thread类
2. 方法二为实现Runnable方法


#### Java 多线程Thread类的主要方法

- getName():获取线程的名字（获取名字的前提是先获取该线程）
- Thread.currentThread():获取当前的线程（static方法）
- isAlive():判断线程是否启动
- join():线程的强行运行
- Thread.sleep():线程的休眠
- Thread.yield():线程的礼让(static方法)
