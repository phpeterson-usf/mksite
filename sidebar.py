from base import Base

class Sidebar(Base):
    def init(self, **kwargs):
        kwargs['file_names'] = ['sidebar.md', 'sidebar.css', 'logo.png']
        self.copy_newer_files(**kwargs)

    def build(self, **kwargs):
        self.mustache_newer_files(kwargs['mustache_sources'])

    def publish(self, **kwargs):
        pass
