from factory import ExtractorFactory
import utils

if __name__ == '__main__':
    config_dict = utils.get_configs()
    builders = config_dict.get("builders")

    factory = ExtractorFactory(builders)
    builder = factory.get_builder("DOU")

    # if builder.verify_today_diary():
    diary = factory.factory("DOU")
    diary.extract()
