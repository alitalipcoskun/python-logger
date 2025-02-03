from src.logger import CustomLogger

if __name__=="__main__":
    dict_test = {"test": "Bu bir deneme logudur"}
    logger = CustomLogger()
    logger.log(dict_test, "info")