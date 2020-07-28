学习笔记
# 多进程
* os.fork()
* from multiprocessing import Process
    * 进程的getpid() getppid()
    * active_children()
    * name
    * cpu_count()

## "__name__" 如何使用？
如果单独运行这个文件的话，会运行如下
```python
if __name__ == '__main__':
    print('do something')
``` 
如果该文件是被引入其他的文件的话，改代码不会执行

## 多进程通信
无法通过变量赋值的方式进行数据共享
* 队列（最流行）基于管道，
* 管道：比队列更原始
* 共享内存：Value 和 Array

## 锁

## 进程池


处理多任务，可以多进程、多线程、协程

## 多线程
* 阻塞和非阻塞针对发起方，同步异步针对被调用方
* 并发 并行
* 在 I/O 密集情况下多有优势，cpython是伪多线程，同一时间只有一个线程，
当开启多线程的时候只是在不停地再这些线程中切换，当在cpu密集情况下，多线程会比单线程慢

```python
threading.Thread(target=run, args=("thread 1",))
```
