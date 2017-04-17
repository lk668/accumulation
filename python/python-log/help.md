#### format的格式说明


| 属性名称 | 格式 | 说明 |
| :------: | :--: | :--: |
| name	| %(name)s	| 日志的名称 |
| asctime |	%(asctime)s |	可读时间，默认格式‘2003-07-08 16:49:45,896’，逗号之后是毫秒 |
| filename |	%(filename)s |	文件名，pathname的一部分 |
| pathname |	%(pathname)s |	文件的全路径名称 |
| funcName |	%(funcName)s |	调用日志多对应的方法名 |
| levelname |	%(levelname)s |	日志的等级 |
| levelno | %(levelno)s	| 数字化的日志等级 |
| lineno | %(lineno)d |	被记录日志在源码中的行数 |
| module | %(module)s |	模块名 |
| msecs	| %(msecs)d	| 时间中的毫秒部分 |
| process |	%(process)d	| 进程的ID |
| processName |	%(processName)s	| 进程的名称 |
| thread	| %(thread)d	| 线程的ID |
| threadName	| %(threadName)s |	线程的名称 |
| relativeCreated |	%(relativeCreated)d |	日志被创建的相对时间，以毫秒为单位 |
