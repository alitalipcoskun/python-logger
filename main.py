from src import CustomLogger, TestClass

name = __name__

if __name__=="__main__":
    dict_test = {"test": "Bu bir deneme logudur"}
    main_logger = CustomLogger(name="main.py")
    main_logger.logger.info("Main class info log")
    test_class = TestClass()
    
    try:
        print(1/0)
    except Exception as e:
        main_logger.logger.error(e)
    