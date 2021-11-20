from base import Base

class Index(Base):
    def init(self, **kwargs):
        kwargs['file_names'] = ['index.html', 'mksite.toml']
        self.copy_newer_files(**kwargs)

    def build(self, **kwargs):
        pass
    def publish(self, **kwargs):
        pass
