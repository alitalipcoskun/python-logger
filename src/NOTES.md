# Logging
It is used for monitoring the software events that occured in runtime. The event is described by a descriptive message, and it may contain data which is related to program flow.

## Accessing Logger
Logging functionality is accessed by creating a logger. The logger methods such as `debug, info, warning, critical, error` are called to obtain necesarry functionality.

```python
# logger declaration
logger = getLogger(__name__)
```

In order to report events that occur during normal operation of a program, `info and debug` are used.

To parse warning regarding a particular runtime event, `warn` is used.

To report an error in a specific runtime event, `raise an exception`.

To report suppression of an error without raising an exception, `exception, critical, error` are used.

| Level     | When it’s used                                                                 |
|-----------|------------------------------------------------------------------------------|
| DEBUG     | Detailed information, typically of interest only when diagnosing problems.  |
| INFO      | Confirmation that things are working as expected.                           |
| WARNING   | An indication that something unexpected happened, or indicative of a problem in the near future (e.g. ‘disk space low’). The software is still working as expected. |
| ERROR     | Due to a more serious problem, the software has not been able to perform some function. |
| CRITICAL  | A serious error, indicating that the program itself may be unable to continue running. |

## Level Configuration
The level configuration of logger is important to parse the logs onto the console or a file. The default level is `WARNING`, thus `DEBUG and INFO` logs are not available if you do not change the configuration.

## Creating logger file
One of the best practices to store logs is naming the log file as the date and time of the runtime.

It is obtained from `datetime` module.

```python
from datetime import datetime

# The variable contains month, day, year, hour minute and second of the runtime as the name of the log file
filename = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
```
# Advanced Logging
The library has a modularity for several categories:

- *Loggers (logger class)* expose the interface that application code directly uses.
- *Handlers* send the log records (created by loggers) to appropriate destination
- Filters provide a finer grained facility for determining which log records to output.
- Formatters specify the layout of log records in the final output

`Note that the log event information is passed between loggers, handlers, filters and formatters in a LogRecord instance.`

## Level Setting
```python
logger.setLevel(level)
```
The method sets the treshould for this logger to `level`. Logging messages which are less crucial will be ignored.

## Handlers
These objects are used for dispatching the appropriate log messages to the specified destination of the desired location which is also conducted by the handler objects.

For example, the application may want to send all log messages to a log file. All logs will be stored in the log file. In addition, critical log messages will be sent to specified e-mail address. As a result, we need FileHandler and SMTPHandler for this scenario.

Application code should not directly instantiate and use instances of Handler. Instead, the Handler class is a base class that defines the interface that all handlers should have and establishes some default behavior that child classes can use (or override).

### StreanHandler
If stream is specified, the instance will use it for logging output; otherwise, sys.stderr will be used.

### FileHandler
The FileHandler class, located in the core logging package, sends logging output to a disk file. It inherits the output functionality from StreamHandler.

`RotatingFileHandler and TimedRotatingFileHandler` are used for helpful to maintain and analyze the log files.
It will be discussed in future.
