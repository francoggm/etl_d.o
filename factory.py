import utils

class ExtractorFactory:
    def __init__(self, builders_name : list):
        self._builders = {}

        if builders_name:
            self._register_builders_from_config(builders_name)

    def get_builder(self, diary):
        return self._builders.get(diary)

    def _register_builders_from_config(self, builders_name):
        for builder in builders_name:
            builder_class = utils.import_class(f"diary.{builder}", builder)

            if builder_class:
                self._builders[builder] = builder_class

    def factory(self, diary, **kwargs):
        builder = self._builders.get(diary)
        if not builder:
            raise ValueError(diary)

        return builder(**kwargs)
