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
